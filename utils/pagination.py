def is_last_page(soup) -> bool:
    """
    Checks if the current page is the last page.
    Args:
        soup (BeautifulSoup): Parsed HTML content of the page.
    Returns:
        bool: True if the current page is the last page, False otherwise.
    """
    pagination = soup.find("ul", class_="pagination")
    last_li = pagination.find_all("li")[-1]
    return bool(last_li.find("span"))
