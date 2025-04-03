# Refactored code
# This code follows the Single Responsibility Principle (SRP).
class Order:
    def __init__(self, order_id, items):
        self.order_id = order_id
        self.items = items
    
    # I removed the orderCalculator, InvoicePrinter, OrderRepository methods and move into different classes

# This class is responsible for calculating the total price of the order.
class OrderCalculator:
    def calculate_total(order):
        return sum(price for _, price in order.items)

# This class is responsible for printing the invoice.
class InvoicePrinter:
    def print_invoice(order):
        print(f"Invoice for Order ID: {order.order_id}")
        for item, price in order.items:
            print(f"{item}: ${price}")
        print(f"Total: ${OrderCalculator.calculate_total(order)}")

# This class is responsible for saving the order to a database.
class OrderRepository:
    def save_to_database(order):
        print(f"Saving order {order.order_id} to database...")

# Test the refactored code
print("=== Testing Followed SRP Code ===")
order1 = Order(2, [("Keyboard", 100), ("Monitor", 300)])
InvoicePrinter.print_invoice(order1)
OrderRepository.save_to_database(order1)