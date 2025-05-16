import sqlite3


class Reservation:
    def __init__(self, name: str, guests: int, date: str):
        self.name = name
        self.guests = guests
        self.date = date


class ReservationCreate:
    @staticmethod
    def create_reservation(name: str, guests: str, date: str) -> Reservation:
        if not name.strip() or not guests.strip() or not date.strip():
            raise ValueError("Name, guests, and date cannot be empty.")
        if not guests.isdigit():
            raise ValueError("Guests must be a numeric value.")
        return Reservation(name.strip(), int(guests), date.strip())


class ReservationManager:
    def __init__(self, db_path: str):
        self.conn = sqlite3.connect(db_path)
        self.cursor = self.conn.cursor()
        self._create_table()

    def _create_table(self) -> None:
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS reservations (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                guests INTEGER NOT NULL,
                date TEXT NOT NULL
            )
        ''')
        self.conn.commit()

    def add_reservation(self, item: Reservation) -> None:
        try:
            self.cursor.execute("INSERT INTO reservations (name, guests, date) VALUES (?, ?, ?)",
                                (item.name, item.guests, item.date))
            self.conn.commit()
            print("Reservation added successfully.")
        except sqlite3.Error as e:
            print(f"Failed to add reservation: {e}")

    def update_reservation(self, new_name: str, new_guests: int, new_date: str, select_id: int) -> None:
        self.cursor.execute("UPDATE reservations SET name = ?, guests = ?, date = ? WHERE id = ?",
                            (new_name.strip(), new_guests, new_date.strip(), select_id))
        if self.cursor.rowcount == 0:
            print("Reservation not found.")
        else:
            self.conn.commit()
            print("Reservation updated successfully.")

    def delete_reservation(self, reservation_id: int) -> None:
        self.cursor.execute("DELETE FROM reservations WHERE id = ?", (reservation_id,))
        if self.cursor.rowcount == 0:
            print("Reservation not found.")
        else:
            self.conn.commit()
            print("Reservation deleted successfully.")

    def view_reservations(self) -> None:
        self.cursor.execute("SELECT id, name, guests, date FROM reservations")
        rows = self.cursor.fetchall()

        print("\n+----+----------------------+--------+------------+")
        print("| ID | Name                 | Guests | Date       |")
        print("+----+----------------------+--------+------------+")
        if not rows:
            print("|{:^49}|".format("No reservations found."))
        else:
            for row in rows:
                id_, name, guests, date = row
                print(f"| {id_:<2} | {name:<20} | {guests:<6} | {date:<10} |")
        print("+----+----------------------+--------+------------+")

    def close(self) -> None:
        self.conn.close()


class ReservationConsole:
    def __init__(self, manager: ReservationManager):
        self.manager = manager

    def run(self) -> None:
        while True:
            print("\nReservation Menu")
            print("1. Add Reservation")
            print("2. View Reservations")
            print("3. Update Reservation")
            print("4. Delete Reservation")
            print("5. Exit")

            choice = input("Choose an option (1-5): ").strip()

            if choice == "1":
                name = input("Enter name: ")
                guests = input("Enter number of guests: ")
                date = input("Enter reservation date (YYYY-MM-DD): ")
                try:
                    reservation = ReservationCreate.create_reservation(name, guests, date)
                    self.manager.add_reservation(reservation)
                except ValueError as e:
                    print(f"Error: {e}")

            elif choice == "2":
                self.manager.view_reservations()

            elif choice == "3":
                try:
                    select_id = int(input("Enter ID of reservation to update: "))
                    new_name = input("Enter new name: ")
                    new_guests = int(input("Enter new number of guests: "))
                    new_date = input("Enter new reservation date (YYYY-MM-DD): ")
                    self.manager.update_reservation(new_name, new_guests, new_date, select_id)
                except ValueError:
                    print("ID and guests must be numeric.")

            elif choice == "4":
                try:
                    reservation_id = int(input("Enter ID of reservation to delete: "))
                    self.manager.delete_reservation(reservation_id)
                except ValueError:
                    print("ID must be numeric.")

            elif choice == "5":
                print("Goodbye!")
                self.manager.close()
                break

            else:
                print("Invalid choice. Please enter a number between 1 and 5.")


if __name__ == "__main__":
    reservation_manager = ReservationManager("./Database/reservations.sqlite")
    app = ReservationConsole(reservation_manager)
    app.run()
