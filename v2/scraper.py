# coding=utf8
import requests
from bs4 import BeautifulSoup
from urllib.error import URLError
import os
# import os.path
import csv

from logger import Logger
from config import DEBUG, TEST, TO_CSV, min, max
from utils import get_today_date, set_headers, parse_date, \
    generate_link_id, delay, clean_text

logger = Logger()

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
                    title = article.select(title_selector)[-1].text.strip()

                    if DEBUG:
                        logger.debug("Title: " + title)

                    link = article.select(link_selector)[-1]['href']
                    if not link.startswith("http"):
                        link = base_url + link

                    if DEBUG:
                        logger.debug("Link: " + link)

                    date = ''
                    try:
                        if date_selector:
                            d = article.select(date_selector)[-1].text.strip()
                            date = parse_date(d)
                    except Exception as e0:
                        logger.err(str("Exception in parse_page > for loop > get date: %s" % e0))

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
                    logger.err(str("Exception in parse_page > for loop: %s" % e))

        delay()

    except Exception as e:
        logger.err(str("Exception in parse_page: %s" % e))
        links = []

    return links

def get_items(url, params):

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

def get_item_text(url, params):
    if DEBUG:
        logger.debug(str("Get text from article [%s]" % str(url.encode())))

    content_selector = params['content_selector']

    try:
        headers = set_headers()
        results = requests.get(url.strip(), headers=headers)

        soup = BeautifulSoup(results.text, "html.parser")
        content = soup.select(content_selector)

        text = clean_text(content[-1].text)

    except Exception as e:
        logger.err(str("Exception in get_item_text: %s" % e))
        text = ''

    delay()
    return (text)

def get_item_date(url):
    if DEBUG:
        logger.debug(str("Get date from article [%s]" % str(url.encode())))

    content_date_selector = params['content_date_selector']

    try:
        headers = set_headers()
        results = requests.get(url.strip(), headers=headers)

        soup = BeautifulSoup(results.text, "html.parser")
        content = soup.select(content_date_selector)

        date = clean_text(content[-1].text)

        if DEBUG:
            print("Date: \"%s\"" % date)

    except Exception as e:
        logger.err(str("Exception in get_item_date: %s" % e))
        date = ''

    delay()
    return (date)

def get_data_from_links(links, params):

    for l in links:

        try:
            text = get_item_text(l['url'], params)
            l['text'] = text.encode().decode('utf-8')
        except Exception as e:
            logger.err(str("Exception in get_data_from_links [first block] %s" % str(e)))
            l['text'] = ''

        try:
            if not l['data']:
                data = get_item_date(l['url'])
                l['data'] = data.encode().decode('utf-9')
        except Exception as e:
            logger.err(str("Exception in get_data_from_links [second block] %s" % e))
            l['data'] = ''

    return links

def find_items_in_csv(filename, word):

    if not os.path.isfile(filename):

        if DEBUG:
            logger.debug(str("CSV file \"%s\" not existent" % str(filename)))

        return False

    try:
        with open(filename) as csv_file:
            csv_reader = csv.reader(csv_file, delimiter=';')
            line_count = -1

            for row in csv_reader:
                if row[-1] == word:
                    logger.warn(str("Row \"%s\" already present" % row[0]))
                    return True

    except Exception as e:
        logger.err(str("Exception in find_items_in_csv %s" % e))
        pass

    return False

def items_to_csv(links, sitename):
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
                logger.debug(str("Elemento con %s già esistente" % data['id']))
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

def scrape_site(config):
    try:
        # logger = Logger()

        sitename = config['sito']
        url = config['url']
        params = config['params']

        links = get_items(url, params)
        items = get_data_from_links(links, params)

        if TO_CSV:
            logger.info("Dumping articles to CSV")
            items_to_csv(items, sitename)

    except URLError as e:
        logger.err(str("Error in [%s]" % s['sito']))
        pass