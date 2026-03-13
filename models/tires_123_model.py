from pydantic import BaseModel


class TechnicalInfo(BaseModel):
    width: int
    height: int
    diameter: int
    product_code: str
    product_season: str
    load_index: int
    speed_index: str
    reinforced: str
    runflat: str
    transport_type: str
    construction_type: str


class Product(BaseModel):
    brand: str
    model: str
    product_class: str
    price: float
    wet_grip: str
    fuel_effect: str
    noise: str
    remaining_quantity: int
    technical_info: TechnicalInfo
    url: str
