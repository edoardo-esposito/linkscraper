# coding=utf8

import time, random
import requests
from bs4 import BeautifulSoup
import hashlib
from urllib.error import URLError
import os
import csv
import dateparser
from datetime import date
from logger import Logger

DEBUG = False
TEST = False
TO_CSV = True

min = 1
max = 2

######## UTILITY FUNCTIONS
def get_today_date():
    today = date.today()
    today.strftime("%Y-%m-%d")

    return str(today)

def generate_link_id(titolo):
    link_id = hashlib.md5(titolo.encode('utf-8')).hexdigest()
    return link_id

def set_headers():
    headers = {
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
        "Accept-Encoding": "gzip, deflate, br",
        "Accept-Language": "en-US,en;q=0.9",
        "Sec-Fetch-Mode": "navigate",
        "Sec-Fetch-Site": "none",
        "Upgrade-Insecure-Requests": "1",
        "User-Agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.79 Safari/537.36",
    }

    return headers

def delay():
    if TEST: return None

    min = 5
    max = 10
    t = random.uniform(min, max)

    # print("Delay %d" % t)
    time.sleep(t)
    return None

def clean_text(text):
    import re

    text = re.sub("\'", "", text)
    text = re.sub(r'[\'|"|#]', r'', text)
    text = re.sub(r'[)|(|\|/]', r' ', text)
    text = re.sub("[^a-zA-Z0-9,.!?]", " ", text)

    text = text.replace(r'\n', '')
    text = text.replace(r'\r', '')
    text = ' '.join(text.split())
    text = text.strip()

    return text

def parse_date(date):
    if DEBUG:
        logger.debug(str("Parsing input date %s" % date))

    d = dateparser.parse(date)

    if d:
        return d

    logger.err(str("Could not parse date %s" % date))
    return date

######## SCRAPER
def parse_page(url, params):
    links = []

    logger.info("Parsing url: " + url)

    base_url = params['base_url']
    article_selector = params['article_selector']
    title_selector = params['title_selector']
    link_selector = params['link_selector']

    if 'date_selector' in params:
        date_selector = params['date_selector']
    else:
        date_selector = None

    try:
        headers = set_headers()
        results = requests.get(url.strip(), headers=headers)

        soup = BeautifulSoup(results.text, "html.parser")
        articles = soup.select(article_selector)

        if articles:
            if DEBUG:
                logger.debug(str("Number of links in url: %d" % len(articles)))

            for article in articles:

                try:
                    title = article.select(title_selector)[0].text.strip()

                    if DEBUG:
                        logger.debug("Title: " + title)

                    link = article.select(link_selector)[0]['href']
                    if not link.startswith("http"):
                        link = base_url + link

                    if DEBUG:
                        logger.debug("Link: " + link)

                    date = ''
                    try:
                        if date_selector:
                            date = parse_date(article.select(date_selector)[0].text.strip())
                    except Exception as e1:
                        logger.err("Exception in parse_page > for loop > get date")

                    if DEBUG:
                        logger.debug("Date: " + str(date))

                    links.append({
                        'id': generate_link_id(title),
                        'titolo': title,
                        'text': '',
                        'url': link,
                        'data': date
                    })

                    if TEST:
                        break

                except Exception as e:
                    logger.err("Exception in parse_page > for loop")
                    # print("Exception in parse_page > for loop")
                    # print(e)

        delay()

    except Exception as e:
        # TODO write exception to log for analysis
        logger.err("Exception in parse_page")
        # print ("Exception in parse_page")
        # print(e)
        links = []

    return links

def get_items(url):

    if DEBUG:
        logger.debug(str("Get links from [%s]" % url))

    if isinstance(url, list):
        links = []

        for u in url:
            l = parse_page(u, params)
            links = links + l[:len(l)]
    else:
        links = parse_page(url, params)

    # delay()

    return links

def get_item_text(url):
    if DEBUG:
        logger.debug(str("Get text from article [%s]" % url.encode()))

    content_selector = params['content_selector']

    try:
        headers = set_headers()
        results = requests.get(url.strip(), headers=headers)

        soup = BeautifulSoup(results.text, "html.parser")
        content = soup.select(content_selector)

        text = clean_text(content[0].text)

    except Exception as e:
        # TODO write exception to log for analysis
        logger.err("Exception in get_item_text")
        # print ("Exception in get_item_text")
        # print (e)
        text = ''

    delay()
    return (text)

