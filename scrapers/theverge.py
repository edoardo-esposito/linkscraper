import requests
from bs4 import BeautifulSoup
from scrapers.abstractscraper import AbstractScraper

class TheVerge_Scraper(AbstractScraper):

    def get_items(self):
        super().get_items()

        links = super().parse_atom_rss(self.url)
        self.links = links

#        print (links)

    def cycle_items(self):
        super().cycle_items()

        return self.links

    def get_item_text(self,url):
        super().get_item_text(url)

        headers = super().set_headers()
        results = requests.get(url.strip(), headers=headers)
        soup = BeautifulSoup(results.text, "html.parser")
        div = soup.find('div', class_="l-col__main")

        text = ""
        if div:
            pars = div.find_all('p')
    
            for p in pars:
                t = super().clean_paragraph(p)
                text += t + ' '
                # text += p.text

#            print (text)

        return (text)

def run(): 
    URL = "https://www.theverge.com/rss/index.xml"
    s = TheVerge_Scraper(URL)
    s.get_items()
    items = s.cycle_items()
    
    print (items)

if __name__ == '__main__':
    run()


