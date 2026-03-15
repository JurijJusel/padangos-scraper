from models.tires_123_model import Product, TechnicalInfo
from utils.http_get_soup import get_soup
from utils.pagination import is_last_page


def get_product_links_123(soup) -> list[str]:
    """
    Scrapes all product links from a page.
    Args:
        soup (BeautifulSoup): Parsed HTML content of the page.
    Returns:
        list[str]: List of product URLs.
    """
    recommended = soup.find_all("div", class_="product_element mobile recommended")
    mobile = soup.find_all("div", class_="product_element mobile")
    all_items = recommended + mobile
    all_links = [item.find("a", class_="main_link")["href"] for item in all_items]
    return all_links


def get_all_pages_and_products_links_123(base_url: str) -> list[str]:
    """
    Generates a list of all product links across all pages.
    Stops when the next page arrow is a span (last page).
    Args:
        base_url (str): The base URL without page parameter.
            Example: "https://padangos123.lt/padangos/245-45-R18/?filter=fmod_2:4;brands:2"
    Returns:
        list[str]: List of product URLs.
    """
    links = []
    page = 1

    while True:
        url = f"{base_url}&page={page}"
        soup = get_soup(url)
        products = get_product_links_123(soup)
        links.extend(products)
        print(f"Page {page} — found {len(products)} products")

        if is_last_page(soup):
            print(f"Last page: {page}")
            break

        page += 1

    return links


def scrape_product_123(soup, url) -> Product:
    """
    Scrapes product data from a BeautifulSoup object.
    Args:
        soup (BeautifulSoup): Parsed HTML content of the page.
        url (str): The URL of the page.
    Returns:
        Product: Pydantic model with scraped data.
    """
    brand_tag = soup.find("span", itemprop="brand")
    brand = brand_tag.text
    model = brand_tag.next_sibling.strip()
    product_class = soup.find("div", class_="product_class").get_text(strip=True)
    price = soup.find("div", class_="current_price").get_text(strip=True)
    wet_grip = soup.find("img", alt="Sukibimas su šlapia kelio danga").find_next_sibling("span").text
    fuel_effect = soup.find("img", alt="Degalų sąnaudų efektyvumas").find_next_sibling("span").text
    noise = soup.find("img", alt="Išorinis triukšmas").find_next_sibling("span").text
    remaining_quantity = soup.find("div", class_="quantity").get_text(strip=True)

    tech = TechnicalInfo(
        product_code=soup.find("dt", string="Prekės kodas:").find_next_sibling("dd").get_text(strip=True),
        product_season=soup.find("dt", string="Tipas:").find_next_sibling("dd").get_text(strip=True),
        width=int(soup.find("dt", string="Plotis:").find_next_sibling("dd").get_text(strip=True)),
        height=int(soup.find("dt", string="Aukštis:").find_next_sibling("dd").get_text(strip=True)),
        diameter=int(soup.find("dt", string="Skersmuo:").find_next_sibling("dd").get_text(strip=True)),
        load_index=int(soup.find("dt", string="Apkrovos indeksas:").find_next_sibling("dd").get_text(strip=True)),
        speed_index=soup.find("dt", string="Greičio indeksas:").find_next_sibling("dd").get_text(strip=True),
        reinforced=soup.find("dt", string="Sustiprintos:").find_next_sibling("dd").get_text(strip=True),
        runflat=soup.find("dt", string="Runflat:").find_next_sibling("dd").get_text(strip=True),
        transport_type=soup.find("dt", string="Transporto tipas:").find_next_sibling("dd").get_text(strip=True),
        construction_type=soup.find("dt", string="Konstrukcijos tipas:").find_next_sibling("dd").get_text(strip=True),
    )

    return Product(
        url=url,
        brand=brand,
        model=model,
        product_class=product_class,
        price=price,
        wet_grip=wet_grip,
        fuel_effect=fuel_effect,
        noise=noise,
        remaining_quantity=remaining_quantity,
        technical_info=tech,
    )
