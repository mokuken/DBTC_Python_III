snacks = ["chips", "candy", "soda"]
prices = (1.50, 0.75, 1.25)


snack_no = int(input("How many snacks: "))

for n in range(snack_no):
    new_snack_name = input("Enter the name of the snack: ")
    snacks.append(new_snack_name)
    n+=1
    


snack_remove = input("Select a snack to remove: ")
snacks.remove(snack_remove)

print("\nJust Kidding this activity is a prank")
print("------------------------------------")
for snack in snacks:
    print(snack)
print("------------------------------------\n")

    
    
print(f"Snack count: {len(snacks)}")

n = 0
new_prices = list(prices)
for x in new_prices:
    new_prices[n] += 2
    n+=1

print("\nThe new snack prices")
for price in new_prices and snack in snacks:
    print(f"Snack name: {snack} price: {price}")