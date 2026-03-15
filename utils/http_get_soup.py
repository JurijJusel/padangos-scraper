import requests
from bs4 import BeautifulSoup


def get_soup(base_url):
    """
    Fetches and parses a webpage into a BeautifulSoup object.
    Args:
        page_url (str): The full URL of the page to fetch.
    Returns:
        BeautifulSoup: Parsed HTML content of the page.
    """
    req = requests.get(base_url, headers={"User-Agent":"Mozilla/5.0"})
    req.raise_for_status()
    soup = BeautifulSoup(req.text, "html.parser")
    return soup
