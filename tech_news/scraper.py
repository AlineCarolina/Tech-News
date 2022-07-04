import requests
import time
from parsel import Selector

from tech_news.database import create_news


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
    selector = Selector(html_content)

    data = {
        "url": selector.css("head link[rel=canonical]::attr(href)").get(),
        "title": selector.css(".entry-header-inner h1::text").get(),
        "timestamp": selector.css(".post-meta li::text").get(),
        "writer": selector.css(".post-meta a::text").get(),
        "comments_count": selector.css(".h5.title-block").get() or 0,
        "summary": selector.css(".entry-content").xpath("string(p)").get(),
        "tags": selector.css(".post-tags a::text").getall(),
        "category": selector.css("span.label::text").get(),
    }
    return data


# Requisito 5
def get_tech_news(amount):
    url = "https://blog.betrybe.com/"
    news = []
    while len(news) < amount:
        data = fetch(url)
        novidades = scrape_novidades(data)
        news.extend(scrape_noticia(
            fetch(new_url))for new_url in novidades
            if len(news) < amount
        )
        url = scrape_next_page_link(data)
    create_news(news)
    return news
