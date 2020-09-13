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
# FATTI:
# The Verge, SingularityHub, CleanTechnica, IPI Singapore, The Spoon, Phys.Org, GreenBiz
# Springwise, Reuters
# DA FARE:
# Futurism, Mckinsey Insight, VentureBeat, Wired, Endgadget, WaterTechnology,
# AdWeek, The RobotReport, Israel21c, GreenBiz

def getReutersLinks(min, max):
    links = []
    for i in range(min, max):
        links.append("https://www.reuters.com/news/archive/technologynews?view=page&page=%d&pageSize=10" % i)

    return links

def getSingularityHubLinks(min, max):
    links = []
    for i in range(min, max):
        links.append("https://singularityhub.com/tag/artificial-intelligence/page/%d/" % i)
    for i in range(min, max):
        links.append("https://singularityhub.com/tag/blockchain/page/%d/" % i)
    for i in range(min, max):
        links.append("https://singularityhub.com/tag/robotics/page/%d/" % i)
    for i in range(min, max):
        links.append("https://singularityhub.com/tag/neuroscience/page/%d/" % i)
    for i in range(min, max):
        links.append("https://singularityhub.com/tag/computing/page/%d/" % i)
    for i in range(min, max):
        links.append("https://singularityhub.com/tag/biotechnology/page/%d/" % i)

    return links

def getIPILinks(min, max):
    links = []
    for i in range(min, max):
        links.append("https://www.ipi-singapore.org/news?page=%d" % i)
    for i in range(min, max):
        links.append("https://www.ipi-singapore.org/innovation-insights?page=%d" % i)

    return links

def getIsrael21cLinks(min, max):
    links = []
    for i in range(min, max):
        links.append("https://www.israel21c.org/topic/technology/page/%d/" % i)
    for i in range(min, max):
        links.append("https://www.israel21c.org/topic/health/page/%d/" % i)
    for i in range(min, max):
        links.append("https://www.israel21c.org/topic/environment/page/%d/" % i)

    return links

def getCleanTechnicaLinks(min, max):
    links = []
    for i in range(min, max):
        links.append("https://cleantechnica.com/category/clean-energy/page/%d/" % i)
    for i in range(min, max):
        links.append("https://cleantechnica.com/category/cleantechnica-2/cleantechnica-exclusive/cleantechnica-reviews/page/%d/" % i)
    for i in range(min, max):
        links.append("https://cleantechnica.com/category/energy-efficiency/page/%d/" % i)

    return links

def getTheSpoonLinks(min, max):
    links = []

    for i in range(min, max):
        links.append("https://thespoon.tech/category/topics/connected-kitchen/page/%d/" % i)
    for i in range(min, max):
        links.append("https://thespoon.tech/category/topics/robotics-ai/page/%d/" % i)
    for i in range(min, max):
        links.append("https://thespoon.tech/category/restaurant-tech/page/%d/" % i)
    for i in range(min, max):
        links.append("https://thespoon.tech/category/future-of-grocery/page/%d/" % i)
    for i in range(min, max):
        links.append("https://thespoon.tech/category/future-food/page/%d/" % i)
    for i in range(min, max):
        links.append("https://thespoon.tech/category/future-of-drink/page/%d/" % i)
    for i in range(min, max):
        links.append("https://thespoon.tech/category/food-waste/page/%d/" % i)
    for i in range(min, max):
        links.append("https://thespoon.tech/category/topics/foodtech/page/%d/" % i)
    for i in range(min, max):
        links.append("https://thespoon.tech/category/topics/food-tech-biz//page/%d/" % i)

    return links

def getTheVergeLinks(min, max):
    links = []

    for i in range(min, max):
        links.append("https://www.theverge.com/tech/archives/%d " % i)
    for i in range(min, max):
        links.append("https://www.theverge.com/energy/archives/%d" % i)
    for i in range(min, max):
        links.append("https://www.theverge.com/health/archives/%d" % i)

    return links

