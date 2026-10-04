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

            print("\nItem added successfully!")
            print(f"New item ID: {new_id}")

            input("\nPress Enter to return to the menu...")

        elif choice == "2":
            if not inventory:
                print("Inventory is empty.")
            else:
                print("\n===== INVENTORY =====")

                for item in inventory:
                    print(f"ID: {item['id']}")
                    print(f"Product: {item['product_name']}")
                    print(f"Brand: {item['brands']}")
                    print(f"Barcode: {item['barcode']}")
                    print(f"Price: {item['price']}")
                    print(f"Stock: {item['stock']}")
                    print("-" * 30)
            input("\nPress Enter to return to the menu...")

        elif choice == "3":
            item_id = input("Enter the inventory item ID: ")

            try:
                item_id = int(item_id)
            except ValueError:
                print("Invalid ID. Please enter a number.")
                continue

            found_item = None

            for item in inventory:
                if item["id"] == item_id:
                    found_item = item
                    break

            if found_item:
                print("\n===== INVENTORY ITEM =====")
                print(f"ID: {found_item['id']}")
                print(f"Product: {found_item['product_name']}")
                print(f"Brand: {found_item['brands']}")
                print(f"Barcode: {found_item['barcode']}")
                print(f"Ingredients: {found_item['ingredients_text']}")
                print(f"Price: {found_item['price']}")
                print(f"Stock: {found_item['stock']}")
            else:
                print("Item not found.")
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

            found_item = None

            for item in inventory:
                if item["id"] == item_id:
                    found_item = item
                    break

            if not found_item:
                print("Item not found.")
                input("\nPress Enter to return to the menu...")
                continue

            print(f"\nUpdating: {found_item['product_name']}")

            new_price = input(f"Enter new price (current: {found_item['price']}): ")
            new_stock = input(f"Enter new stock (current: {found_item['stock']}): ")

            try:
                if new_price:
                    found_item["price"] = float(new_price)

                if new_stock:
                    found_item["stock"] = int(new_stock)

            except ValueError:
                print("Price must be a number and stock must be a whole number.")
                input("\nPress Enter to return to the menu...")
                continue

            print("\nItem updated successfully!")

            print(f"Price: {found_item['price']}")
            print(f"Stock: {found_item['stock']}")

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

            found_item = None

            for item in inventory:
                if item["id"] == item_id:
                    found_item = item
                    break

            if not found_item:
                print("Item not found.")
                input("\nPress Enter to return to the menu...")
                continue

            print(f"\nYou are about to delete: {found_item['product_name']}")

            confirmation = input("Are you sure? (y/n): ").lower()

            if confirmation == "y":
                inventory.remove(found_item)
                print("Item deleted successfully!")
            else:
                print("Delete cancelled.")

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

            new_id = max([item["id"] for item in inventory], default=0) + 1

            new_item = {
                "id": new_id,
                "product_name": product["product_name"],
                "brands": product["brands"],
                "barcode": product["barcode"],
                "ingredients_text": product["ingredients_text"],
                "price": price,
                "stock": stock
            }

            inventory.append(new_item)

            print("\nProduct imported successfully!")
            print(f"ID: {new_id}")
            print(f"Product: {new_item['product_name']}")
            print(f"Brand: {new_item['brands']}")
            print(f"Price: {new_item['price']}")
            print(f"Stock: {new_item['stock']}")

            
            input("\nPress Enter to return to the menu...")

        elif choice == "8":
            print("Goodbye!")
            break

        else:
            print("Invalid choice. Please select an option from 1 to 8.")


if __name__ == "__main__":
    main()