import requests
from bs4 import BeautifulSoup
from abstractscraper import AbstractScraper


class Calcatech_Scraper(AbstractScraper):

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
        # super().get_item_text(url)
        #
        # try:
        #     headers = super().set_headers()
        #     results = requests.get(url.strip(), headers=headers)
        #     soup = BeautifulSoup(results.text, "html.parser")
        #     article = soup.find('div', class_="main-article")
        #     div = soup.find_all('div', class_="article-body")
        #
        #     print (len(div))
        #     print (div)
        #
        #     text = ""
        #     # if div:
        #     #     pars = div.find_all('p')
        #     #     print (pars)
        #     #
        #     #     for p in pars:
        #     #         t = super().clean_paragraph(p)
        #     #         text += t
        # except Exception as e:
        #     # TODO write exception to log for analysis
        #     print(e)
        #     text = ''
        #
        # print (text)
        #
        # return (text)


def run():
    URL = "https://www.calcalistech.com/GeneralRSSCtech/0,16665,L-5211,00.xml"
    sito = "Calcatech"
    s = Calcatech_Scraper(URL, sito)
    s.get_items()
    items = s.cycle_items()
    print(items)
    s.items_to_csv()


if __name__ == '__main__':
    run()