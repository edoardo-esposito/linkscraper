import urllib
from urllib.request import urlopen
import csv
from bs4 import BeautifulSoup, NavigableString
import hashlib
import sqlite3
from datetime import datetime
import re

DEBUG = True
JUST_ONE_LINK = True
class AbstractScraper(object):

    def __init__(self, url):
        self.url = url
        super().__init__()

    def set_headers(self):
        headers = {
                "User-Agent":"Mozilla/5.0 (Macintosh; Intel Mac OSX 10_14_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36",
                'Accept': 'application/xml;q=0.9, */*;q=0.8'
#                "Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8" 
                }

        return headers

    def get_items(self):
        if DEBUG:
            print ("Get links from [%s]" % self.url)

        pass

    def cycle_items(self):
#        if DEBUG:
#            print ("CYCLE ARTICLES")

        for l in self.links:
            text = self.get_item_text(l['url'])
            l['text'] = text.encode().decode('utf-8')

        return self.links

    def get_item_text(self,url):
        if DEBUG:
            print ("Get text from article [%s]" % url.encode())

        pass

    def generate_link_id(self, titolo):
        link_id = hashlib.md5(titolo.encode('utf-8')).hexdigest()
        return link_id

    def parse_standard_rss(self, url):
        headers = self.set_headers()

        req = urllib.request.Request(self.url, headers = headers)
        parse_xml_url = urllib.request.urlopen(req)

        xml_page = parse_xml_url.read()
        parse_xml_url.close()

        soup_page = BeautifulSoup(xml_page, "lxml")
        channel = soup_page.find("channel")
        news_list = channel.findAll("item")

        links = []
        for getfeed in news_list:
            titolo = getfeed.title.text
            link_id = self.generate_link_id(titolo)

            links.append({ 
                'id': link_id,
                'titolo': titolo,
                'url': getfeed.link.nextSibling.rstrip(),
                'data': getfeed.pubdate.text
            })

            if JUST_ONE_LINK:
                break

        return links

    def parse_atom_rss(self, url):
        headers = self.set_headers()

        req = urllib.request.Request(self.url, headers = headers)
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
#        soup = BeautifulSoup(html, "html.parser")
    
        for tag in soup.findAll(True):
            if tag.name in valid_tags:
                print ('-----')
                print (tag.name)
                print (tag.contents)
                for t in tag.contents:

                    self.strip_tags(t, valid_tags)

                print ('-----\n')

#                for t in tag.contents:
#                     print ('-----')
#                     print (t.name)
#                     print (t.contents)
#                     print ('-----\n')
##                    if t.name in valid_tags:
##                        print ('-----')
##                        print (type(t))
##                        print (t.contents)
##                        print ('-----\n')
#
#
##                s = ""
##    
##                for c in tag.contents:
##                    if not isinstance(c, NavigableString):
##                        c = self.strip_tags(c, invalid_tags)
##                    s += str(c)
##    
##                tag.replaceWith(s)
    
        return soup
    
    def clean_text(self, taggedtext):
#        if DEBUG:
#            print ("Clean text [%s]" % taggedtext)

#        allowed_tags = ['h2', 'p']
#
#        text = ''
#        for tag in taggedtext.find_all(allowed_tags):
#            t = tag.extract()
#            text += str(t)
#
#        btext = BeautifulSoup(text, "html.parser")
#
#        if len(btext.find_all('script')) > 0:
#            btext.script.decompose()
#
#        for tag in btext:
#            for attribute in ['class', 'id', 'name', 'style', 'lang']:
#                del tag[attribute]

        

#        print ("Lunghezza normale %d" % len(taggedtext.text))
#        valid_tags = ['h2', 'p']
#        strippedtext = self.strip_tags(taggedtext, valid_tags)
#        print ("Lunghezza strippato %d" % len(strippedtext.text))

        btext = taggedtext.text

        return btext

    def clean_paragraph(self, paragraph):
#        if DEBUG:
#            print ("Clean paragraph [%s]" % paragraph)

        cleantext = paragraph.text
        cleantext = cleantext.replace(r'\n','')
        cleantext = cleantext.replace(r'\r','')
        cleantext = re.sub(r'[^A-Za-z0-9\s]+','', str(cleantext))
        cleantext = cleantext.strip()

#        if DEBUG:
#            print ("Cleaned [%s]" % cleantext)

        return cleantext

    def WIP_clean_text(self, taggedtext):
        if DEBUG:
            print ("Clean text [%s]" % taggedtext)
        

#        btext = taggedtext.text

        allowed_tags = ['h2', 'p']
        disallowed_tags = ['class', 'id', 'name', 'style', 'lang', 'span']
        text = ''

#        for tag in taggedtext.find_all(disallowed_tags):
        for tag in taggedtext.find_all(allowed_tags):
            print ("AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA")
            print (tag)
            print ("BBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBB")
#            t = tag.extract()
#            text += str(t)

#        print ("AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA ------")
#        print (text)
#
#        btext = BeautifulSoup(text, "html.parser")
#
#        if len(btext.find_all('script')) > 0:
#            btext.script.decompose()
#
#        for tag in btext:
#            for attribute in ['class', 'id', 'name', 'style', 'lang', 'span']:
#                del tag[attribute]
#        
        cleantext = taggedtext.text
#        cleantext = cleantext.replace(r'\n','')
#        cleantext = cleantext.replace(r'\r','')
#        cleantext = re.sub(r'[^A-Za-z0-9\s]+','', str(cleantext))
#
#        print ("BBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBB ------")
#        print (cleantext)

        return cleantext

    def find_items_in_csv(self, csv_file, word):
        try:
            with open('articoli.csv') as csv_file:
                csv_reader = csv.reader(csv_file, delimiter=';')
                line_count = 0
    
                for row in csv_reader:
                    if row[0] == word:
                        return True
        except IOError:
            print("File non presente")

        return False

    def items_to_csv(self):
        if DEBUG:
            print ("Print to CSV")

        csv_file = "articoli.csv"
        csv_columns = ['id','titolo','url','data','text']

        rows =[]
        for data in self.links:

            if self.find_items_in_csv(csv_file, data['id']):
                if DEBUG:
                    print ("Elemento con %s già esistente" % data['id'])
                continue

            row = {}
            row['id'] = data['id']
            row['titolo'] = data['titolo']
            row['url'] = data['url'].rstrip()
            row['data'] = data['data']
            row['text'] = data['text']
#            row['text'] = data['text'][0:100].decode('UTF-8')
#           date_obj = datetime.strptime(data['data'], '%a, %d %b %Y %H:%M:%S %Z')
#           print (date_obj)
            
            rows.append(row)
#            print (rows)

        try:
            with open(csv_file, 'a') as csvfile:
                writer = csv.DictWriter(csvfile, fieldnames=csv_columns, delimiter=";", quoting=csv.QUOTE_ALL)

                for row in rows:
                    writer.writerow(row)

        except IOError:
            print("I/O error")

