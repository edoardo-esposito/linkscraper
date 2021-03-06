import hashlib
import requests
from bs4 import BeautifulSoup
from scrapers.abstractscraper import AbstractScraper


class Futurism_Scraper(AbstractScraper):

    def get_items(self):
        super().get_items()

        headers = super().set_headers()
        results = requests.get(self.url.strip(), headers=headers)

        soup = BeautifulSoup(results.text, "html.parser")
        container = soup.find('div', class_='container')

        titles = soup.find_all('h4', class_='card-title')

        links = []
        for obj in titles:
            titolo = obj.get_text()
            links.append({
                'id': hashlib.md5(titolo.encode('utf-8')).hexdigest(),
                'titolo': titolo,
                'url': obj.find('a').get('href'),
                'data': ''
            })

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
            content_div = soup.find(attrs={"itemprop": "articleBody"})

            text = super().clean_text(content_div)
        except Exception as e:
            # TODO write exception to log for analysis
            print(e)
            text = ''

        return text


def run():
    #TODO move url to generic config file (same for execute.py)
    URL = "https://feeder.co/discover/085f3bc023/futurism-com"
    sito = "Futurism"
    s = Futurism_Scraper(URL, sito)
    s.get_items()
    items = s.cycle_items()

    print(items)


if __name__ == '__main__':
    run()
