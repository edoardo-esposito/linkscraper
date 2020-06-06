import requests
from bs4 import BeautifulSoup
from scrapers.abstractscraper import AbstractScraper


class TechXplore_Scraper(AbstractScraper):

    def get_items(self):
        super().get_items()

        if isinstance(self.url, list):
            print (len(self.url))
            links = []
            for u in self.url:
                l = super().parse_standard_rss(u)
                links = links + l[:len(l)]
        else:
            links = super().parse_standard_rss(self.url)

        self.links = links
        # self.links = []

    def cycle_items(self):
        super().cycle_items()

        return self.links

    def get_item_text(self, url):
        super().get_item_text(url)

        try:
            headers = super().set_headers()
            results = requests.get(url.strip(), headers=headers)

            soup = BeautifulSoup(results.text, "html.parser")
            content_div = soup.find('div', class_='article-main')

            text = super().clean_text(content_div)
        except:
            # TODO write exception to log for analysis
            text = ''

        # print (text)

        return (text)
