#URL to scrape tires from.
BASE_URL_123 = "https://padangos123.lt/"

# Tires dimensions to scrape.
DIMENSION = "245-45-R18"
#DIMENSION = "245-40-R19"

# Dictionary mapping tire brands.
PREMIUM_TIRES_BRANDS = {
    #"michelin": 1,
    #"bridgestone": 2,
    #"continental": 3,
    #"dunlop": 4,
    #"pirelli": 5,
    #"goodyear": 6,
    "hankook": 7,
}

# Dictionary mapping season names.
SEASONS = {
    "vasarinės": 4,
    #"universalios": 5,
    #"žieminės": 6,
}

# Dictionary mapping tire features.
FEATURES = {
    #"runflat": "runflat",
    "reinforced": "reinforced",
    "rim_protection": "rim_protection",
}

# Dictionary mapping tire selections.
TIRE_SELECTIONS = {
    "studded": "studded",
    # "soft_mixture": "soft_mixture",
    "medium_hardness": "medium_hardness",
    # "sporty": "sporty",
}
