import requests
from bs4 import BeautifulSoup
from scrapers.abstractscraper import AbstractScraper
from utils import get_today_date, generate_link_id


#TODO scraper doubles elements
class Israel21c_Scraper(AbstractScraper):

    def parse_page(self, url):
        links = []

        headers = super().set_headers()
        results = requests.get(url.strip(), headers=headers)

        soup = BeautifulSoup(results.text, "html.parser")
        container = soup.find('div', id='topics')
        articles = container.find_all('article', class_='item')

        if articles:
            for article in articles:
                if article.find('h1'):
                    title = article.find('h1').find('a').contents[0]
                    href = article.find('h1').find('a')['href']
                    data = article.find('div', class_="date").text.strip()
                    links.append({
                        'id': generate_link_id(title),
                        'titolo': title,
                        'text': '',
                        'url': href,
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

    def cycle_items(self):
        super().cycle_items()

        return self.links

    def get_item_text(self, url):
        super().get_item_text(url)

        try:
            headers = super().set_headers()
            results = requests.get(url.strip(), headers=headers)

            soup = BeautifulSoup(results.text, "html.parser")
            container = soup.find('div', class_='article-body')

            text = ''
            if container:
                pars = container.find_all('p')

                for p in pars:
                    t = super().clean_paragraph(p)
                    text += t + ' '

        except:
            # TODO write exception to log for analysis
            text = ''

        return (text)