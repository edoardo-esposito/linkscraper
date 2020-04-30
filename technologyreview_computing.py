import urllib
from urllib.request import urlopen
import requests
from requests import get
from bs4 import BeautifulSoup
import re
from abstractscraper import AbstractScraper


class TechnologyReview_Computing_Scraper(AbstractScraper):

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
            # outer = soup.find('div', class_ = 'storyContainer')
            content_div = soup.find('div', id='content--body')

            text = super().clean_text(content_div)
        except:
            # TODO write exception to log for analysis
            text = ''

        return (text)


def run():
    URL = "https://www.technologyreview.com/c/computing/rss/"
    sito = 'Technology Review Computing'
    s = TechnologyReview_Computing_Scraper(URL, sito)
    s.get_items()
    items = s.cycle_items()

    print(items)


if __name__ == '__main__':
    run()
