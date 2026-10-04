import requests
from inventory import inventory
from api import search_product_by_barcode

def show_menu():
    print("\n===== INVENTORY MANAGEMENT SYSTEM =====")
    print("1. Add inventory item")
    print("2. View all inventory")
    print("3. View one inventory item")
    print("4. Update inventory item")
    print("5. Delete inventory item")
    print("6. Find product on OpenFoodFacts")
    print("7. Import product from OpenFoodFacts")
    print("8. Exit")


def main():
    while True:
        show_menu()

        choice = input("Choose an option: ")

        if choice == "1":
            print("\n===== ADD INVENTORY ITEM =====")

            product_name = input("Product name: ")
            brands = input("Brand: ")
            barcode = input("Barcode: ")
            ingredients_text = input("Ingredients: ")

            try:
                price = float(input("Price: "))
                stock = int(input("Stock: "))
            except ValueError:
                print("Price must be a number and stock must be a whole number.")
                input("\nPress Enter to return to the menu...")
                continue

            new_item = {
                "product_name": product_name,
                "brands": brands,
                "barcode": barcode,
                "ingredients_text": ingredients_text,
                "price": price,
                "stock": stock
            }

            response = requests.post(
                "http://127.0.0.1:5000/inventory",
                json=new_item
            )

            if response.status_code in (200, 201):
                item = response.json()

                print("\nItem added successfully!")
                print(f"ID: {item['id']}")
                print(f"Product: {item['product_name']}")
                print(f"Price: {item['price']}")
                print(f"Stock: {item['stock']}")

            else:
                print("Unable to add item.")
                print(response.json())

            input("\nPress Enter to return to the menu...")

        elif choice == "2":
            response = requests.get("http://127.0.0.1:5000/inventory")

            if response.status_code == 200:
                items = response.json()

                if not items:
                    print("Inventory is empty.")
                else:
                    print("\n===== INVENTORY =====")

                    for item in items:
                        print(f"ID: {item['id']}")
                        print(f"Product: {item['product_name']}")
                        print(f"Brand: {item['brands']}")
                        print(f"Barcode: {item['barcode']}")
                        print(f"Price: {item['price']}")
                        print(f"Stock: {item['stock']}")
                        print("-" * 30)

            else:
                print("Unable to retrieve inventory from the Flask API.")

            input("\nPress Enter to return to the menu...")

        elif choice == "3":
            print("\n===== VIEW INVENTORY ITEM =====")

            item_id = input("Enter the inventory item ID: ")

            try:
                item_id = int(item_id)
            except ValueError:
                print("Invalid ID. Please enter a number.")
                input("\nPress Enter to return to the menu...")
                continue

            response = requests.get(
                f"http://127.0.0.1:5000/inventory/{item_id}"
            )

            if response.status_code == 200:
                item = response.json()

                print("\n===== INVENTORY ITEM =====")
                print(f"ID: {item['id']}")
                print(f"Product: {item['product_name']}")
                print(f"Brand: {item['brands']}")
                print(f"Barcode: {item['barcode']}")
                print(f"Ingredients: {item['ingredients_text']}")
                print(f"Price: {item['price']}")
                print(f"Stock: {item['stock']}")

            elif response.status_code == 404:
                print("Item not found.")

            else:
                print("Unable to retrieve the inventory item.")

            input("\nPress Enter to return to the menu...")

        elif choice == "4":
            print("\n===== UPDATE INVENTORY ITEM =====")

            item_id = input("Enter the inventory item ID: ")

            try:
                item_id = int(item_id)
            except ValueError:
                print("Invalid ID. Please enter a number.")
                input("\nPress Enter to return to the menu...")
                continue

    
            response = requests.get(
                f"http://127.0.0.1:5000/inventory/{item_id}"
            )

            if response.status_code == 404:
                print("Item not found.")
                input("\nPress Enter to return to the menu...")
                continue

            if response.status_code != 200:
                print("Unable to retrieve item.")
                input("\nPress Enter to return to the menu...")
                continue

            item = response.json()
            print(f"\nProduct: {item['product_name']}")
            print()

           

            new_price = input(
                f"Enter new price (current: {item['price']}): "
            )
            new_stock = input(
                f"Enter new stock (current:{item['stock']}): ")

            update_data = {}

            if new_price:
                try:
                    update_data["price"] = float(new_price)
                except ValueError:
                    print("Price must be a number.")
                    input("\nPress Enter to return to the menu...")
                    continue

            if new_stock:
                try:
                    update_data["stock"] = int(new_stock)
                except ValueError:
                    print("Stock must be a whole number.")
                    input("\nPress Enter to return to the menu...")
                    continue

            if not update_data:
                print("No changes were entered.")
                input("\nPress Enter to return to the menu...")
                continue

            response = requests.patch(
                f"http://127.0.0.1:5000/inventory/{item_id}",
                json=update_data
            )

            if response.status_code == 200:
                item = response.json()

                print("\nItem updated successfully!")
                print(f"Product: {item['product_name']}")
                print(f"Price: {item['price']}")
                print(f"Stock: {item['stock']}")

            elif response.status_code == 404:
                print("Item not found.")

            else:
                print("Unable to update item.")
                print(f"Status code: {response.status_code}")
                print(f"Response: {response.text}")

            input("\nPress Enter to return to the menu...")

        elif choice == "5":
            print("\n===== DELETE INVENTORY ITEM =====")

            item_id = input("Enter the inventory item ID: ")

            try:
                item_id = int(item_id)
            except ValueError:
                print("Invalid ID. Please enter a number.")
                input("\nPress Enter to return to the menu...")
                continue

    
            response = requests.get(
                f"http://127.0.0.1:5000/inventory/{item_id}"
            )

            if response.status_code == 404:
                print("Item not found.")
                input("\nPress Enter to return to the menu...")
                continue

            if response.status_code != 200:
                print("Unable to retrieve item.")
                input("\nPress Enter to return to the menu...")
                continue

            item = response.json()

            print(f"\nProduct: {item['product_name']}")
            print(f"Price: {item['price']}")
            print(f"Stock: {item['stock']}")

            confirm = input("\nAre you sure you want to delete this item? (y/n): ")

            if confirm.lower() != "y":
             print("Delete cancelled.")
             input("\nPress Enter to return to the menu...")
             continue

            response = requests.delete(
                f"http://127.0.0.1:5000/inventory/{item_id}"
            )

            if response.status_code == 200:
                print("\nItem deleted successfully!")

            elif response.status_code == 404:
             print("Item not found.")

            else:
                print("Unable to delete item.")
                print(f"Status code: {response.status_code}")
                print(f"Response: {response.text}")

            input("\nPress Enter to return to the menu...")

        elif choice == "6":
            print("\n===== FIND PRODUCT ON OPENFOODFACTS =====")

            barcode = input("Enter product barcode: ")

            product = search_product_by_barcode(barcode)

            if product:
                print("\n===== PRODUCT FOUND =====")
                print(f"Product: {product['product_name']}")
                print(f"Brand: {product['brands']}")
                print(f"Barcode: {product['barcode']}")
                print(f"Ingredients: {product['ingredients_text']}")
            else:
                print("Product not found.")

            input("\nPress Enter to return to the menu...")

        elif choice == "7":
            print("\n===== IMPORT PRODUCT FROM OPENFOODFACTS =====")

            barcode = input("Enter product barcode: ")

            product = search_product_by_barcode(barcode)

            if not product:
                print("Product not found.")
                input("\nPress Enter to return to the menu...")
                continue

            try:
                price = float(input("Enter price: "))
                stock = int(input("Enter stock quantity: "))
            except ValueError:
                print("Price must be a number and stock must be a whole number.")
                input("\nPress Enter to return to the menu...")
                continue

            new_item = {
                "product_name": product["product_name"],
                "brands": product["brands"],
                "barcode": product["barcode"],
                "ingredients_text": product["ingredients_text"],
                "price": price,
                "stock": stock
            }

            response = requests.post(
                "http://127.0.0.1:5000/inventory",
                json=new_item
            )

            if response.status_code == 201:
                item = response.json()

                print("\nProduct imported successfully!")
                print(f"ID: {item['id']}")
                print(f"Product: {item['product_name']}")
                print(f"Brand: {item['brands']}")
                print(f"Price: {item['price']}")
                print(f"Stock: {item['stock']}")

            else:
                print("\nUnable to import product.")
                print(f"Status code: {response.status_code}")
                print(f"Response: {response.text}")

            input("\nPress Enter to return to the menu...")

        elif choice == "8":
            print("Goodbye!")
            break

        else:
            print("Invalid choice. Please select an option from 1 to 8.")


if __name__ == "__main__":
    main()