import re
from tech_news.database import search_news


# Requisito 6
def search_by_title(title: str):
    noticies = search_news({"title": re.compile(title, re.IGNORECASE)})
    tuple_news = [(notice["title"], notice["url"]) for notice in noticies]

    return tuple_news


# Requisito 7
def search_by_date(date):
    year, month, day = date.split("-")
    if len(year) < 4 or int(year) < 2021:
        raise ValueError("Data inválida")

    date_formated = f"{day}/{month}/{year}"
    noticies = search_news({"timestamp": date_formated})
    tuple_news = [(notice["title"], notice["url"]) for notice in noticies]

    return tuple_news


# Requisito 8
def search_by_tag(tag):
    noticies = search_news({"tags": re.compile(tag, re.IGNORECASE)})
    tuple_news = [(notice["title"], notice["url"]) for notice in noticies]

    return tuple_news


# Requisito 9
def search_by_category(category):
    noticies = search_news({"category": re.compile(category, re.IGNORECASE)})
    tuple_news = [(notice["title"], notice["url"]) for notice in noticies]

    return tuple_news