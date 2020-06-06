import requests
from bs4 import BeautifulSoup
from scrapers.abstractscraper import AbstractScraper
from utils import get_today_date, generate_link_id


class GreenBiz_Scraper(AbstractScraper):

    def parse_page(self, url):
        links = []

        headers = super().set_headers()
        results = requests.get(url.strip(), headers=headers)

        soup = BeautifulSoup(results.text, "html.parser")
        container = soup.find('ul', class_='collection-page__list')

        articles = container.find_all('article')

        if articles:
            for article in articles:
                if article.find('h2'):
                    title = article.find('h2').find('a').contents[0].text
                    href = article.find('h2').find('a')['href']
                    data = article.find('p', class_="article-teaser-vertical__date").text.strip()

                    # print(title)
                    # print (href)
                    # print (data)


                    links.append({
                        'id': generate_link_id(title),
                        'titolo': title,
                        'text': '',
                        'url': "https://www.greenbiz.com" + href,
                        'data': data
                    })

        return links

    def get_items(self):
        super().get_items()

        if isinstance(self.url, list):
            print (len(self.url))
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

        try:
            headers = super().set_headers()
            results = requests.get(url.strip(), headers=headers)
            soup = BeautifulSoup(results.text, "html.parser")
            article = soup.find('div', class_="article__body")

            text = ""
            if article:
                pars = article.find_all('p')

                for p in pars:
                    t = super().clean_paragraph(p)
                    # text += p.text
                    text += t + ' '
        except:
            # TODO write exception to log for analysis
            text = ''

        return (text)
