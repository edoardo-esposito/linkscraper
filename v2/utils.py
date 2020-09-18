# coding=utf8
import dateparser
from datetime import date
import time, random
import hashlib
import math

from logger import Logger
from config import DEBUG, TEST, TO_CSV, min, max

logger = Logger()

def get_today_date():
    today = date.today()
    today.strftime("%Y-%m-%d")

    return str(today)

def generate_link_id(titolo):
    link_id = hashlib.md5(titolo.encode('utf-8')).hexdigest()
    return link_id

def set_headers():

    headers_list = [
        # Firefox 77 Mac
        {
            "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:77.0) Gecko/20100101 Firefox/77.0",
            "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
            "Accept-Language": "en-US,en;q=0.5",
            "Referer": "https://www.google.com/",
            "DNT": "1",
            "Connection": "keep-alive",
            "Upgrade-Insecure-Requests": "1"
        },
        # Firefox 77 Windows
        {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:77.0) Gecko/20100101 Firefox/77.0",
            "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
            "Accept-Language": "en-US,en;q=0.5",
            "Accept-Encoding": "gzip, deflate, br",
            "Referer": "https://www.google.com/",
            "DNT": "1",
            "Connection": "keep-alive",
            "Upgrade-Insecure-Requests": "1"
        },
        # Chrome 83 Mac
        {
            "Connection": "keep-alive",
            "DNT": "1",
            "Upgrade-Insecure-Requests": "1",
            "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.97 Safari/537.36",
            "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
            "Sec-Fetch-Site": "none",
            "Sec-Fetch-Mode": "navigate",
            "Sec-Fetch-Dest": "document",
            "Referer": "https://www.google.com/",
            "Accept-Encoding": "gzip, deflate, br",
            "Accept-Language": "en-GB,en-US;q=0.9,en;q=0.8"
        },
        # Chrome 83 Windows
        {
            "Connection": "keep-alive",
            "Upgrade-Insecure-Requests": "1",
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.97 Safari/537.36",
            "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
            "Sec-Fetch-Site": "same-origin",
            "Sec-Fetch-Mode": "navigate",
            "Sec-Fetch-User": "?1",
            "Sec-Fetch-Dest": "document",
            "Referer": "https://www.google.com/",
            "Accept-Encoding": "gzip, deflate, br",
            "Accept-Language": "en-US,en;q=0.9"
        }
    ]

    random_index = math.floor(random.uniform(1, len(headers_list)))
    return headers_list[random_index]

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
