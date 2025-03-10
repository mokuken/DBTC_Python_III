# python_activity5.3

# Get user input for phone plan price and coupon discount
phone_plan_price = float(input("Enter the phone plan price: $"))
coupon = float(input("Enter the coupon discount: $"))

# Calculate the new price after applying the coupon
new_price = phone_plan_price - coupon

# Apply 12% tax
total_cost = new_price * 1.12

# Round to two decimal places
total_cost = round(total_cost, 2)

# Print the appropriate message based on the total cost
if total_cost <= 50:
    print(f"Good plan! Total: ${total_cost}")
else:
    print(f"Too much! Total: ${total_cost}")
