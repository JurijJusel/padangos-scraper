from pydantic import BaseModel
from datetime import datetime


class ScrapeInfo(BaseModel):
    base_url: str
    total_products: int
    scraped_at: str = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
