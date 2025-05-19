import sqlite3


class Product:
    def __init__(self, name: str, quantity: int, price: int):
        self.name = name
        self.quantity = quantity
        self.price = price


class ProductCreate:
    @staticmethod
    def create_reservation(name: str, quantity: str, price: str) -> Product:
        if not name.strip() or not quantity.strip() or not price.strip():
            raise ValueError("Name, guests, and date cannot be empty.")
        if not quantity.isdigit():
            raise ValueError("Guests must be a numeric value.")
        return Product(name.strip(), int(quantity), price.strip())


class InventoryManager:
    def __init__(self, db_path: str):
        self.conn = sqlite3.connect(db_path)
        self.cursor = self.conn.cursor()
        self._create_table()

    def _create_table(self) -> None:
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS products (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                quantity INTEGER NOT NULL,
                price REAL NOT NULL
            )
        ''')
        self.conn.commit()

    def add_product(self, item: Product) -> None:
        try:
            self.cursor.execute("INSERT INTO products (name, quantity, price) VALUES (?, ?, ?)",
                                (item.name, item.quantity, item.price))
            self.conn.commit()
            print("Product added successfully.")
        except sqlite3.Error as e:
            print(f"Failed to add the product: {e}")

    def update_product(self, new_name: str, new_quantity: int, new_price: str, select_id: int) -> None:
        self.cursor.execute("UPDATE products SET name = ?, quantity = ?, price = ? WHERE id = ?",
                            (new_name.strip(), new_quantity, new_price, select_id))
        if self.cursor.rowcount == 0:
            print("Product not found.")
        else:
            self.conn.commit()
            print("Product updated successfully.")

    def delete_product(self, product_id: int) -> None:
        self.cursor.execute("DELETE FROM products WHERE id = ?", (product_id,))
        if self.cursor.rowcount == 0:
            print("Product not found.")
        else:
            self.conn.commit()
            print("Product deleted successfully.")

    def view_products(self) -> None:
        self.cursor.execute("SELECT id, name, quantity, price FROM products")
        rows = self.cursor.fetchall()

        print("\n+----+----------------------+----------+-------------+")
        print("| ID | Name                 | Quantity | Price       |")
        print("+----+----------------------+----------+-------------+")
        if not rows:
            print("|{:^52}|".format("No reservations found."))
        else:
            for row in rows:
                id_, name, quantity, price = row
                print(f"| {id_:<2} | {name:<20} | {quantity:<8} | {price:<11} |")
        print("+----+----------------------+----------+-------------+")

    def close(self) -> None:
        self.conn.close()


class InventoryConsole:
    def __init__(self, manager: InventoryManager):
        self.manager = manager

    def run(self) -> None:
        while True:
            print("\nWelcome to the Product Inventory System!")
            print("[1] Add Product")
            print("[2] View Products")
            print("[3] Update Product")
            print("[4] Delete Product")
            print("[5] Exit")

            choice = input("Choose an option (1-5): ").strip()

            if choice == "1":
                name = input("Enter name: ")
                quantity = input("Enter quantity: ")
                price = input("Enter the price: ")
                try:
                    Product = ProductCreate.create_reservation(name, quantity, price)
                    self.manager.add_product(Product)
                except ValueError as e:
                    print(f"Error: {e}")

            elif choice == "2":
                self.manager.view_products()

            elif choice == "3":
                try:
                    select_id = int(input("Enter ID of Product to update: "))
                    new_name = input("Enter new name: ")
                    mew_quantity = int(input("Enter new quantity: "))
                    new_price = int(input("Enter new price: "))
                    self.manager.update_product(new_name, mew_quantity, new_price, select_id)
                except ValueError:
                    print("ID and quantity must be numeric.")

            elif choice == "4":
                try:
                    product_id = int(input("Enter ID of product to delete: "))
                    self.manager.delete_product(product_id)
                except ValueError:
                    print("ID must be numeric.")

            elif choice == "5":
                print("Goodbye!")
                self.manager.close()
                break

            else:
                print("Invalid choice. Please enter a number between 1 and 5.")


if __name__ == "__main__":
    inventory_manager = InventoryManager("./Database/inventroy.sqlite")
    app = InventoryConsole(inventory_manager)
    app.run()
