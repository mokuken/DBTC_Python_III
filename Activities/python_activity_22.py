"""Inventory Management System"""

# --- S: Single Responsibility Principle ---
class Item:
    """Represents a single item in the inventory with a name, price, and stock quantity."""
    def __init__(self, name: str, price: int, stock: int):
        self.name = name
        self.price = price
        self.stock = stock

# --- Factory Pattern ---
class ItemCreate:
    """Factory for creating Item instances."""
    @staticmethod
    def create_item(name: str, price: int, stock: int) -> Item:
        """Creates and returns a new Item instance."""
        return Item(name, price, stock)

# --- O: Open/Closed Principle ---
class InventoryManager:
    """Manages the inventory, allowing adding, updating, and viewing items."""
    def __init__(self):
        self.inventory = {}

    def add_item(self, item: Item):
        """Adds an item to the inventory."""
        self.inventory[item.name] = item
        print(f"'{item.name}' ({item.price})each added with stock {item.stock}.")

    def update_stock(self, name: str, new_stock: int):
        """Updates the stock quantity for a given item by name."""
        if name in self.inventory:
            self.inventory[name].stock = new_stock
            print(f"Stock for '{name}' updated to {new_stock}.")
        else:
            print("Item not found.")

    def view_inventory(self):
        """show the items available in the inventory"""
        print(f"\n{'-' * 15} Inventory {'-' * 15}")
        if not self.inventory:
            print("Inventory is empty.")
            return
        print(f"{'Item':<15}{'Price':<15}{'Stock':<15}")
        print("-" * 41)
        for item in self.inventory.values():
            print(f"{item.name:<15}{item.price:<15}{item.stock}")
        print("-" * 41)

# --- D: Dependency Inversion Principle ---
class InventoryConsole:
    """Handles user interaction for the inventory system via the console."""
    def __init__(self, manager: InventoryManager):
        self.manager = manager

    def run(self):
        """Main loop for handling user commands in the inventory system."""
        while True:
            print("\n1. Add Item\n2. Update Stock\n3. View Inventory\n4. Exit")
            choice = input("Choose an option (1-4): ")

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
                self.manager.view_inventory()
            elif choice == "4":
                print("Goodbye!")
                break
            else:
                print("Invalid choice.")

# --- Run the application ---
if __name__ == "__main__":
    inventory_manager = InventoryManager()
    ui = InventoryConsole(inventory_manager)
    ui.run()
