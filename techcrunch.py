import urllib
from urllib.request import urlopen
import requests
from requests import get
from bs4 import BeautifulSoup
import re
from abstractscraper import AbstractScraper

class TechCrunch_Scraper(AbstractScraper):

    def get_items(self):
        super().get_items()

        links = super().parse_standard_rss(self.url)
        self.links = links

        print (links)

    def cycle_items(self):
        super().cycle_items()

        return self.links

    def get_item_text(self,url):
        super().get_item_text(url)

#        headers = super().set_headers()
#        results = requests.get(url.strip(), headers=headers)
#        
#        soup = BeautifulSoup(results.text, "html.parser")
#        outer = soup.find('div', id = 'article-body')
#
        text = ""
#        if outer:
#            pars = outer.find_all('p')
#    
#            for p in pars:
#                t = super().clean_paragraph(p)
#                text += p.text

        return (text)

def run(): 
    URL = "https://techcrunch.com/feed/"
    s = TechCrunch_Scraper(URL)
    s.get_items()
    items = s.cycle_items()
    
    print (items)

if __name__ == '__main__':
    run()


