from models.scrap_info_model import ScrapeInfo


def create_scrape_info(base_url: str, total_products: int) -> ScrapeInfo:
    """
    Creates a ScrapeInfo object with the current timestamp.
    Args:
        base_url (str): The base URL that was scraped.
        total_products (int): The total number of products scraped.
    Returns:
        ScrapeInfo: A ScrapeInfo object with the current timestamp.
    """
    return ScrapeInfo(
        base_url=base_url,
        total_products=total_products,
    )
