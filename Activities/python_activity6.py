budget = float(input("What the total budget: $"))
no_friends = int(input("Number of friends joining: "))
snack_price = float(input("Snack price per pack: $"))
packs_wanted = int(input("Number of packs: "))

snack_cost = snack_price * packs_wanted

budget_25_percent = budget * 0.25 # 25 percent of budget
budget_50_percent = budget * 0.50 # 50% of the budget
budget_75_percent = budget * 0.75 # 75% of the budget

snack_discount = snack_cost * 0.05

if snack_cost > budget:
    print(f"\nOver budget! Snack cost: ${snack_cost:.2f}")
elif snack_cost <= budget_25_percent:
    print(f"\nSmall snack haul! Discounted cost: ${snack_cost - snack_discount:.2f}")
elif (snack_cost > budget_25_percent and snack_cost <= budget_50_percent) and no_friends >= 3:
    print(f"\nGroup snack deal! Cost: ${snack_cost:.2f}")
elif snack_cost > budget_50_percent and snack_cost <= budget_75_percent:
    print(f"\nMedium snack plan! Cost: ${snack_cost:.2f}")
elif snack_cost > budget_75_percent and snack_cost <= budget:
    print(f"\nBig snack night! Cost: ${snack_cost:.2f}")

if packs_wanted * no_friends < 5:
    print(f"Warning: Might not have enught snacks!")




