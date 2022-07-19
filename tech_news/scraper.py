import time
import requests


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
    """Seu código deve vir aqui"""


# Requisito 3
def scrape_next_page_link(html_content):
    """Seu código deve vir aqui"""


# Requisito 4
def scrape_noticia(html_content):
    """Seu código deve vir aqui"""


# Requisito 5
def get_tech_news(amount):
    """Seu código deve vir aqui"""
