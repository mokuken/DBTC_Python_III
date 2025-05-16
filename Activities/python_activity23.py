import sqlite3

class Reservation:
    def __init__(self, name: str, guests: int, date: str):
        self.name = name
        self.guests = guests
        self.date = date

class ReservationCreate:
    @staticmethod
    def create_reservation(name: str, guests: int, date: str) -> Reservation:
        return Reservation(name, guests, date)

class ReservationManager:
    def __init__(self, db_path):
        self.conn = sqlite3.connect(db_path)
        self.cursor = self.conn.cursor()
        self._create_table()

    def _create_table(self):
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS reservations (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                guest INTEGER NOT NULL,
                date TEXT NOT NULL
            )
        ''')
        self.conn.commit()

    def add_reservation(self, item: Reservation):
        if not item.name or not str(item.guests).strip() or not item.date:
            print("Name, guests, and date cannot be empty.")
            return
        try:
            self.cursor.execute("INSERT INTO reservations (name, guest, date) VALUES (?, ?, ?)",
                                (item.name, item.guests, item.date))
            self.conn.commit()
            print("Reservation added successfully.")
        except sqlite3.IntegrityError:
            print(f"Item '{item.name}' already exists.")


    def update_reservation(self, new_name: str, new_guest: int, new_date: str, select_id: int):
        self.cursor.execute("UPDATE reservations SET name = ?, guest = ?, date = ? WHERE id = ?", (new_name, new_guest, new_date, select_id))
        if self.cursor.rowcount == 0:
            print("Item not found.")
        else:
            self.conn.commit()
            print(f"Reservation for '{new_name}' has been updated.")

    def view_reservations(self):
        self.cursor.execute("SELECT id, name, guest, date FROM reservations")
        rows = self.cursor.fetchall()

        if not rows:
            print("\n+-----------------+-----------------+---------------+---------------+")
            print("| {:<15} | {:<15} | {:<13} | {:<13} |".format("id", "Name", "Guests", "Date"))
            print("+-----------------+-----------------+---------------+---------------+")
            print("|{:^67}|".format("reservations is empty."))
            print("+-----------------+-----------------+---------------+---------------+")
            return

        print("\n+-----------------+-----------------+---------------+---------------+")
        print("| {:<15} | {:<15} | {:<13} | {:<13} |".format("id", "Name", "Guests", "Date"))
        print("+-----------------+-----------------+---------------+---------------+")
        for id, name, guest, date in rows:
            print("| {:<15} | {:<15} | {:<13} | {:<13} |".format(id, name, guest, date))
        print("+-----------------+-----------------+---------------+---------------+")

    def close(self):
        self.conn.close()

class ReservationConsole:
    def __init__(self, manager: ReservationManager):
        self.manager = manager

    def run(self):
        while True:
            print("\n1. Add Reservation\n2. View Reservations\n3. Update Reservation\n4. Exit")
            choice = input("Choose an option (1-4): ")

            if choice == "1":
                name = input("Enter name: ")
                try:
                    guests = input("Enter number of guests: ")
                    date = input("Enter reservation date (YYYY-MM-DD): ")
                    item = ReservationCreate.create_reservation(name, guests, date)
                    self.manager.add_reservation(item)
                except ValueError:
                    print("guests must be numbers.")

            elif choice == "2":
                self.manager.view_reservations()

            elif choice == "3":
                try:
                    select_id = int(input("Enter id to update: "))
                    new_name = input("Enter new name: ")
                    new_guest = int(input("Enter number of guests "))
                    new_date = input("Enter reservation date (YYYY-MM-DD): ")
                    self.manager.update_reservation(new_name, new_guest, new_date, select_id)
                except ValueError:
                    print("id and guests must be a number.")

            elif choice == "4":
                print("Goodbye!")
                self.manager.close()
                break

            else:
                print("Invalid choice.")

if __name__ == "__main__":
    reservation_manager = ReservationManager("./Database/reservations.sqlite")
    ui = ReservationConsole(reservation_manager)
    ui.run()
