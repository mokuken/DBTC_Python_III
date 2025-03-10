# python_activity5.2

# Get user input for snack price and discount amount
snack_price = float(input("Enter the snack price: "))
discount = float(input("Enter the discount amount: "))

# Calculate the new price after discount
new_price = snack_price - discount

# Apply 12% tax
final_cost = new_price * 1.12

# Round to two decimal places
final_cost = round(final_cost, 2)

# Check if the cost is less than 3 and print accordingly
if final_cost < 3:
    print(f"Cheap snack! Cost: {final_cost}")