def getGreenBizLinks(min, max):
    links = []

    for i in range(min, max):
        links.append("https://www.greenbiz.com/collections/sustainability/page=%d " % i)
    for i in range(min, max):
        links.append("https://www.greenbiz.com/collections/food-systems/page=%d " % i)
    for i in range(min, max):
        links.append("https://www.greenbiz.com/collections/energy/page=%d " % i)
    for i in range(min, max):
        links.append("https://www.greenbiz.com/collections/transportation/page=%d " % i)
    for i in range(min, max):
        links.append("https://www.greenbiz.com/collections/circular-economy/page=%d " % i)
    for i in range(min, max):
        links.append("https://www.greenbiz.com/collections/cities/page=%d " % i)

    return links

def getWaterTechnologyLinks(min, max):
    links = []

    for i in range(min, max):
        links.append("https://www.water-technology.net/news/technology/page/%d/" % i)

    return links

def getVentureBeatLinks(min, max):
    links = []

    # for i in range(min, max):
    #     links.append("https://venturebeat.com/category/ai/page/%d/" % i)

    for i in range(min, max):
        links.append("https://venturebeat.com/category/arvr/page/%d/" % i)

    for i in range(min, max):
        links.append("https://venturebeat.com/category/cloud/page/%d/" % i)

    for i in range(min, max):
        links.append("https://venturebeat.com/category/big-data/page/%d/" % i)

    # for i in range(min, max):
    #     links.append("https://venturebeat.com/category/machine-learning/page/%d/" % i)
    #
    # for i in range(min, max):
    #     links.append("https://venturebeat.com/category/computer-vision/page/%d/" % i)
    #
    # for i in range(min, max):
    #     links.append("https://venturebeat.com/category/natural-language-processing/page/%d/" % i)
    #
    # for i in range(min, max):
    #     links.append("https://venturebeat.com/category/robotic-process-automation/page/%d/" % i)
    #
    # for i in range(min, max):
    #     links.append("https://venturebeat.com/category/entrepreneur/page/%d/" % i)
    #
    # for i in range(min, max):
    #     links.append("https://venturebeat.com/category/mobile/page/%d/" % i)
    #
    # for i in range(min, max):
    #     links.append("https://venturebeat.com/category/security/page/%d/" % i)
    #
    # for i in range(min, max):
    #     links.append("https://venturebeat.com/category/transportation/page/%d/" % i)

    return links

def getFoxNewsLinks():
    links = []
    links.append("https://www.foxnews.com/category/tech/topics/innovation")
    links.append("https://www.foxnews.com/category/tech/technologies/drones")
    links.append("https://www.foxnews.com/category/tech/topics/military-tech")

    return links

def getPysOrgLinks(min, max):
    links = []

    for i in range(min, max):
        links.append("https://phys.org/weekly-news/page%d.html" % i)

    # 'https://phys.org/space-news/',
    # "https://phys.org/nanotech-news/",
    # "https://phys.org/physics-news/",
    # 'https://phys.org/technology-news/'

    return links

