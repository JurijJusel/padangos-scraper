def build_filter_123(brands: dict, seasons: dict) -> str:
    """
    Builds a filter string for the URL.
    Args:
        brands (dict): A dictionary of tire brands and their filter values.
            Example: {"bridgestone": 2, "michelin": 1}
        seasons (dict): A dictionary of seasons and their filter values.
            Example: {"vasarinės": 4, "žieminės": 6}
    Returns:
        str: Filter string for the URL.
            Example: "?filter=fmod_2:4,6;brands:2,3"
    """
    brand_ids = ",".join(str(b) for b in brands.values())
    season_ids = ",".join(str(s) for s in seasons.values())
    return f"?filter=fmod_2:{season_ids};brands:{brand_ids}"


def build_full_url_123(base_url: str, dimension: str, brands: dict, seasons: dict) -> str:
    """
    Constructs the full URL for scraping.
    Args:
        base_url (str): The base URL of the website to scrape.
            Example: "https://padangos123.lt/"
        dimension (str): The tire dimension to filter by.
            Example: "245-45-R18"
        brands (dict): A dictionary of tire brands and their filter values.
            Example: {"bridgestone": 2, "michelin": 3}
        seasons (dict): A dictionary of seasons and their filter values.
            Example: {"vasarinės": 4, "žieminės": 6}
    Returns:
        str: The full URL constructed from the base URL, dimension, and filter.
            Example: "https://padangos123.lt/padangos/245-45-R18/?filter=fmod_2:4,6;brands:2,3"
    """
    filter_str = build_filter_123(brands, seasons)
    return f"{base_url}padangos/{dimension}/{filter_str}"
