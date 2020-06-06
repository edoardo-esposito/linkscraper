import requests
from bs4 import BeautifulSoup
from scrapers.abstractscraper import AbstractScraper


class AdWeek_Scraper(AbstractScraper):

    def get_items(self):
        super().get_items()

        links = super().parse_standard_rss(self.url)
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
            content_div = soup.find('div', class_='post-text')

            text = super().clean_text(content_div)
        except:
            # TODO write exception to log for analysis
            text = ''

        # print (text)

        return (text)


def run():
    URL = "https://www.adweek.com/feed/"
    sito = 'Adweek'
    s = AdWeek_Scraper(URL, sito)
    s.get_items()
    items = s.cycle_items()

    print(items)


if __name__ == '__main__':
    run()

