from urllib.error import URLError

from technologyreview_computing import TechnologyReview_Computing_Scraper
from singularityhub import SingularityHub_Scraper
from futurism import Futurism_Scraper
from mckinseyinsights import MckinseyInsights_Scraper
from venturebeat import VentureBeat_Scraper
from wiredcom import WiredCom_Scraper
from springwise import Springwise_Scraper
from theverge import TheVerge_Scraper
from engadget import Engadget_Scraper
from watertechnology import WaterTechnology_Scraper

TOCSV = True
PRINT_ITEMS = False


# TODO: CSV output in own directory (in .gitignore)
# TODO: move all scrapers to own directory in order to load just one directory


def run():
    sources = [
        # {
        #     'sito': 'Technology Review Computing',
        #     'scraper': TechnologyReview_Computing_Scraper,
        #     'url': "https://www.technologyreview.com/c/computing/rss/"
        # },
        {
            'sito': 'Water-Technology',
            'scraper': WaterTechnology_Scraper,
            'url': "https://www.water-technology.net/technology/"
        },
        {
            'sito': 'SingularityHub',
            'scraper': SingularityHub_Scraper,
            'url': "https://singularityhub.com/feed/"
        },
        # {
        #     'sito': 'McKinsey Insights',
        #     'scraper': MckinseyInsights_Scraper,
        #     'url': "https://www.mckinsey.com/insights/rss.aspx"
        # },
        {
            'sito': 'VentureBeat',
            'scraper': VentureBeat_Scraper,
            'url': "https://venturebeat.com/feed/"
        },
        # {
        #     'sito': 'Wired.com',
        #     'scraper': WiredCom_Scraper,
        #     'url': "https://www.wired.com/feed/"
        # },
        {
            'sito': 'Futurism',
            'scraper': Futurism_Scraper,
            'url': "https://feeder.co/discover/085f3bc023/futurism-com"
        },
        {
            'sito': 'Springwise',
            'scraper': Springwise_Scraper,
            'url': "https://www.springwise.com/feed/"
        },
        {
            'sito': 'The Verge',
            'scraper': TheVerge_Scraper,
            'url': "https://www.theverge.com/rss/index.xml"
        },
        # {
        #     'sito': 'Engadget',
        #     'scraper': Engadget_Scraper,
        #     'url': "https://www.engadget.com/rss.xml"
        # },
    ]

    errorlog = open("download.log", "a")
    for s in sources:
        print("Get articles from [%s]" % s['sito'])

        try:
            s = s['scraper'](s['url'], s['sito'])
            s.get_items()
            items = s.cycle_items()

            if TOCSV:
                print("Dumping articles to CSV")
                s.items_to_csv()

            if PRINT_ITEMS:
                print(items)

        except URLError as e:
            errorlog.write("URL Error in {0}: {1}\n".s['sito'], str(e))
            print("Error in [%s]" % s['sito'])
            pass


if __name__ == '__main__':
    run()
