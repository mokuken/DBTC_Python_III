products = {
    "corn beef" : 24,
    "noodles" : 12,
    "century tuna" : 32,
    "pancit canton" : 18
}

products["kopiko"] = 12

print("\nThe updated products")
for product_list, items in products.items():
    print(f"{product_list} with a price of {items}")
