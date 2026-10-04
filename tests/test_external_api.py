from unittest.mock import patch, Mock
from api import search_product_by_barcode


@patch("api.requests.get")
def test_search_product_by_barcode(mock_get):
    mock_response = Mock()

    mock_response.status_code = 200

    mock_response.json.return_value = {
        "status": 1,
        "product": {
            "product_name": "Nutella",
            "brands": "Ferrero",
            "ingredients_text": "sugar, palm oil, hazelnuts"
        }
    }

    mock_get.return_value = mock_response

    result = search_product_by_barcode("3017624010701")

    assert result["product_name"] == "Nutella"
    assert result["brands"] == "Ferrero"
    assert result["barcode"] == "3017624010701"
    assert result["ingredients_text"] == "sugar, palm oil, hazelnuts"

    mock_get.assert_called_once()