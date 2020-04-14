import urllib
from urllib.request import urlopen
import requests
from requests import get
from bs4 import BeautifulSoup
import re
from abstractscraper import AbstractScraper

class SingularityHub_Scraper(AbstractScraper):

    def get_items(self):
        super().get_items()

        links = super().parse_standard_rss(self.url)
        self.links = links

    def cycle_items(self):
        super().cycle_items()

        return self.links

    def get_item_text(self,url):
        super().get_item_text(url)

        headers = super().set_headers()
        results = requests.get(url.strip(), headers=headers)
        
        soup = BeautifulSoup(results.text, "html.parser")
        outer = soup.find('div', id = 'td-outer-wrap')
        content_div = soup.find('div', class_='td-post-content')

        text = super().clean_text(content_div)

        return (text)

def run(): 
    URL = "https://singularityhub.com/feed/"
    s = SingularityHub_Scraper(URL)
    s.get_items()
    items = s.cycle_items()
    
    print (items)

if __name__ == '__main__':
    run()
