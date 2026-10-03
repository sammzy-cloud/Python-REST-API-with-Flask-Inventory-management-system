from flask import Flask, jsonify, request
from inventory import inventory

app = Flask(__name__)

@app.route("/inventory", methods = ["GET"])
def get_inventory():
    return jsonify(inventory)

@app.route("/inventory/<int:item_id>", methods = ["GET"])
def get_item(item_id):
    for item in inventory:
        if item["id"] == item_id:
            return jsonify(item_id)
    return jsonify({"error message: Item not found"}), 404

@app.route("/inventory", methods = ["POST"])
def add_item():
    data = request.get_json() or {}
    product_name = data.get("product_name", "").strip()
    brands = data.get("brands", "").strip()
    barcode = data.get("barcode", "").strip()
    ingredients_text = ("ingredients_text", "").strip()
    price = data.get("price")
    stock = data.get("stock")

    if not product_name or not brands or not barcode or not ingredients_text or not price or not stock:
        return jsonify({"error: Product name , brands, barcode , ingredients text, price and stock are required"}), 400
    
    new_id = max([item["id"] for item in inventory], default=0) + 1

    new_item = {
        "id": new_id,
        "product_name": product_name,
        "brands": brands,
        "barcode": barcode,
        "ingredients_text": ingredients_text,
        "price": price,
        "stock": stock
    }

    inventory.append(new_item)

    return jsonify(new_item), 201

@app.route("/inventory/<int:item_id>", methods = ["PATCH"])
def update_item(item_id):
    data = request.get_json() or {}
    for item in inventory:
        if item["id"] == item_id:
            if "product_name" in data:
                item["product_name"] == data["product_name"].strip
            if "brands" in data:
                item["brands"] == data["brands"].strip
            if "barcode" in data:
                item["barcode"] == data["barcode"].strip
            if "ingredients_text" in data:
                item["ingredients_text"] == data["ingredients_text"].strip
            if "price" in data:
                item["price"] = data["price"]
            if "stock" in data:
                item["stock"] = data["stock"]

            return jsonify(item), 200

    return jsonify({"error": "Item not found"}), 404


@app.route("/inventory/<int:item_id>", methods=["DELETE"])
def delete_item(item_id):
    for item in inventory:
        if item["id"] == item_id:
            inventory.remove(item)
            return jsonify({"message": "Item deleted successfully"}), 200

    return jsonify({"error": "Item not found"}), 404

if __name__ == "__main__":
    app.run(debug=True)





        




