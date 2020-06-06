import requests
from bs4 import BeautifulSoup
from scrapers.abstractscraper import AbstractScraper


class TheRobotReport_Scraper(AbstractScraper):

    def get_items(self):
        super().get_items()

        links = super().parse_standard_rss(self.url)
        self.links = links

    def cycle_items(self):
        super().cycle_items()

        return self.links

    def get_item_text(self, url):
        pass

        super().get_item_text(url)

        try:
            headers = super().set_headers()
            results = requests.get(url.strip(), headers=headers)

            soup = BeautifulSoup(results.text, "html.parser")
            # outer = soup.find('div', class_ = 'storyContainer')
            content_div = soup.find('div', class_ ='entry-content')

            text = super().clean_text(content_div)
        except:
            # TODO write exception to log for analysis
            text = ''

        return (text)
