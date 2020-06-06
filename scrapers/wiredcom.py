import requests
from bs4 import BeautifulSoup
from scrapers.abstractscraper import AbstractScraper


class WiredCom_Scraper(AbstractScraper):

    def get_items(self):
        super().get_items()

        links = super().parse_standard_rss(self.url)
        self.links = links

#        print (links)

    def get_items_from_file(self):
        from csv import reader
        from datetime import date

        filename = "customlinks.csv"
        with open(filename, "r") as source:
            rdr = reader(source, delimiter=";")

            links = []
            for row in rdr:
                s = row[2]
                u = row[1]
                t = row[0]

                if s == "Wired":

                    today = date.today()
                    d = today.strftime("%Y-%m-%d")

                    titolo = t
                    link_id = self.generate_link_id(titolo)

                    links.append({
                        'id': link_id,
                        'titolo': titolo,
                        'url': u,
                        'data': d
                    })

            print (links)
            self.links = links

    def cycle_items(self):
        super().cycle_items()

        return self.links

    def get_item_text(self,url):
        super().get_item_text(url)

        try:
            headers = super().set_headers()
            results = requests.get(url.strip(), headers=headers)

            soup = BeautifulSoup(results.text, "html.parser")
            outer = soup.find('div', class_ = 'body__container')

            text = ""
            if outer:
                pars = outer.find_all('p')
    
                for p in pars:
                    t = super().clean_paragraph(p)
                    # text += t
                    text += t + ' '
        except Exception as e:
            # TODO write exception to log for analysis
            print(e)
            text = ''

        return (text)


def run(): 
    URL = "https://www.wired.com/feed/"
    sito = "Wired"
    s = WiredCom_Scraper(URL, sito)

    s.get_items()
    # s.get_items_from_file()
    items = s.cycle_items()

    # s.items_to_csv()
#    print (items)


if __name__ == '__main__':
    run()

