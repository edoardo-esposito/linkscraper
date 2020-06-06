import requests
from bs4 import BeautifulSoup
from scrapers.abstractscraper import AbstractScraper
from utils import get_today_date, generate_link_id


class GenericWebsite_Scraper(AbstractScraper):

    def __init__(self, url, sitename, params):

        print("Activating generic scaper")

        self.url = url
        self.sitename = sitename
        self.params = params

    def parse_page(self, url):
        links = []

        base_url = self.params['base_url']
        article_selector = self.params['article_selector']
        title_selector = self.params['title_selector']
        link_selector = self.params['link_selector']

        if self.params['date_selector']:
            date_selector = self.params['date_selector']
        else:
            date_selector = None

        try:
            headers = super().set_headers()
            results = requests.get(url.strip(), headers=headers)

            soup = BeautifulSoup(results.text, "html.parser")
            articles = soup.select(article_selector)

            if articles:
                for article in articles:
                    title = article.select(title_selector)[0].text

                    link = article.select(link_selector)[0]['href']
                    if not link.startswith(base_url):
                        link = base_url + link

                    date = ''
                    if date_selector:
                        date = article.select(date_selector)[0].text

                    # print(title)
                    # print(link)
                    # print(date)

                    links.append({
                        'id': generate_link_id(title),
                        'titolo': title,
                        'text': '',
                        'url': link,
                        'data': date
                    })

                    # break

        except Exception as e:
            # TODO write exception to log for analysis
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
        except:
            # TODO write exception to log for analysis
            text = ''

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
        except:
            # TODO write exception to log for analysis
            date = ''

        return (date)

