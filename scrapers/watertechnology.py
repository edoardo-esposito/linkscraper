import requests
from bs4 import BeautifulSoup
from scrapers.abstractscraper import AbstractScraper
from utils import get_today_date, generate_link_id


#TODO scraper doubles elements
class WaterTechnology_Scraper(AbstractScraper):

    def get_items(self):
        super().get_items()

        today = get_today_date()

        headers = super().set_headers()
        results = requests.get(self.url.strip(), headers=headers)

        soup = BeautifulSoup(results.text, "html.parser")
        container = soup.find('article', class_='main-feature')
        title = container.find('h2')

        links = [{
            'id': generate_link_id(title.text),
            'titolo': title.text,
            'text': '',
            'url': title.find('a').get('href'),
            'data': today
        }]

        def get_links_from_structure(articles):
            links = []
            rows = articles.find_all('div', class_='row')

            for row in rows:
                a = row.find('a')

                if a:
                    h3 = a.find('h3')

                    if h3:

                        links.append({
                            'id': generate_link_id(h3.text),
                            'titolo': h3.text,
                            'text': '',
                            'url': a.get('href'),
                            'data': today
                            })

            return links

        container = soup.find('div', class_='cards')
        links = get_links_from_structure(container)

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
            container = soup.find('div', class_='post-content-container')

            text = ''
            if container:
                pars = container.find_all('p')

                for p in pars:
                    t = super().clean_paragraph(p)
                    # text += t
                    text += t + ' '

        except:
            # TODO write exception to log for analysis
            text = ''

        return (text)


def run():
    # TODO move url to generic config file (same for execute.py)
    URL = "https://www.water-technology.net/technology/"
    sito = 'Water-Technology'
    s = WaterTechnology_Scraper(URL, sito)
    # s.get_items()
    # items = s.cycle_items()

    # print(items)


if __name__ == '__main__':
    run()
