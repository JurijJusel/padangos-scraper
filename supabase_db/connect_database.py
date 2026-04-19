import os
from supabase import create_client
from dotenv import load_dotenv


def get_supabase_client():
    """
    Create a Supabase client using environment variables.
    Returns:
        Client: A Supabase client instance.
    """
    load_dotenv()

    url = os.getenv("SUPABASE_URL_PADANGOS")
    key = os.getenv("SUPABASE_API_KEY_PADANGOS")

    client = create_client(url, key)
    return client


def insert_to_supabase_tire_if_not_exists(client, tire):
    """
    Insert tire data into Supabase if it does not already exist.
    Checks technical_info table by product_code before inserting.
    If found, skips insert. Otherwise inserts into tires_base
    and technical_info tables.
    Args:
        client: Supabase client instance.
        tire (dict): Flat dictionary containing tire and technical info fields.
    """
    product_code = tire["product_code"]

    existing = (
        client.table("technical_info")
        .select("tires_id")
        .eq("product_code", product_code)
        .execute()
    )

    if existing.data:
        print(f"Data exist in supabase, product_code: {product_code}")
        return None

    base = (
        client.table("tires_base")
        .insert(
            {
                "brand": tire["brand"],
                "model": tire["model"],
                "product_class": tire["product_class"],
                "price": tire["price"],
                "wet_grip": tire["wet_grip"],
                "fuel_effect": tire["fuel_effect"],
                "noise": tire["noise"],
                "remaining_quantity": tire["remaining_quantity"],
                "url": tire["url"],
            }
        )
        .execute()
    )

    tire_id = base.data[0]["id"]

    client.table("technical_info").insert(
        {
            "tires_id": tire_id,
            "width": tire["width"],
            "height": tire["height"],
            "diameter": tire["diameter"],
            "product_code": product_code,
            "product_season": tire["product_season"],
            "load_index": tire["load_index"],
            "speed_index": tire["speed_index"],
            "reinforced": tire["reinforced"],
            "runflat": tire["runflat"],
            "transport_type": tire["transport_type"],
            "construction_type": tire["construction_type"],
        }
    ).execute()

    print(f"Written data to supabase, product_code: {product_code}")


def get_cheapest_tires(client, limit: int = 5):
    """
    Get cheapest tires from Supabase with name, dimensions, price and url.

    Args:
        client: Supabase client instance.
        limit (int): Number of tires to return. Default is 5.

    Returns:
        list: List of cheapest tires with name, dimensions, price and url.
    """
    response = (
        client.table("tires_base")
        .select(
            "brand, model, price, url, "
            "technical_info(width, height, diameter)"
        )
        .order("price", desc=False)
        .limit(limit)
        .execute()
    )

    return response.data


def get_expensive_tires(client, limit: int = 5):
    """
    Get expensive tires from Supabase with name, dimensions, price and url.

    Args:
        client: Supabase client instance.
        limit (int): Number of tires to return. Default is 5.

    Returns:
        list: List of expensive tires with name, dimensions, price and url.
    """
    response = (
        client.table("tires_base")
        .select(
            "brand, model, price, url, "
            "technical_info(width, height, diameter)"
        )
        .order("price", desc=True)
        .limit(limit)
        .execute()
    )

    return response.data
