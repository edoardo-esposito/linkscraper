import requests
from bs4 import BeautifulSoup
from scrapers.abstractscraper import AbstractScraper

class Engadget_Scraper(AbstractScraper):

    def get_items(self):
        super().get_items()

        links = super().parse_standard_rss(self.url)
        self.links = links

#        print (links)

    def cycle_items(self):
        super().cycle_items()

        return self.links

    def get_item_text(self,url):
        super().get_item_text(url)

        try:
            headers = super().set_headers()
            results = requests.get(url.strip(), headers=headers)
            soup = BeautifulSoup(results.text, "html.parser")
            div = soup.find('div', id = "engadget-post-contents")

            text = ""
            if div:
                pars = div.find_all('p')
    
                for p in pars:
                    t = super().clean_paragraph(p)
                    text += t + ' '
        except:
            # TODO write exception to log for analysis
            text = ''

#            print (text)

        return (text)

def run(): 
    URL = "https://www.engadget.com/rss.xml"
    s = Engadget_Scraper(URL)
    s.get_items()
    items = s.cycle_items()
    
    print (items)

if __name__ == '__main__':
    run()



