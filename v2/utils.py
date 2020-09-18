# coding=utf8
import dateparser
from datetime import date
import time, random
import hashlib

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
