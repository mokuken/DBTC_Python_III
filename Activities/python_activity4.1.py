price = int(input("Enter orginal price: "))
discount = int(input("Enter discount amount: "))

discounted_price = price - discount
tax = discounted_price / 100 * 12

new_price = discounted_price + tax

print(f"\nThe discounted price {discounted_price}")
print(f"Final price amount {new_price}\n")