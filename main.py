import time
from rich import print
from rich.progress import track
from core_123.config_123 import (BASE_URL_123, FILTER_PARAMS)
from core_123.scrape_info import create_scrape_info
from core_123.url_builder_123 import build_full_url_123
from crawlers.scrap_tires_123 import (get_all_pages_and_products_links_123,
                                      scrape_product_123)
from utils.file import write_data_to_json_file, write_info_to_jsonl
from constants import JSON_FILE_PATH_123, JSONL_INFO_FILE_PATH_123
from utils.http_get_soup import get_soup


def main():
    base_url = build_full_url_123(BASE_URL_123, FILTER_PARAMS)
    print(f"Scraping BASE_URL: {base_url}")

    product_urls_list = get_all_pages_and_products_links_123(base_url)
    all_product_urls = len(product_urls_list)
    print(f"Found {all_product_urls} product URLs to scrape.")

    is_success = True

    for product_url in  track(product_urls_list, description="Scraping process..."):
        try:
            product_soup = get_soup(product_url)
            product = scrape_product_123(product_soup, product_url)
            print(write_data_to_json_file(product.model_dump(), JSON_FILE_PATH_123))
        except Exception as e:
            print(f"Error scraping {product_url}: {e}")
            is_success = False

        time.sleep(0.5)

    if is_success:
        scrape_info = create_scrape_info(base_url, all_product_urls)
        print(write_info_to_jsonl(scrape_info.model_dump(), JSONL_INFO_FILE_PATH_123))


if __name__ == "__main__":
    main()
    print("DONE!")
