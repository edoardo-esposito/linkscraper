from scrapers.abstractscraper import AbstractScraper

class Dummy_Scraper(AbstractScraper):

    def get_items(self):
        super().get_items()

#        links = super().parse_standard_rss(self.url)

        links = []
        links.append({ 
            'titolo': 'Dummy title',
            'url': 'Dummy url',
            'data': 'Dummy date'
        })

        self.links = links

    def cycle_items(self):
        super().cycle_items()

        return self.links

    def get_item_text(self,url):
        super().get_item_text(url)

        text = ''
        return (text)

def run(): 
    URL = "dummy_url"
    s = Dummy_Scraper(URL)
    s.get_items()
    items = s.cycle_items()

    print (items)

if __name__ == '__main__':
    run()
