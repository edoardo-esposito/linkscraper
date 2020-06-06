from datetime import date
from datetime import datetime
import hashlib
import re
import xml.etree.ElementTree as ET


def get_today_date():
    today = date.today()
    today.strftime("%Y-%m-%d")

    return today


def parse_date(date):
    try:
        if re.compile(r'^[a-zA-Z]{3},').search(date):
            datetime_object = datetime.strptime(date, '%a, %d %b %Y')
            parsed_date = datetime_object.strftime("%Y-%m-%d")
        else:
            parsed_date = date
    except:
        parsed_date = date

    return parsed_date


def generate_link_id(titolo):
    link_id = hashlib.md5(titolo.encode('utf-8')).hexdigest()
    return link_id


def remove_special_chars(text):
    text = text.replace(r'\n', '')
    text = text.replace(r'\r', '')
    text = re.sub(r'[^A-Za-z0-9\s]+', '', str(text))
    text = ' '.join(text.split())
    text = text.strip()

    return text

