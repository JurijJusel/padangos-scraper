# URL to scrape tires from.

BASE_URL_123 = "https://padangos123.lt/"

BASE_URL_LYDERIS = "https://www.padangulyderis.lt/"

BASE_URL_MELGA = "https://melga.lt/"

BASE_URL_PLIUS = "https://padangosplius.lt/"

BASE_URL_PARDUOTUVE = "https://www.padanguparduotuve.lt/"

BASE_URL_VISOS = "https://www.visos-padangos.lt/"

BASE_URL_G = "https://www.gpadangos.lt/"


# Path to the JSON file where scraped data will be stored.
JSON_FILE_PATH_123 = "data/data_123.json"


# Dictionary mapping tire brands to their corresponding filter values used in the URL.
PREMIUM_TIRES_BRANDS = {
    "michelin": 1,
    "bridgestone": 2,
    "continental": 3,
    #"dunlop": 4,
    #"pirelli": 5,
    #"goodyear": 6,
}


# Dictionary mapping season names to their corresponding filter values used in the URL.
SEASONS = {
    "vasarinės": 4,
    #"universalios": 5,
    #"žieminės": 6,
}


# Tires dimensions to scrape.
DIMENSION = "245-45-R18"
