from tech_news.database import search_news
from datetime import datetime


# Requisito 6
def search_by_title(title):
    data = search_news({"title": {"$regex": title, "$options": "-i"}})
    titles = []
    for item in data:
        titles.append((item["title"], item["url"]))
    return titles


# Requisito 7
def search_by_date(date):
    MONTH = {
        "01": "janeiro",
        "02": "fevereiro",
        "03": "março",
        "04": "abril",
        "05": "maio",
        "06": "junho",
        "07": "julho",
        "08": "agosto",
        "09": "setembro",
        "10": "outubro",
        "11": "novembro",
        "12": "dezembro",
    }
    try:
        datetime.strptime(date, "%Y-%m-%d")
    except ValueError:
        raise ValueError("Data inválida")
    else:
        year, month, day = date.split("-")
        data_format = f"{int(day)} de {MONTH[month]} de {year}"
        noticias = search_news({"timestamp": data_format})
        list = []
        for noticia in noticias:
            list.append((noticia["title"], noticia["url"]))
        return list


# Requisito 8
def search_by_tag(tag):
    """Seu código deve vir aqui"""


# Requisito 9
def search_by_category(category):
    """Seu código deve vir aqui"""
