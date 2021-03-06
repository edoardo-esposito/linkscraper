# coding=utf8
from config import TEST, TO_CSV, min, max
from scraper import get_items,  get_data_from_links, items_to_csv, scrape_site


def getSingularityHubLinks(min, max):
    links = []
    for i in range(min, max):
        links.append("https://singularityhub.com/tag/artificial-intelligence/page/%d/" % i)

    if TEST:
        return links[0]

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
    for i in range(min, max):
        links.append("https://singularityhub.com/tag/virtual-reality/page/%d/" % i)
    for i in range(min, max):
        links.append("https://singularityhub.com/tag/3d-printing/page/%d/" % i)
    for i in range(min, max):
        links.append("https://singularityhub.com/tag/augmented-reality/page/%d/" % i)
    for i in range(min, max):
        links.append("https://singularityhub.com/tag/automation/page/%d/" % i)
    for i in range(min, max):
        links.append("https://singularityhub.com/tag/brain-computer-interface/page/%d/" % i)
    for i in range(min, max):
        links.append("https://singularityhub.com/tag/energy/page/%d/" % i)
    for i in range(min, max):
        links.append("https://singularityhub.com/tag/environment/page/%d/" % i)
    for i in range(min, max):
        links.append("https://singularityhub.com/tag/innovation/page/%d/" % i)
    for i in range(min, max):
        links.append("https://singularityhub.com/tag/internet-of-things/page/%d/" % i)

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

scrape_site(config)
