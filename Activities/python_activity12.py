food = ["Burger"]
price = [42]
stock = [15]

def manage_menu(chosen):
    if chosen == 1:
        while True:
            print("\n----- ADD NEW FOOD -----")
            try: 
                new_food = input("Enter new food: ")
                new_price = int(input("Enter the price: "))
                new_stock = int(input("Enter the stock: "))
            except ValueError:
                print("Please enter a valid number")
                continue

            food.append(new_food)
            price.append(new_price)
            stock.append(new_stock)

            print(f"\n{new_food} added to menu (P{new_price}, {new_price} in stock).")

            show_menu()
            again = input("Add another food? (yes/no): ")
            if again == "yes":
                continue
            elif again == "no":
                break
            else:
                continue

    elif chosen == 2:
        show_menu()
        while True:
            edit_food = input("Enter a food to edit: ")
            food_index = food.index(edit_food)
            price.pop(food_index)
            stock.pop(food_index)

            edit_price = int(input("Enter the new price: "))
            edit_stock = int(input("Enter the new stock: "))

            price.insert(food_index, edit_price)
            stock.insert(food_index, edit_stock)

            show_menu()
            again = input("Edit another food? (yes/no): ")
            if again == "yes":
                continue
            elif again == "no":
                break
            else:
                continue
        
    elif chosen == 3:
        show_menu()

        while True:
            del_food = input("Enter the name of food to delete: ")
            food_index = food.index(del_food)
            food.remove(del_food)
            price.pop(food_index)
            stock.pop(food_index)

            show_menu()
            again = input("Delete another food? (yes/no): ")
            if again == "yes":
                continue
            elif again == "no":
                break
            else:
                continue

def show_menu():
    print("\n-----------------------------------------")
    print("Food name       Price (P)       Stock")
    print("-------------------------------------------")
    if len(food) > 0:
        for i in range(len(food)):
                print(f"{food[i]}\t\tP {price[i]}\t\t{stock[i]}")
    elif len(food) == 0:
        print("Empty Inventory.")
    print("-------------------------------------------")

print("Select from these choices:\n"
    "1 = Add Food\n"
    "2 = Edit Food\n"
    "3 = Delete Food\n")

action = int(input("(1-3) Pick an action: "))

while True:
    manage_menu(action)
    promt = input("Do another action (yes/no): ")
    if promt == "yes":
        action = int(input("(1-3) Pick an action: "))
        promt = "yes"
        continue
    else:
        print("\nThank you for using Roxas City Restaurant Manager")
        break
