from unittest.mock import patch, Mock
import cli


@patch("cli.requests.get")
@patch("builtins.input", side_effect=["2", "", "8"])
def test_view_inventory(mock_input, mock_get):
    mock_response = Mock()
    mock_response.status_code = 200
    mock_response.json.return_value = [
        {
            "id": 1,
            "product_name": "Test Product",
            "brands": "Test Brand",
            "barcode": "123456",
            "ingredients_text": "Test ingredients",
            "price": 100,
            "stock": 10
        }
    ]

    mock_get.return_value = mock_response

    cli.main()

    mock_get.assert_called_once()


@patch("cli.requests.get")
@patch("cli.requests.delete")
@patch("builtins.input", side_effect=["5", "1", "y", "", "8"])
def test_delete_inventory_item(mock_input, mock_delete, mock_get):
    # Mock the GET request used to retrieve the item
    mock_get_response = Mock()
    mock_get_response.status_code = 200
    mock_get_response.json.return_value = {
        "id": 1,
        "product_name": "Test Product",
        "brands": "Test Brand",
        "barcode": "123456",
        "ingredients_text": "Test ingredients",
        "price": 100,
        "stock": 10
    }

    mock_get.return_value = mock_get_response

    # Mock the DELETE request
    mock_delete_response = Mock()
    mock_delete_response.status_code = 200
    mock_delete_response.json.return_value = {
        "message": "Item deleted successfully"
    }

    mock_delete.return_value = mock_delete_response

    cli.main()

    mock_get.assert_called_once()
    mock_delete.assert_called_once()