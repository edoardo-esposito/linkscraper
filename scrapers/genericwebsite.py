import requests
from bs4 import BeautifulSoup
from scrapers.abstractscraper import AbstractScraper
from utils import get_today_date, generate_link_id
import time, random, string

TEST = False


class GenericWebsite_Scraper(AbstractScraper):

    def __init__(self, url, sitename, params):

        print("Activating generic scaper")

        self.url = url
        self.sitename = sitename
        self.params = params

    def delay(self):
        if TEST: return None

        min = 5
        max = 10
        t = random.uniform(min, max)
        print("Delay %d" % t)
        time.sleep(t)
        return None

    def parse_page(self, url):
        links = []

        base_url = self.params['base_url']
        article_selector = self.params['article_selector']
        title_selector = self.params['title_selector']
        link_selector = self.params['link_selector']

        if 'date_selector' in self.params:
            date_selector = self.params['date_selector']
        else:
            date_selector = None

        try:
            headers = super().set_headers()
            results = requests.get(url.strip(), headers=headers)
            # print (results.text)

            soup = BeautifulSoup(results.text, "html.parser")
            articles = soup.select(article_selector)
            # print (article_selector)
            # print (articles)

            if articles:
                print ("Getting links")

                if TEST:
                    print ("Len: %d" % len(articles))

                for article in articles:

                    try:
                        title = article.select(title_selector)[0].text.strip()
                        if TEST:
                            print("---------------------------------")
                            print(title)

                        link = article.select(link_selector)[0]['href']
                        if not link.startswith("http"):
                            link = base_url + link

                        if TEST:
                            print("---------------------------------")
                            print(link)

                        date = ''
                        try:
                            if date_selector:
                                date = article.select(date_selector)[0].text.strip()
                        except Exception as e1:
                            print("Exception in parse_page > for loop > get date")

                        if TEST:
                            print(date)

                        links.append({
                            'id': generate_link_id(title),
                            'titolo': title,
                            'text': '',
                            'url': link,
                            'data': date
                        })

                        if TEST:
                            break
                    except Exception as e:
                        # TODO write exception to log for analysis
                        print("Exception in parse_page > for loop")
                        print(e)

            self.delay()

        except Exception as e:
            # TODO write exception to log for analysis
            print ("Exception in parse_page")
            print(e)
            links = []

        return links

    def get_items(self):
        super().get_items()

        if isinstance(self.url, list):
            # print(len(self.url))
            links = []
            for u in self.url:
                l = self.parse_page(u)
                links = links + l[:len(l)]
        else:
            links = self.parse_page(self.url)

        self.delay()
        # links = self.parse_page(self.url)
        self.links = links

        # print (links)

    def cycle_items(self):
        super().cycle_items()

        return self.links

    def get_item_text(self, url):
        super().get_item_text(url)

        content_selector = self.params['content_selector']

        try:
            headers = super().set_headers()
            results = requests.get(url.strip(), headers=headers)

            soup = BeautifulSoup(results.text, "html.parser")
            content = soup.select(content_selector)

            text = super().clean_text(content[0].text)
        except Exception as e:
            # TODO write exception to log for analysis
            print ("Exception in get_item_text")
            print (e)
            text = ''

        self.delay()
        return (text)

    def get_item_date(self, url):
        # super().get_item_text(url)

        content_date_selector = self.params['content_date_selector']

        try:
            headers = super().set_headers()
            results = requests.get(url.strip(), headers=headers)

            soup = BeautifulSoup(results.text, "html.parser")
            content = soup.select(content_date_selector)

            date = super().clean_text(content[0].text)
            if TEST:
                print("---------------------------------")
                print ("Date: %s" % date)
        except Exception as e:
            # TODO write exception to log for analysis
            print ("Exception in get_item_date")
            print (e)
            date = ''

        self.delay()
        return (date)

