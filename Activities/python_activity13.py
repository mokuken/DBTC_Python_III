book = {
    "one": {"author": "same", "dop": 2025, "stock": 24},
    "two": {"author": "name", "dop": 2020, "stock": 16},
    "three": {"author": "same", "dop": 2025, "stock": 50}
}

def manage_inventory(chosen):
    if chosen == 1:
        while True:
            print("\n----- ADD NEW BOOK -----")
            try: 
                new_book = input("Enter book name: ")
                new_author = input("Enter the name of author: ")
                new_dop = int(input("Enter the date of publish: "))
                new_stock = int(input("Enter the number of stock: "))
            except ValueError:
                print("Please enter a valid number")
                continue

            book[new_book] = {"author": new_author, "dop": new_dop, "stock": new_stock}

            print(f"\n{new_book} by {new_author}, published on {new_dop} is added to inventory!).")

            show_inventory()
            if input("Add another book? (yes/no): ").lower() == "yes":
                continue
            else:
                break

    elif chosen == 2:
        show_inventory()
        while True:
            edit_food = input("Enter the book name to edit: ")
            if edit_food in book:
                edit_price = input("Enter the new Author : ")
                edit_stock = int(input("Enter the new DoP: "))

                book[edit_food]["author"] = edit_price
                book[edit_food]["dop"] = edit_stock

                show_inventory()
                again = input("Edit another Book? (yes/no): ")
                if again == "yes":
                    continue
                elif again == "no":
                    break
                else:
                    continue
            else:
                print("Book not found in menu.")
                continue

    elif chosen == 3:
        show_inventory()

        while True:
            del_book = input("Enter the name of Book to delete: ")
            confirm_del = input("Are you sure? (yes/no): ")
            if del_book in book:
                if confirm_del == "yes":
                    del book[del_book]
                    show_inventory()

            else:
                print("Book not found in the inventory.")
                continue

            again = input("Delete another Book? (yes/no): ")
            if again == "yes":
                continue
            elif again == "no":
                break
            else:
                continue
    
    elif chosen == 4:
        while True:
            search_type = input("Search by Author Name or Date of Publish (an/dop): ")

            if search_type == "an":
                search_an = input("Enter the author name: ")
                found = True
                print(f"\n{"-" * 60}")
                print(f"Book Name\tAuthor\t\tDoP\t\tStocks")
                print("-" * 60)
                for name, details in book.items():
                    if details["author"].lower() == search_an.lower():
                        print(f"{name}\t\t{details['author']}\t\t{details['dop']}\t\t{details['stock']}")
                        found = True
                    elif found == False:
                        print("No books found by that author.")
                print("-" * 60)
            elif search_type == "dop":
                search_dop = int(input("Enter the date of publication: "))
                found = True
                print(f"\n{"-" * 60}")
                print(f"Book Name\tAuthor\t\tDoP\t\tStocks")
                print("-" * 60)
                for name, details in book.items():
                    if details["dop"] == search_dop:
                        print(f"{name}\t\t{details['author']}\t\t{details['dop']}\t\t{details['stock']}")
                        found = True
                    elif found == False:
                        print("No books found by that date of publication.")
                print("-" * 60)
            
            again = input("Search another Book? (yes/no): ")
            if again == "yes":
                continue
            elif again == "no":
                break
            else:
                continue




    if chosen == 5:
        show_inventory()

def show_inventory():
    print(f"\n{"-" * 60}")
    print(f"Book Name\tAuthor\t\tDoP\t\tStocks")
    print("-" * 60)
    if len(book) > 0:
        for name, details in book.items():
            print(f"{name}\t\t{details['author']}\t\t{details['dop']}\t\t{details['stock']}")
    else:
        print("Empty Inventory.")
    print("-" * 60)

print("\nSelect from these choices:\n"
    "1 = Add Book\n"
    "2 = Edit Book\n"
    "3 = Delete Book\n"
    "4 = Search Book\n"
    "5 = View All Books\n")

action = int(input("(1-5) Pick an action: "))

while True:
    manage_inventory(action)
    promt = input("Do another action (yes/no): ")
    if promt == "yes":
        print("\nSelect from these choices:\n"
            "1 = Add Book\n"
            "2 = Edit Book\n"
            "3 = Delete Book\n"
            "4 = Search Book\n"
            "5 = View All Books\n")
        action = int(input("(1-5) Pick an action: "))
        promt = "yes"
        continue
    else:
        print("\nThank you for using Roxas City Book Inventory Management")
        break