def build_filter_123(seasons: dict, brands: dict,
                    features: dict = {}, tire_selections: dict = {}) -> str:
    """
    Builds a filter string for the URL.
    tire_selections is only included if winter season (6) is in seasons.
    Args:
        seasons (dict): A dictionary of seasons and their filter values.
            Example: {"vasarinės": 4, "žieminės": 6}
        brands (dict): A dictionary of tire brands and their filter values.
            Example: {"bridgestone": 2, "michelin": 1}
        features (dict): A dictionary of features and their filter values.
            Example: {"runflat": "runflat", "reinforced": "reinforced"}
        tire_selections (dict): A dictionary of tire selections and their filter values.
            Only included in URL if winter season (6) is in seasons.
            Example: {"studded": "studded", "soft_mixture": "soft_mixture"}
    Returns:
        str: Filter string for the URL.
            Example: "?filter=features:runflat;tire_selections:studded;fmod_2:6;brands:2"
    """
    parts = []

    if features:
        feature_ids = ",".join(str(f) for f in features.values())
        parts.append(f"features:{feature_ids}")

    if tire_selections and 6 in seasons.values():
        selection_ids = ",".join(str(s) for s in tire_selections.values())
        parts.append(f"tire_selections:{selection_ids}")

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
            Example: "https://padangos123.lt/"
        filter_params (dict): A dictionary containing all filter parameters.
            Keys:
                "dimension" (str): Tire dimension. Example: "245-45-R18"
                "brands" (dict): Tire brands. Example: {"bridgestone": 2}
                "seasons" (dict): Seasons. Example: {"žieminės": 6}
                "features" (dict): Optional. Example: {"runflat": "runflat"}
                "tire_selections" (dict): Optional, only for winter. Example: {"studded": "studded"}
    Returns:
        str: The full URL constructed from the base URL and filter parameters.
            Example: "https://padangos123.lt/padangos/245-45-R18/?filter=fmod_2:6;brands:2"
    """
    filter_str = build_filter_123(
        seasons=filter_params["seasons"],
        brands=filter_params["brands"],
        features=filter_params.get("features", {}),
        tire_selections=filter_params.get("tire_selections", {}),
    )
    return f"{base_url}padangos/{filter_params['dimension']}/{filter_str}"
