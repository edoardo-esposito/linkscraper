from urllib.error import URLError

from scrapers.technologyreview_computing import TechnologyReview_Computing_Scraper
from scrapers.singularityhub import SingularityHub_Scraper
from scrapers.futurism import Futurism_Scraper
from scrapers.mckinseyinsights import MckinseyInsights_Scraper
from scrapers.venturebeat import VentureBeat_Scraper
from scrapers.wiredcom import WiredCom_Scraper
from scrapers.springwise import Springwise_Scraper
from scrapers.theverge import TheVerge_Scraper
from scrapers.engadget import Engadget_Scraper
from scrapers.watertechnology import WaterTechnology_Scraper
from scrapers.adweek import AdWeek_Scraper
from scrapers.therobotreport import TheRobotReport_Scraper
from scrapers.finextra import Finextra_Scraper
from scrapers.thetech import TheTech_Scraper
from scrapers.techxplore import TechXplore_Scraper
from scrapers.israel21c import Israel21c_Scraper
from scrapers.greenbiz import GreenBiz_Scraper
from scrapers.genericwebsite import GenericWebsite_Scraper

TOCSV = True
PRINT_ITEMS = False


def run():

    sources = [
        {
            'sito': 'CleanTechnica',
            'scraper': GenericWebsite_Scraper,
            'url': [
                'https://cleantechnica.com/category/clean-energy/',
                'https://cleantechnica.com/category/cleantechnica-2/cleantechnica-exclusive/cleantechnica-reviews/',
                'https://cleantechnica.com/category/energy-efficiency/'
             ],
            'params': {
                "base_url": "https://cleantechnica.com/",
                "article_selector": "section#omc-main > article",
                "title_selector": "div.omc-blog-two-text > h2",
                "link_selector": "h2 > a",
                "date_selector": "article > div.omc-blog-two-text > p.omc-blog-two-date",
                "content_selector": "#omc-full-article"
            }
        },
        # {
        #     'sito': 'IPI Singapore',
        #     'scraper': GenericWebsite_Scraper,
        #     'url': [
        #         # "https://www.ipi-singapore.org/success-stories",
        #         "https://www.ipi-singapore.org/innovation-insights?page=4",
        #         "https://www.ipi-singapore.org/news?page=4"
        #     ],
        #     'params': {
        #         "base_url": "https://www.ipi-singapore.org/",
        #         # "article_selector": "section > section > div > ul > li",
        #         "article_selector": "div.view-content > div.news-list-hld > div > ul > li",
        #         "title_selector": "h3",
        #         "link_selector": "span > a",
        #         "date_selector": "h4",
        #         "content_date_selector": "section > div > div.contant-hld > h4",
        #         "content_selector": "div.contant-hld > div"
        #     }
        # },
        # {
        #     'sito': 'GreenBiz',
        #     'scraper': GenericWebsite_Scraper,
        #     'url': [
        #         "https://www.greenbiz.com/collections/sustainability",
        #         "https://www.greenbiz.com/collections/food-systems",
        #         "https://www.greenbiz.com/collections/energy",
        #         "https://www.greenbiz.com/collections/transportation",
        #         "https://www.greenbiz.com/collections/circular-economy",
        #         "https://www.greenbiz.com/collections/cities"
        #     ],
        #     'params': {
        #         "base_url": "https://www.greenbiz.com/",
        #         "article_selector": "article > div.article-teaser-vertical__content",
        #         "title_selector": "h2 > a > span",
        #         "link_selector": "h2 > a",
        #         "date_selector": "p.article-teaser-vertical__date",
        #         "content_selector": "article > div > div.article-full__body.text-body > div.article__body"
        #     }
        # }
    ]

    for s in sources:
        print("Get articles from [%s]" % s['sito'])

        try:
            s = s['scraper'](s['url'], s['sito'], s['params'])
            s.get_items()
            items = s.cycle_items()

            if TOCSV:
                print("Dumping articles to CSV")
                s.items_to_csv()

            if PRINT_ITEMS:
                print(items)

        except URLError as e:
            print("Error in [%s]" % s['sito'])
            pass


