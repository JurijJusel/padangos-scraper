from rich import print
from constants import BASE_URL_123, PREMIUM_TIRES_BRANDS, SEASONS, DIMENSION
from utils.url_builder import build_full_url_123
from crawlers.scrap_tires_123 import get_all_pages_and_products_links_123, scrape_product_123
from utils.file import write_data_to_json_file
from constants import JSON_FILE_PATH_123
from utils.http_get_soup import get_soup


def main():
    base_url = build_full_url_123(BASE_URL_123, DIMENSION, PREMIUM_TIRES_BRANDS, SEASONS)
    print(f"Scraping BASE_URL: {base_url}")

    product_urls_list = get_all_pages_and_products_links_123(base_url)
    print(f"Found {len(product_urls_list)} product URLs to scrape.")

    for product_url in product_urls_list[:10]:  # Limit to first 5 products
        print(f"Scraping product url: {product_url}")
        product_soup = get_soup(product_url)
        product = scrape_product_123(product_soup, product_url)
        print(write_data_to_json_file(product.model_dump(), JSON_FILE_PATH_123))


if __name__ == "__main__":
    main()
    print("DONE!")