def get_item_date(self, url):
    if DEBUG:
        logger.debug(str("Get date from article [%s]" % url.encode()))

    content_date_selector = self.params['content_date_selector']

    try:
        headers = set_headers()
        results = requests.get(url.strip(), headers=headers)

        soup = BeautifulSoup(results.text, "html.parser")
        content = soup.select(content_date_selector)

        date = clean_text(content[0].text)

        if DEBUG:
            print("Date: \"%s\"" % date)

    except Exception as e:
        # TODO write exception to log for analysis
        print ("Exception in get_item_date")
        print (e)
        date = ''

    delay()
    return (date)

def get_data_from_links(links):

    for l in links:
        try:
            text = get_item_text(l['url'])
            l['text'] = text.encode().decode('utf-8')

            if not l['data']:
                data = get_item_date(l['url'])
                l['data'] = data.encode().decode('utf-8')
        except Exception as e:
            logger.err(str("Exception in get_data_from_links %s" % l['url']))
            # print ("Exception")
            # print (e)
            l['text'] = ''

    return links

def find_items_in_csv(filename, word):
    try:
        with open(filename) as csv_file:
            csv_reader = csv.reader(csv_file, delimiter=';')
            line_count = 0

            for row in csv_reader:
                if row[0] == word:
                    logger.warn(str("Row \"%s\" already present" % row[1]))
                    return True

    except IndexError:
        logger.err(str("Index Error in find_items_in_csv on %s" % filename))
        pass
    except IOError:
        logger.err(str("IOError in find_items_in_csv on %s" % filename))
        pass

    return False

def items_to_csv(links):
    if DEBUG:
        logger.debug("Printing to CSV")

    dirname = "output"
    # d = datetime.date.today().strftime("%Y-%m-%d_%H%M")

    d = get_today_date()
    # TODO add date to file
    filename = dirname + "\\" + d + "_" + sitename.replace(" ", "") + ".csv"

    if DEBUG:
        logger.debug("Filename: " + filename)

    if not os.path.exists(dirname):
        os.makedirs(dirname)

    csv_columns = ['id', 'titolo', 'url', 'data', 'text', 'source']

    rows = []
    for data in links:

        if find_items_in_csv(filename, data['id']):
            if DEBUG:
                logger.err(str("Elemento con %s già esistente" % data['id']))
            continue

        txt = ''
        if data['text']:
            txt = data['text']

        row = {'id': data['id'], 'titolo': data['titolo'],
               'url': data['url'].rstrip(),
               'data': data['data'], 'text': txt, 'source': sitename}

        rows.append(row)

    try:
        with open(filename, 'a', newline='') as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=csv_columns, delimiter=";", quoting=csv.QUOTE_ALL)

            for row in rows:
                try:
                    writer.writerow(row)
                except:
                    logger.err(str("Exception in items_to_csv on %s" % filename))
                    pass

    except IOError:
        logger.err(str("IOError in items_to_csv on %s" % filename))

############# SITE CONFIG
def getSingularityHubLinks(min, max):
    links = []
    for i in range(min, max):
        links.append("https://singularityhub.com/tag/artificial-intelligence/page/%d/" % i)
    for i in range(min, max):
        links.append("https://singularityhub.com/tag/blockchain/page/%d/" % i)
    # for i in range(min, max):
    #     links.append("https://singularityhub.com/tag/robotics/page/%d/" % i)
    # for i in range(min, max):
    #     links.append("https://singularityhub.com/tag/neuroscience/page/%d/" % i)
    # for i in range(min, max):
    #     links.append("https://singularityhub.com/tag/computing/page/%d/" % i)
    # for i in range(min, max):
    #     links.append("https://singularityhub.com/tag/biotechnology/page/%d/" % i)

    if DEBUG:
        return links[0]

    return links

config = {
    'sito': 'SingularityHub',
    'url': getSingularityHubLinks(min, max),
    'params': {
        "base_url": "https://singularityhub.com/",
        "article_selector": "#td-outer-wrap .td-ss-main-content .item-details",
        "title_selector": "h3.entry-title",
        "link_selector": "h3 > a",
        "date_selector": "div.td-module-meta-info > span.td-post-date > time",
        "content_selector": "div.td-container div.td-post-content"
    }
}

try:
    logger = Logger()

    sitename = config['sito']
    url = config['url']
    params = config['params']

    links = get_items(url)
    items = get_data_from_links(links)

    if TO_CSV:
        logger.info("Dumping articles to CSV")
        items_to_csv(items)

except URLError as e:
    logger.err(str("Error in [%s]" % s['sito']))
    pass
