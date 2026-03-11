import requests
from bs4 import BeautifulSoup
from constants import URL_123 as URL
from rich import print


def get_soup(page_url):
    """
    Fetches and parses a webpage into a BeautifulSoup object.
    Args:
        page_url (str): The full URL of the page to fetch.
    Returns:
        BeautifulSoup: Parsed HTML content of the page.
    """
    req = requests.get(page_url, headers={"User-Agent":"Mozilla/5.0"})
    print(req.status_code)
    req.raise_for_status()
    soup = BeautifulSoup(req.text, "html.parser")
    return soup


if __name__ == "__main__":
    url = URL
    soup  = get_soup(url)
    print(soup.title.text)
    #print(soup)
