import pytest
from app import app


@pytest.fixture
def client():
    app.config["TESTING"] = True

    with app.test_client() as client:
        yield client


def test_get_inventory(client):
    response = client.get("/inventory")

    assert response.status_code == 200


def test_add_inventory_item(client):
    item = {
        "product_name": "Test Product",
        "brands": "Test Brand",
        "barcode": "123456789",
        "ingredients_text": "Test ingredients",
        "price": 100,
        "stock": 10
    }

    response = client.post("/inventory", json=item)

    assert response.status_code == 201
    assert response.get_json()["product_name"] == "Test Product"


def test_update_inventory_item(client):
    item = {
        "product_name": "Update Test",
        "brands": "Test Brand",
        "barcode": "987654321",
        "ingredients_text": "Test ingredients",
        "price": 50,
        "stock": 5
    }

    create_response = client.post("/inventory", json=item)
    item_id = create_response.get_json()["id"]

    response = client.patch(
        f"/inventory/{item_id}",
        json={"price": 75, "stock": 20}
    )

    assert response.status_code == 200
    assert response.get_json()["price"] == 75
    assert response.get_json()["stock"] == 20


def test_delete_inventory_item(client):
    item = {
        "product_name": "Delete Test",
        "brands": "Test Brand",
        "barcode": "111111111",
        "ingredients_text": "Test ingredients",
        "price": 30,
        "stock": 5
    }

    create_response = client.post("/inventory", json=item)
    item_id = create_response.get_json()["id"]

    response = client.delete(f"/inventory/{item_id}")

    assert response.status_code == 200