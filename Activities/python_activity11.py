#### TASK ONE
greeting = "welcome user"
name = input("Enter your name: ")

def greet(name):
    print("\n========================")
    print(greeting, name)
    print("========================\n")

greet(name)

#### TASK TWO
snack_quantity = 10
snack_cost = 5
discount = 25

def cal_snacks(discount):
    total = snack_quantity * snack_cost
    discount = total * (discount / 100)
    return total - discount


snack = cal_snacks(discount)
print(f"Total snack price {snack} with the discount of {discount}%\n")


#### TASK THREE
global_total = 10
subject = "Python"

def time_tracker(hour, subject):
    new_global_total = global_total + hour
    subject = subject

    print(f"You studied for {new_global_total} hours on {subject}")

time_tracker(72, subject)