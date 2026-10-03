import requests


OPENFOODFACTS_URL =  "https://world.openfoodfacts.org"


def search_product_by_barcode(barcode):
    url = f"{OPENFOODFACTS_URL}/api/v2/product/{barcode}.json"
    headers = {
        "User-Agent": "InventoryManagementSystem/1.0"
    }

    response = requests.get(url, headers = headers)

    if response.status_code != 200:
        return None

    data = response.json()

    if data.get("status") != 1:
        return None

    product = data.get("product", {})

    return {
        "product_name": product.get("product_name", ""),
        "brands": product.get("brands", ""),
        "barcode": barcode,
        "ingredients_text": product.get("ingredients_text", "")
    }

