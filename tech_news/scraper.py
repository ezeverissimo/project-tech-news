from parsel import Selector
import time
import requests

from tech_news.database import create_news


# Requisito 1
def fetch(url):
    header = {"user-agent": "Fake user-agent"}

    try:
        time.sleep(1)
        response = requests.get(url, timeout=3, headers=header)
    except requests.ReadTimeout:
        return None
    else:
        if response.status_code != 200:
            return None
        return response.text


# Requisito 2
def scrape_novidades(html_content):
    selector = Selector(text=html_content)
    links: list = selector.css("a.cs-overlay-link::attr(href)").getall()

    return links


# Requisito 3
def scrape_next_page_link(html_content):
    selector = Selector(text=html_content)
    next_page = selector.css("a.next::attr(href)").get()

    return next_page


# Requisito 4
def scrape_noticia(html_content):
    selector = Selector(text=html_content)
    url = [
        link.attrib["href"]
        for link in selector.css("link")
        if link.attrib["rel"] == "canonical"
    ]

    title = selector.css("h1.entry-title::text").get()
    writer = selector.css("span.author a.url::text").get()
    timestamp = selector.css("li.meta-date::text").get()
    comments_count = len(selector.css("ol.comment-list li").getall())
    summary = "".join(selector.css("div.entry-content p:nth-child(2) *::text")
                      .getall())
    tags = selector.css("section.post-tags ul li a::text").getall()
    category = selector.css("a.category-style span.label::text").get()

    return {
        "url": url[0],
        "title": title,
        "timestamp": timestamp,
        "writer": writer,
        "comments_count": comments_count,
        "summary": summary,
        "tags": tags,
        "category": category,
    }


# Requisito 5
def get_tech_news(amount):
    html_page = fetch("https://blog.betrybe.com")
    noticies = scrape_novidades(html_page)
    tech_news = list()

    while True:
        for noticie_url in noticies[:amount]:
            html_noticie = fetch(noticie_url)
            tech_news.append(scrape_noticia(html_noticie))
            amount -= 1

        if amount < 1:
            break

        next_page = scrape_next_page_link(html_page)
        html_page = fetch(next_page)
        noticies = scrape_novidades(html_page)

    create_news(tech_news)
    return tech_news
