from pydantic import BaseModel, field_validator


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

    @field_validator("remaining_quantity", mode="before")
    def parse_quantity(cls, v):
        quantity = str(v).split(" ")[1] if " " in str(v) else str(v)
        return int(quantity.replace("+", "").strip())

    @field_validator("price", mode="before")
    def parse_price(cls, v):
        return float(str(v).split("€")[0].replace(",", ".").strip())
