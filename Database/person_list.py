import sqlite3

# --- S: Single Responsibility Principle ---
class Item:
    def __init__(self, name: str, price: int, stock: int):
        self.name = name
        self.price = price
        self.stock = stock

# --- Factory Pattern ---
class ItemCreate:
    @staticmethod
    def create_item(name: str, price: int, stock: int) -> Item:
        return Item(name, price, stock)

# --- O: Open/Closed Principle & Database Interaction ---
class InventoryManager:
    def __init__(self, db_path="inventory.db"):
        self.conn = sqlite3.connect(db_path)
        self.cursor = self.conn.cursor()
        self._create_table()

    def _create_table(self):
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS inventory (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL UNIQUE,
                price INTEGER NOT NULL,
                stock INTEGER NOT NULL
            )
        ''')
        self.conn.commit()

    def add_item(self, item: Item):
        try:
            self.cursor.execute("INSERT INTO inventory (name, price, stock) VALUES (?, ?, ?)",
                                (item.name, item.price, item.stock))
            self.conn.commit()
            print(f"'{item.name}' ({item.price})each added with stock {item.stock}.")
        except sqlite3.IntegrityError:
            print(f"Item '{item.name}' already exists.")

    def update_stock(self, name: str, new_stock: int):
        self.cursor.execute("UPDATE inventory SET stock = ? WHERE name = ?", (new_stock, name))
        if self.cursor.rowcount == 0:
            print("Item not found.")
        else:
            self.conn.commit()
            print(f"Stock for '{name}' updated to {new_stock}.")

    def delete_item(self, name: str):
        self.cursor.execute("DELETE FROM inventory WHERE name = ?", (name,))
        if self.cursor.rowcount == 0:
            print("Item not found.")
        else:
            self.conn.commit()
            print(f"Item '{name}' has been deleted from inventory.")

    def view_inventory(self):
        self.cursor.execute("SELECT name, price, stock FROM inventory")
        rows = self.cursor.fetchall()

        if not rows:
            print("\n+-----------------+---------------+---------------+")
            print("| {:<15} | {:<13} | {:<13} |".format("Item", "Price", "Stock"))
            print("+-----------------+---------------+---------------+")
            print("|{:^47}|".format("Inventory is empty."))
            print("+-----------------+---------------+---------------+")
            return

        print("\n+-----------------+---------------+---------------+")
        print("| {:<15} | {:<13} | {:<13} |".format("Item", "Price", "Stock"))
        print("+-----------------+---------------+---------------+")
        for name, price, stock in rows:
            print("| {:<15} | {:<13} | {:<13} |".format(name, price, stock))
        print("+-----------------+---------------+---------------+")

    def close(self):
        self.conn.close()

# --- D: Dependency Inversion Principle ---
class InventoryConsole:
    def __init__(self, manager: InventoryManager):
        self.manager = manager

    def run(self):
        while True:
            print("\n1. Add Item\n2. Update Stock\n3. Delete Item\n4. View Inventory\n5. Exit")
            choice = input("Choose an option (1-5): ")

            if choice == "1":
                name = input("Enter item name: ")
                try:
                    price = int(input("Enter item price: "))
                    stock = int(input("Enter stock quantity: "))
                    item = ItemCreate.create_item(name, price, stock)
                    self.manager.add_item(item)
                except ValueError:
                    print("Price and stock must be numbers.")

            elif choice == "2":
                name = input("Enter item name to update stock: ")
                try:
                    new_stock = int(input("Enter new stock quantity: "))
                    self.manager.update_stock(name, new_stock)
                except ValueError:
                    print("Stock must be a number.")

            elif choice == "3":
                name = input("Enter item name to delete: ")
                self.manager.delete_item(name)

            elif choice == "4":
                self.manager.view_inventory()

            elif choice == "5":
                print("Goodbye!")
                self.manager.close()
                break

            else:
                print("Invalid choice.")

# --- Run the application ---
if __name__ == "__main__":
    inventory_manager = InventoryManager("inventory.db")
    ui = InventoryConsole(inventory_manager)
    ui.run()
