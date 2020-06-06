import requests
from bs4 import BeautifulSoup
from scrapers.abstractscraper import AbstractScraper


class TechnologyOrg_Scraper(AbstractScraper):

    def get_items(self):
        super().get_items()

        links = super().parse_standard_rss(self.url)
        self.links = links

        print (links)


    def cycle_items(self):
        super().cycle_items()

        return self.links

    def get_item_text(self, url):
        super().get_item_text(url)

        try:
            headers = super().set_headers()
            results = requests.get(url.strip(), headers=headers)
            soup = BeautifulSoup(results.text, "html.parser")
            article = soup.find('div', id="technology-org-primary")
            content_div = article.find_all('div', class_="entry-content")

            text = ""
            if div:
                pars = div.find_all('p')

                for p in pars:
                    t = super().clean_paragraph(p)
                    # text += t.text()
                    text += t + ' '
        except:
            # TODO write exception to log for analysis
            text = ''

        print (text)

        return (text)


def run():
    URL = "http://feeds.feedburner.com/TechnologyOrgSpotlightNews?format=xml"
    sito = 'Technology Org'
    s = TechnologyOrg_Scraper(URL, sito)

    s.get_items()
    items = s.cycle_items()
    s.items_to_csv()
    # print(items)


if __name__ == '__main__':
    run()