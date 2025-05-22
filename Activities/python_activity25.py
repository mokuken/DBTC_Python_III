import sqlite3


class LibraryDB:
    def __init__(self, db_path="./Database/library.sqlite"):
        self.conn = sqlite3.connect(db_path)
        self.cursor = self.conn.cursor()
        self._create_tables()

    def _create_tables(self):
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS books (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                title TEXT NOT NULL,
                author TEXT NOT NULL,
                available INTEGER NOT NULL DEFAULT 1
            )
        ''')
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS borrowers (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL
            )
        ''')
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS transactions (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                borrower_id INTEGER,
                book_id INTEGER,
                status TEXT CHECK(status IN ('borrowed', 'returned')),
                FOREIGN KEY(borrower_id) REFERENCES borrowers(id),
                FOREIGN KEY(book_id) REFERENCES books(id)
            )
        ''')
        self.conn.commit()

    def add_book(self, title, author):
        self.cursor.execute("INSERT INTO books (title, author) VALUES (?, ?)", (title, author))
        self.conn.commit()
        print("Book added.")

    def register_borrower(self, name):
        self.cursor.execute("INSERT INTO borrowers (name) VALUES (?)", (name,))
        self.conn.commit()
        print("Borrower registered.")

    def borrow_book(self, borrower_id, book_id):
        # Check availability
        self.cursor.execute("SELECT available FROM books WHERE id = ?", (book_id,))
        book = self.cursor.fetchone()
        if not book:
            print("Book not found.")
            return
        if book[0] == 0:
            print("Book is currently not available.")
            return

        # Check for duplicate borrow
        self.cursor.execute('''
            SELECT * FROM transactions 
            WHERE borrower_id = ? AND book_id = ? AND status = 'borrowed'
        ''', (borrower_id, book_id))
        if self.cursor.fetchone():
            print("This borrower has already borrowed this book and not returned it.")
            return

        # Borrow book
        self.cursor.execute("UPDATE books SET available = 0 WHERE id = ?", (book_id,))
        self.cursor.execute('''
            INSERT INTO transactions (borrower_id, book_id, status) VALUES (?, ?, 'borrowed')
        ''', (borrower_id, book_id))
        self.conn.commit()
        print("Book borrowed.")

    def return_book(self, borrower_id, book_id):
        self.cursor.execute('''
            SELECT * FROM transactions
            WHERE borrower_id = ? AND book_id = ? AND status = 'borrowed'
        ''', (borrower_id, book_id))
        if not self.cursor.fetchone():
            print("No such active borrow transaction.")
            return

        self.cursor.execute("UPDATE books SET available = 1 WHERE id = ?", (book_id,))
        self.cursor.execute('''
            UPDATE transactions SET status = 'returned'
            WHERE borrower_id = ? AND book_id = ? AND status = 'borrowed'
        ''', (borrower_id, book_id))
        self.conn.commit()
        print("Book returned.")

    def view_transactions(self):
        self.cursor.execute('''
            SELECT t.id, b.name, bk.title, t.status
            FROM transactions t
            JOIN borrowers b ON t.borrower_id = b.id
            JOIN books bk ON t.book_id = bk.id
        ''')
        transactions = self.cursor.fetchall()
        print("\nTransactions:")
        print("+----+----------------+--------------------------+-------------+")
        print("| ID | Borrower       | Book Title               | Status      |")
        print("+----+----------------+--------------------------+-------------+")
        if not transactions:
            print("|{:^62}|".format("No transactions found."))
        else:
            for t in transactions:
                print(f"| {t[0]:<2} | {t[1]:<14} | {t[2]:<24} | {t[3]:<11} |")
        print("+----+----------------+--------------------------+-------------+")

    def close(self):
        self.conn.close()


class LibraryConsole:
    def __init__(self, db: LibraryDB):
        self.db = db

    def run(self):
        while True:
            print("\n📚 Library System Menu")
            print("[1] Add Book")
            print("[2] Register Borrower")
            print("[3] Borrow Book")
            print("[4] Return Book")
            print("[5] View Transactions")
            print("[6] Exit")

            choice = input("Choose an option (1-6): ").strip()
            try:
                if choice == "1":
                    title = input("Enter book title: ")
                    author = input("Enter author name: ")
                    self.db.add_book(title, author)
                elif choice == "2":
                    name = input("Enter borrower name: ")
                    self.db.register_borrower(name)
                elif choice == "3":
                    borrower_id = int(input("Enter borrower ID: "))
                    book_id = int(input("Enter book ID: "))
                    self.db.borrow_book(borrower_id, book_id)
                elif choice == "4":
                    borrower_id = int(input("Enter borrower ID: "))
                    book_id = int(input("Enter book ID: "))
                    self.db.return_book(borrower_id, book_id)
                elif choice == "5":
                    self.db.view_transactions()
                elif choice == "6":
                    print("Goodbye!")
                    self.db.close()
                    break
                else:
                    print("Invalid choice. Enter 1-6.")
            except ValueError:
                print("Invalid input. Please enter numeric values where required.")


if __name__ == "__main__":
    db = LibraryDB()
    app = LibraryConsole(db)
    app.run()