# TODO: CSV output in own directory (in .gitignore)
# TODO: move all scrapers to own directory in order to load just one directory
def OLDrun():
    sources = [
        # {
        #     'sito': 'GreenBiz',
        #     'scraper': GreenBiz_Scraper,
        #     'url': [
        #         "https://www.greenbiz.com/collections/sustainability?page=5",
        #         "https://www.greenbiz.com/collections/food-systems?page=5",
        #         "https://www.greenbiz.com/collections/energy?page=5",
        #         "https://www.greenbiz.com/collections/transportation?page=5",
        #         "https://www.greenbiz.com/collections/circular-economy?page=5",
        #         "https://www.greenbiz.com/collections/cities?page=5"
        #     ]
        # },
        # {
        #     'sito': 'Technology Review Computing',
        #     'scraper': TechnologyReview_Computing_Scraper,
        #     'url': "https://www.technologyreview.com/c/computing/rss/"
        # },
        # {
        #     'sito': 'Water-Technology',
        #     'scraper': WaterTechnology_Scraper,
        #     'url': "https://www.water-technology.net/technology/"
        # },
        # {
        #     'sito': 'SingularityHub',
        #     'scraper': SingularityHub_Scraper,
        #     'url': "https://singularityhub.com/feed/"
        # },
        # {
        #     'sito': 'McKinsey Insights',
        #     'scraper': MckinseyInsights_Scraper,
        #     'url': "https://www.mckinsey.com/insights/rss.aspx"
        # },
        # {
        #     'sito': 'VentureBeat',
        #     'scraper': VentureBeat_Scraper,
        #     'url': "https://venturebeat.com/feed/"
        # },
        # {
        #     'sito': 'Wired.com',
        #     'scraper': WiredCom_Scraper,
        #     'url': "https://www.wired.com/feed/"
        # },
        # {
        #     'sito': 'Futurism',
        #     'scraper': Futurism_Scraper,
        #     'url': "https://feeder.co/discover/085f3bc023/futurism-com"
        # },
        # {
        #     'sito': 'Springwise',
        #     'scraper': Springwise_Scraper,
        #     'url': "https://www.springwise.com/feed/"
        # },
        # {
        #     'sito': 'The Verge',
        #     'scraper': TheVerge_Scraper,
        #     'url': "https://www.theverge.com/rss/index.xml"
        # },
        # {
        #     'sito': 'Engadget',
        #     'scraper': Engadget_Scraper,
        #     'url': "https://www.engadget.com/rss.xml"
        # },
        # {
        #     'sito': 'Adweek',
        #     'scraper': AdWeek_Scraper,
        #     'url': "https://www.adweek.com/feed/"
        # },
        # {
        #     'sito': 'The Robot Report',
        #     'scraper': TheRobotReport_Scraper,
        #     'url': "https://www.therobotreport.com/feed/",
        # },
        # {
        #     'sito': 'The Tech',
        #     'scraper': TheTech_Scraper,
        #     'url': "https://thetech.com/feed"
        # },
        # {
        #     'sito': 'Israel21c',
        #     'scraper': Israel21c_Scraper,
        #     'url': [
        #         "https://www.israel21c.org/topic/technology/",
        #         "https://www.israel21c.org/topic/health/",
        #         "https://www.israel21c.org/topic/environment/",
        #         "https://www.israel21c.org/topic/social-action/",
        #
        #     ]
        # },
        # {
        #     'sito': 'TechXplore',
        #     'scraper': TechXplore_Scraper,
        #     'url': [
        #         # "https://techxplore.com/rss-feed/breaking/automotive-news/",
        #         # "https://techxplore.com/rss-feed/breaking/computer-sciences-news/",
        #         "https://techxplore.com/rss-feed/breaking/energy-green-tech-news/",
        #         "https://techxplore.com/rss-feed/breaking/hi-tech-news/",
        #         "https://techxplore.com/rss-feed/breaking/machine-learning-ai-news/",
        #         "https://techxplore.com/rss-feed/breaking/robotics-news/",
        #         # "https://techxplore.com/rss-feed/breaking/security-news/"
        #     ]
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
