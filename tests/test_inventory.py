from inventory import inventory


def test_inventory_is_a_list():
    assert isinstance(inventory, list)


def test_inventory_items_have_required_fields():
    required_fields = [
        "id",
        "product_name",
        "brands",
        "barcode",
        "ingredients_text",
        "price",
        "stock"
    ]

    for item in inventory:
        for field in required_fields:
            assert field in item