def run():
    min = 1#40
    max = 2#60

    sources = [
        # {
        #     'sito': "DUMMY",
        #     'scraper': GenericWebsite_Scraper,
        #     'url': [
        #         "https://"
        #     ],
        #     'params': {
        #         "base_url": "https://",
        #         "article_selector": "",
        #         "title_selector": "",
        #         "link_selector": "",
        #         "date_selector": "",
        #         "content_date_selector": "",
        #         "content_selector": ""
        #     }
        # },
        {
            'sito': "TechnologyOrg",
            'scraper': GenericWebsite_Scraper,
            'url': [
                "https://www.technology.org/category/information-processing/ai-neural-networks/page/2/"
            ],
            'params': {
                "base_url": "https://www.technology.org",
                "article_selector": "div#technology-org-primary > ul.technology-org-list > li",
                "title_selector": "a",
                "link_selector": "a",
                "date_selector": "span.technology-org-time > span",
                "content_date_selector": "",
                "content_selector": "div#main div#technology-org-primary > div.entry-content"
            }
        },
        # {
        #     'sito': "Fox News",
        #     'scraper': GenericWebsite_Scraper,
        #     'url': getFoxNewsLinks(),
        #     'params': {
        #         "base_url": "https://foxnews.com",
        #         "article_selector": "section.collection > div.content > article",
        #         "title_selector": "header > h4",
        #         "link_selector": "header > h4 > a",
        #         "date_selector": "header > div.meta span",
        #         "content_date_selector": "",
        #         "content_selector": "article.article-wrap div.article-body"
        #     }
        # },
        # {
        #     'sito': "VentureBeat",
        #     'scraper': GenericWebsite_Scraper,
        #     'url': getVentureBeatLinks(min, max),
        #     'params': {
        #         "base_url": "https://venturebeat.com",
        #         "article_selector": "div#river > article",
        #         "title_selector": "header > h2",
        #         "link_selector": "header > h2 > a",
        #         "date_selector": "header > div.ArticleListing__byline > time",
        #         "content_date_selector": "",
        #         "content_selector": "div#content > article > div.article-content"
        #     }
        # },
        # {
        #     'sito': "WaterTechnology",
        #     'scraper': GenericWebsite_Scraper,
        #     'url': getWaterTechnologyLinks(min, max),
        #     'params': {
        #         "base_url": "https://www.water-technology.net/",
        #         "article_selector": "section > div.posts article",
        #         "title_selector": "h2",
        #         "link_selector": "h2 > a",
        #         "date_selector": "div.imgspace",
        #         "content_date_selector": "",
        #         "content_selector": "div#infinite-article div.post-content"
        #     }
        # },
        # {
        #     'sito': "Reuters",
        #     'scraper': GenericWebsite_Scraper,
        #     'url': getReutersLinks(min, max),
        #     'params': {
        #         "base_url": "https://www.reuters.com/",
        #         "article_selector": "div#content section.module-content article.story",
        #         "title_selector": "div.story-content > a > h3",
        #         "link_selector": "div.story-content > a",
        #         "date_selector": "div.story-content > time.article-time > span",
        #         "content_date_selector": "",
        #         "content_selector": "div.ArticlePage_container div.StandardArticleBody_body"
        #     }
        # },
        # {
        #     'sito': "Israel21c",
        #     'scraper': GenericWebsite_Scraper,
        #     'url': getIsrael21cLinks(min, max),
        #     'params': {
        #         "base_url": "https://www.israel21c.org/",
        #         "article_selector": "div#topics > section > article.item",
        #         "title_selector": "div.item-body > header > h1",
        #         "link_selector": "div.item-body > header > h1 > a",
        #         "date_selector": "div.item-body > div.date",
        #         "content_selector": "article div.article-body"
        #     }
        # },
        # {
        #     'sito': 'TheVerge',
        #     'scraper': GenericWebsite_Scraper,
        #     'url': getTheVergeLinks(min, max),
        #     'params': {
        #         "base_url": "https://www.theverge.com/",
        #         "article_selector": "#content div.l-col__main > div.c-compact-river > div.c-compact-river__entry",
        #         "title_selector": "div.c-entry-box--compact > div.c-entry-box--compact__body > h2.c-entry-box--compact__title",
        #         "link_selector": "div.c-entry-box--compact > div.c-entry-box--compact__body > h2.c-entry-box--compact__title > a",
        #         "content_date_selector": "time",
        #         "content_selector": "article.l-main-content > div.l-article-body-segment div.c-entry-content"
        #     }
        # },
        # {
        #     'sito': 'SingularityHub',
        #     'scraper': GenericWebsite_Scraper,
        #     'url': getSingularityHubLinks(min, max),
        #     'params': {
        #         "base_url": "https://singularityhub.com/",
        #         "article_selector": "#td-outer-wrap .td-ss-main-content .item-details",
        #         "title_selector": "h3.entry-title",
        #         "link_selector": "h3 > a",
        #         "date_selector": "div.td-module-meta-info > span.td-post-date > time",
        #         "content_selector": "div.td-container div.td-post-content"
        #     }
        # },
        # {
        #     'sito': 'CleanTechnica',
        #     'scraper': GenericWebsite_Scraper,
        #     'url': getCleanTechnicaLinks(min, max),
        #     'params': {
        #         "base_url": "https://cleantechnica.com/",
        #         "article_selector": "section#omc-main > article",
        #         "title_selector": "div.omc-blog-two-text > h2",
        #         "link_selector": "h2 > a",
        #         "date_selector": "article > div.omc-blog-two-text > p.omc-blog-two-date",
        #         "content_selector": "#omc-full-article"
        #     }
        # },
        # {
        #     'sito': 'IPI Singapore',
        #     'scraper': GenericWebsite_Scraper,
        #     'url': getIPILinks(min, max),
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
        #     'sito': 'TheSpoon',
        #     'scraper': GenericWebsite_Scraper,
        #     'url': getTheSpoonLinks(min, max),
        #     'params': {
        #         'base_url': "https://thespoon.tech/",
        #         'article_selector': 'div#article-wrap > article',
        #         'title_selector': 'header.entry-header > h2',
        #         'link_selector': 'header.entry-header > h2 > a',
        #         'date_selector': 'header.entry-header > p.entry-meta > time',
        #         'content_selector': 'div.entry-content > p'
        #     }
        # }
        # {
        #     'sito': "SpringWise",
        #     'scraper': GenericWebsite_Scraper,
        #     'url': [
        #         "https://www.springwise.com/sustainability-innovations/",
        #         "https://www.springwise.com/advertising-and-marketing-innovations/",
        #         "https://www.springwise.com/agriculture-energy-innovations/",
        #         "https://www.springwise.com/architecture-and-design-innovations/",
        #         "https://www.springwise.com/education-innovations/",
        #         "https://www.springwise.com/fashion-and-beauty-innovations/",
        #         "https://www.springwise.com/financial-services-innovations/",
        #         "https://www.springwise.com/food-and-drink-innovations/",
        #         "https://www.springwise.com/healthcare-and-wellbeing-innovations/",
        #         "https://www.springwise.com/mobility-and-transport-innovations/",
        #         "https://www.springwise.com/property-and-construction-innovations/",
        #         "https://www.springwise.com/retail-innovations/",
        #         "https://www.springwise.com/work-and-lifestyle-innovations/"
        #     ],
        #     'params': {
        #         "base_url": "https://www.springwise.com/",
        #         "article_selector": "article",
        #         "title_selector": "div.pp-post-grid__content > h3",
        #         "link_selector": "a",
        #         "date_selector": "time",
        #         "content_selector": "main.sw-content > article.sw-article > section.sw-article__content > div.sw-article__body"
        #     }
        # },
        # {
        #     'sito': 'Phys.Org',
        #     'scraper': GenericWebsite_Scraper,
        #     'url': getPysOrgLinks(min, max),
        #     'params': {
        #         "base_url": "https://phys.org/",
        #         "article_selector": ".sorted-news-list > article",
        #         "title_selector": "h3",
        #         "link_selector": "h3 > a",
        #         "content_date_selector": "article.news-article > div.article__info p",
        #         "content_selector": "article.news-article > div.article-main > p"
        #     }
        # },
        # {
        #     'sito': 'GreenBiz',
        #     'scraper': GenericWebsite_Scraper,
        #     'url': getGreenBizLinks(min, max),
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
# TODO: move all scrapers wto own directory in order to load just one directory
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
        {
            'sito': 'Technology Review Computing',
            'scraper': TechnologyReview_Computing_Scraper,
            'url': "https://www.technologyreview.com/c/computing/rss/"
        },
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
        {
            'sito': 'McKinsey Insights',
            'scraper': MckinseyInsights_Scraper,
            'url': "https://www.mckinsey.com/insights/rss.aspx"
        },
        {
            'sito': 'VentureBeat',
            'scraper': VentureBeat_Scraper,
            'url': "https://venturebeat.com/feed/"
        },
        {
            'sito': 'Wired.com',
            'scraper': WiredCom_Scraper,
            'url': "https://www.wired.com/feed/"
        },
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
        {
            'sito': 'Engadget',
            'scraper': Engadget_Scraper,
            'url': "https://www.engadget.com/rss.xml"
        },
        {
            'sito': 'Adweek',
            'scraper': AdWeek_Scraper,
            'url': "https://www.adweek.com/feed/"
        },
        {
            'sito': 'The Robot Report',
            'scraper': TheRobotReport_Scraper,
            'url': "https://www.therobotreport.com/feed/",
        },
        {
            'sito': 'The Tech',
            'scraper': TheTech_Scraper,
            'url': "https://thetech.com/feed"
        },
        {
            'sito': 'Israel21c',
            'scraper': Israel21c_Scraper,
            'url': [
                "https://www.israel21c.org/topic/technology/",
                "https://www.israel21c.org/topic/health/",
                "https://www.israel21c.org/topic/environment/",
                "https://www.israel21c.org/topic/social-action/",

            ]
        },
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
