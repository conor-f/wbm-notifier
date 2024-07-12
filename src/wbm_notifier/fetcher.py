import requests
from bs4 import BeautifulSoup


def fetch_webpage(url):
    response = requests.get(url)
    response.raise_for_status()
    return response.text


def parse_webpage(content):
    soup = BeautifulSoup(content, "html.parser")
    entries = []
    for div in soup.find_all("div", class_="textWrap"):
        entry = {}
        try:
            entry["area"] = div.find("div", class_="area").text.strip()
            entry["address"] = div.find("div", class_="address").text.strip()
            entry["price"] = div.find("div", class_="main-property-rent").text.strip()
            entry["size"] = div.find("div", class_="main-property-size").text.strip()
            entry["rooms"] = div.find("div", class_="main-property-rooms").text.strip()
            entry["features"] = div.find(
                "ul", class_="check-property-list"
            ).text.strip()
            entry["link"] = div.find("a")["href"]
            entries.append(entry)
        except AttributeError:
            continue
    return entries
