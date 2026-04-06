def build_filter_123(seasons: dict, brands: dict) -> str:
    """
    Builds a filter string for the URL.
    Args:
        seasons (dict): A dictionary of seasons and their filter values.
            Example: {"vasarinės": 4, "žieminės": 6}
        brands (dict): A dictionary of tire brands and their filter values.
            Example: {"bridgestone": 2, "michelin": 1}
    Returns:
        str: Filter string for the URL.
            Example: "?filter=fmod_2:4;brands:2"
    """
    parts = []

    season_ids = ",".join(str(s) for s in seasons.values())
    parts.append(f"fmod_2:{season_ids}")

    brand_ids = ",".join(str(b) for b in brands.values())
    parts.append(f"brands:{brand_ids}")

    return "?filter=" + ";".join(parts)


def build_full_url_123(base_url: str, filter_params: dict) -> str:
    """
    Constructs the full URL for scraping.
    Args:
        base_url (str): The base URL of the website to scrape.
            Example: "https://padangosplius.lt/"
        filter_params (dict): A dictionary containing all filter parameters.
            Keys:
                "dimension" (str): Tire dimension. Example: "245-45-R18"
                "brands" (dict): Tire brands. Example: {"bridgestone": 2}
                "seasons" (dict): Seasons. Example: {"vasarinės": 4}
    Returns:
        str: The full URL.
            Example: "https://padangos123.lt/padangos/245-45-R18/?filter=fmod_2:4;brands:2"
    """
    filter_str = build_filter_123(
        seasons=filter_params["seasons"],
        brands=filter_params["brands"],
    )
    return f"{base_url}padangos/{filter_params['dimension']}/{filter_str}"
