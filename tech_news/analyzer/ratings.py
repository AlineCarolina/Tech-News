# Requisito 10
from tech_news.database import db


def top_5_news():
    top_noticias = db.news.find().sort("comments_count", -1).limit(5)
    list = []
    for item in top_noticias:
        list.append((item["title"], item["url"]))
    return list


# Requisito 11
def top_5_categories():
    """Seu código deve vir aqui"""
