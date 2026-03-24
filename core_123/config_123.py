#URL to scrape tires from.
BASE_URL_123 = "https://padangos123.lt/"


# Tires dimensions to scrape.
DIMENSION = "245-45-R18"


FILTER_PARAMS = {
    "dimension": DIMENSION,
    "brands": {
        # "michelin": 1,
        #"bridgestone": 2,
        # "continental": 3,
        # "dunlop": 4,
        # "pirelli": 5,
         "goodyear": 6,
         "hankook": 7,
    },
    "seasons": {
        "vasarinės": 4,
        # "universalios": 5,
        # "žieminės": 6,
    },
}
