import requests
from bs4 import BeautifulSoup
from abstractscraper import AbstractScraper


class TheRobotReport_Scraper(AbstractScraper):

    def get_items(self):
        super().get_items()

        links = super().parse_standard_rss(self.url)
        self.links = links

        print (links)

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
            content_div = soup.find('div', id='content--body')

            text = super().clean_text(content_div)
        except:
            # TODO write exception to log for analysis
            text = ''

        return (text)


def run():
    URL = "https://www.therobotreport.com/feed/"
    sito = "The Robot Report"
    s = TheRobotReport_Scraper(URL, sito)
    s.get_items()
    items = s.cycle_items()
    print(items)
    s.items_to_csv()


if __name__ == '__main__':
    run()


