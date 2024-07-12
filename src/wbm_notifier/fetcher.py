import requests
from bs4 import BeautifulSoup


def fetch_webpage(url):
    response = requests.get(url)
    response.raise_for_status()
    return response.text


def parse_webpage(content):
    soup = BeautifulSoup(content, "html.parser")
    return soup.get_text()
