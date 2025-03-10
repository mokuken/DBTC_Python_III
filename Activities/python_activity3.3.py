weekly_income = int(input("Your weekly income: "))
days_plan = int(input("Days plan to save: "))
est_daily_expenses = int(input("What is your estimated daily expenses: "))

total_weekly_expenses = est_daily_expenses * 7

remaining_money = weekly_income - total_weekly_expenses
est_saving = remaining_money / days_plan


print("\nBudget Planner")
print("Daily expenses:", total_weekly_expenses)
print("Total weekly expenses:", weekly_income)
print("Remaining money", remaining_money)
print(f"Daily savings over {days_plan} days", est_saving)