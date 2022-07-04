import requests
import time
from parsel import Selector


# Requisito 1
def fetch(url):
    time.sleep(1)
    try:
        response = requests.get(
            url, headers={"user-agent": "Fake user-agent"}, timeout=3
        )
        if response.status_code != 200:
            return None
        else:
            return response.text
    except requests.Timeout:
        return None


# Requisito 2
def scrape_novidades(html_content):
    selector = Selector(html_content)
    return selector.css('.entry-title a::attr(href)').getall()


# Requisito 3
def scrape_next_page_link(html_content):
    try:
        selector = Selector(html_content)
        return selector.css('.nav-links a.next::attr(href)').get()
    except html_content.len == 0:
        return None


# Requisito 4
def scrape_noticia(html_content):
    """Seu código deve vir aqui"""


# Requisito 5
def get_tech_news(amount):
    """Seu código deve vir aqui"""
