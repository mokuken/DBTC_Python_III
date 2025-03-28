# Dictionary to store book inventory with book name as key and details as value
book = {
    "one": {"author": "same", "dop": 2025, "stock": 24},
    "two": {"author": "name", "dop": 2020, "stock": 16},
    "three": {"author": "same", "dop": 2025, "stock": 50}
}

# Function to manage the inventory based on user choice
def manage_inventory(chosen):
    if chosen == 1:  # Add a new book
        while True:
            print("\n----- ADD NEW BOOK -----")
            try: 
                # Input details for the new book
                new_book = input("Enter book name: ")
                new_author = input("Enter the name of author: ")
                new_dop = int(input("Enter the date of publish: "))
                new_stock = int(input("Enter the number of stock: "))
            except ValueError:
                # Handle invalid input for numbers
                print("Please enter a valid number")
                continue

            # Add the new book to the inventory
            book[new_book] = {"author": new_author, "dop": new_dop, "stock": new_stock}

            print(f"\n{new_book} by {new_author}, published on {new_dop} is added to inventory!).")

            # Display the updated inventory
            show_inventory()
            if input("Add another book? (yes/no): ").lower() == "yes":
                continue
            else:
                break

    elif chosen == 2:  # Edit an existing book
        show_inventory()
        while True:
            # Input the book name to edit
            edit_food = input("Enter the book name to edit: ")
            if edit_food in book:
                # Input new details for the book
                edit_price = input("Enter the new Author : ")
                edit_stock = int(input("Enter the new DoP: "))

                # Update the book details
                book[edit_food]["author"] = edit_price
                book[edit_food]["dop"] = edit_stock

                # Display the updated inventory
                show_inventory()
                if input("Edit another book? (yes/no): ").lower() != "yes":
                    break
                
            else:
                # Handle case where book is not found
                print("Book not found in menu.")
                continue

    elif chosen == 3:  # Delete a book
        show_inventory()

        while True:
            # Input the book name to delete
            del_book = input("Enter the name of Book to delete: ")
            confirm_del = input("Are you sure? (yes/no): ")
            if del_book in book:
                if confirm_del == "yes":
                    # Delete the book from inventory
                    del book[del_book]
                    show_inventory()

            else:
                # Handle case where book is not found
                print("Book not found in the inventory.")
                continue

            if input("Delete another book? (yes/no): ").lower() != "yes":
                break
    
    elif chosen == 4:  # Search for a book
        while True:
            # Choose search type: by author name or date of publication
            search_type = input("Search by Author Name or Date of Publish (an/dop): ")

            if search_type == "an":  # Search by author name
                search_an = input("Enter the author name: ")
                found = False
                print(f"\n{'-' * 60}")
                print(f"Book Name\tAuthor\t\tDoP\t\tStocks")
                print("-" * 60)
                for name, details in book.items():
                    if details["author"].lower() == search_an.lower():
                        # Display books by the specified author
                        print(f"{name}\t\t{details['author']}\t\t{details['dop']}\t\t{details['stock']}")
                        found = True
                if not found:
                    print("No books found by that author.")
                print("-" * 60)
            elif search_type == "dop":  # Search by date of publication
                search_dop = int(input("Enter the date of publication: "))
                found = False
                print(f"\n{'-' * 60}")
                print(f"Book Name\tAuthor\t\tDoP\t\tStocks")
                print("-" * 60)
                for name, details in book.items():
                    if details["dop"] == search_dop:
                        # Display books published on the specified date
                        print(f"{name}\t\t{details['author']}\t\t{details['dop']}\t\t{details['stock']}")
                        found = True
                if not found:
                    print("No books found by that date of publication.")
                print("-" * 60)
            
            if input("Search another book? (yes/no): ").lower() != "yes":
                break

    elif chosen == 5:  # View all books
        show_inventory()

# Function to display the inventory
def show_inventory():
    print(f"\n{'-' * 60}")
    print(f"Book Name\tAuthor\t\tDoP\t\tStocks")
    print("-" * 60)
    if len(book) > 0:
        # Display all books in the inventory
        for name, details in book.items():
            print(f"{name}\t\t{details['author']}\t\t{details['dop']}\t\t{details['stock']}")
    else:
        # Handle case where inventory is empty
        print("Empty Inventory.")
    print("-" * 60)

# Display menu options to the user
print("\nSelect from these choices:\n"
    "1 = Add Book\n"
    "2 = Edit Book\n"
    "3 = Delete Book\n"
    "4 = Search Book\n"
    "5 = View All Books\n")

# Input the user's action choice
action = int(input("(1-5) Pick an action: "))

# Loop to allow multiple actions until the user decides to exit
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
        # Exit message
        print("\nThank you for using Roxas City Book Inventory Management")
        break