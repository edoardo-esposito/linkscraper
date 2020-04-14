import urllib
from urllib.request import urlopen
import requests
from requests import get
from bs4 import BeautifulSoup
import re
from abstractscraper import AbstractScraper

class Springwise_Scraper(AbstractScraper):

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

        headers = super().set_headers()
        results = requests.get(url.strip(), headers=headers)
        soup = BeautifulSoup(results.text, "html.parser")
        article = soup.find('article', class_="sw-article")
        div = soup.find('div', class_="sw-article__body")

        text = ""
        if div:
            pars = div.find_all('p')
    
            for p in pars:
                t = super().clean_paragraph(p)
                text += p.text

#            print (text)

        return (text)

def run(): 
    URL = "https://www.springwise.com/feed/"
    s = Springwise_Scraper(URL)
    s.get_items()
    items = s.cycle_items()
    
    print (items)

if __name__ == '__main__':
    run()

