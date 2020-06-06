import urllib
from urllib.request import urlopen
import csv
from bs4 import BeautifulSoup
import hashlib
import re
import os
from utils import parse_date, generate_link_id, remove_special_chars

DEBUG = True
JUST_ONE_LINK = False


class AbstractScraper(object):

    def __init__(self, url, sitename, params=None):
        self.url = url
        self.sitename = sitename
        super().__init__()

    @staticmethod
    def set_headers():
        headers = {
            "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OSX 10_14_3) AppleWebKit/537.36 (KHTML, like Gecko) "
                          "Chrome/71.0.3578.98 Safari/537.36",
            'Accept': 'application/xml;q=0.9, */*;q=0.8'
        }

        return headers

    def get_items(self):
        if DEBUG:
            print("Get links from [%s]" % self.url)

        pass

    def cycle_items(self):
        print("%d links found" % len(self.links))

        for l in self.links:
            try:
                text = self.get_item_text(l['url'])
                l['text'] = text.encode().decode('utf-8')

                if not l['data']:
                    data = self.get_item_date(l['url'])
                    l['data'] = data.encode().decode('utf-8')
            except:
                l['text'] = ''

        return self.links

    def get_item_text(self, url):
        if DEBUG:
            print("Get text from article [%s]" % url.encode())

        pass

    def parse_standard_rss(self, url):
        headers = self.set_headers()

        req = urllib.request.Request(url, headers=headers)
        parse_xml_url = urllib.request.urlopen(req)

        xml_page = parse_xml_url.read()
        parse_xml_url.close()

        soup_page = BeautifulSoup(xml_page, "lxml")
        channel = soup_page.find("channel")
        news_list = channel.findAll("item")

        links = []
        for getfeed in news_list:
            titolo = getfeed.title.text

            description = ""
            if getfeed.description.text:
                description = getfeed.description.text

            link_id = generate_link_id(titolo)

            links.append({
                'id': link_id,
                'titolo': titolo,
                'text': description,
                'url': getfeed.link.nextSibling.rstrip(),
                'data': parse_date(getfeed.pubdate.text)
            })

            if JUST_ONE_LINK:
                break

        return links

    def parse_atom_rss(self, url):
        headers = self.set_headers()

        req = urllib.request.Request(self.url, headers=headers)
        parse_xml_url = urllib.request.urlopen(req)

        xml_page = parse_xml_url.read()
        parse_xml_url.close()

        soup_page = BeautifulSoup(xml_page, "lxml")
        news_list = soup_page.findAll("entry")

        links = []
        for getfeed in news_list:
            titolo = getfeed.title.text

            links.append({
                'id': hashlib.md5(titolo.encode('utf-8')).hexdigest(),
                'titolo': titolo,
                'url': getfeed.link['href'],
                'data': getfeed.published.text
            })

            if JUST_ONE_LINK:
                break

        return links

    def strip_tags(self, soup, valid_tags):
        for tag in soup.findAll(True):
            if tag.name in valid_tags:
                print('-----')
                print(tag.name)
                print(tag.contents)
                for t in tag.contents:
                    self.strip_tags(t, valid_tags)

                print('-----\n')

        return soup

    # def clean_text(self, taggedtext):
    #     btext = remove_special_chars(taggedtext.text)
    #     return btext

    def clean_text(self, text):
        import re

        # remove backslash-apostrophe
        text = re.sub("\'", "", text)
        # text = re.sub(r'[?|!|\'|"|#]', r'', text)
        # text = re.sub(r'[.|,|)|(|\|/]', r' ', text)
        text = re.sub(r'[\'|"|#]', r'', text)
        text = re.sub(r'[)|(|\|/]', r' ', text)

        # remove everything except alphabets
        # text = re.sub("[^a-zA-Z]", " ", text)
        text = re.sub("[^a-zA-Z0-9,.!?]", " ", text)

        text = text.replace("\n", " ")

        # remove whitespaces
        text = ' '.join(text.split())

        return text

    def clean_paragraph(self, paragraph):

        for s in paragraph.select('script'):
            s.extract()

        cleaned = remove_special_chars(paragraph.text)

        # cleaned = cleaned.replace(r'\n', '')
        # cleaned = cleaned.replace(r'\r', '')
        # cleaned = re.sub(r'[^A-Za-z0-9\s]+', '', str(cleaned))
        # cleaned = cleaned.strip()

        return cleaned

    def find_items_in_csv(self, filename, word):
        try:
            with open(filename) as csv_file:
                csv_reader = csv.reader(csv_file, delimiter=';')
                line_count = 0

                for row in csv_reader:
                    if row[0] == word:
                        return True

        except IndexError:
            pass
        except IOError:
            pass
            # print("File non presente")

        return False

    def var_to_file(self, var):
        with open("output1.html", "w") as file:
            file.write(str(var))

    def items_to_csv(self):
        if DEBUG:
            print("Print to CSV")

        dirname = "output"
        # TODO add date to file
        filename = dirname + "\\" + self.sitename.replace(" ", "") + ".csv"

        if not os.path.exists(dirname):
            os.makedirs(dirname)

        csv_columns = ['id', 'titolo', 'url', 'data', 'text']

        rows = []
        for data in self.links:

            if self.find_items_in_csv(filename, data['id']):
                if DEBUG:
                    print("Elemento con %s già esistente" % data['id'])
                continue

            txt = ''
            if data['text']:
                txt = data['text']

            row = {'id': data['id'], 'titolo': data['titolo'],
                   'url': data['url'].rstrip(),
                   'data': data['data'], 'text': txt}

            rows.append(row)

        try:
            with open(filename, 'w', newline='') as csvfile:
                writer = csv.DictWriter(csvfile, fieldnames=csv_columns, delimiter=";", quoting=csv.QUOTE_ALL)

                for row in rows:
                    try:
                        writer.writerow(row)
                    except:
                        pass

        except IOError:
            print("I/O error")
