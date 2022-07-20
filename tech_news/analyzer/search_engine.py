import re
from tech_news.database import search_news


# Requisito 6
def search_by_title(title: str):
    noticies = search_news({"title": re.compile(title, re.IGNORECASE)})
    tuple_news = [(notice["title"], notice["url"]) for notice in noticies]

    return tuple_news


# Requisito 7
def search_by_date(date):
    """Seu código deve vir aqui"""


# Requisito 8
def search_by_tag(tag):
    """Seu código deve vir aqui"""


# Requisito 9
def search_by_category(category):
    """Seu código deve vir aqui"""
