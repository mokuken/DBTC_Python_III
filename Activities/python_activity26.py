import sqlite3
import base64
from abc import ABC, abstractmethod


class Base64Encoder:
    """Utility class for Base64 encoding/decoding."""
    
    @staticmethod
    def encode(data: str) -> str:
        return base64.b64encode(data.encode()).decode()

    @staticmethod
    def decode(data: str) -> str:
        return base64.b64decode(data.encode()).decode()


class User:
    """Represents a user profile."""
    
    def __init__(self, username: str, email: str, password: str, bio: str):
        self.username = username
        self.email = email
        self.password = Base64Encoder.encode(password)
        self.bio = Base64Encoder.encode(bio)


class UserProfileManager(ABC):
    """Abstract base class for profile managers."""
    
    @abstractmethod
    def create_user(self, user: User): pass

    @abstractmethod
    def read_user(self, username: str): pass

    @abstractmethod
    def update_user(self, username: str, email: str, password: str, bio: str): pass

    @abstractmethod
    def delete_user(self, username: str): pass


class UserDatabase(UserProfileManager):
    """SQLite-based implementation of user profile management."""
    
    def __init__(self, db_path: str = "./Database/user_profiles.db"):
        self._conn = sqlite3.connect(db_path)
        self._cursor = self._conn.cursor()
        self._create_table()

    def _create_table(self):
        self._cursor.execute('''
            CREATE TABLE IF NOT EXISTS users (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                username TEXT UNIQUE NOT NULL,
                email TEXT NOT NULL,
                password TEXT NOT NULL,
                bio TEXT NOT NULL
            )
        ''')
        self._conn.commit()

    def create_user(self, user: User):
        try:
            self._cursor.execute(
                "INSERT INTO users (username, email, password, bio) VALUES (?, ?, ?, ?)",
                (user.username, user.email, user.password, user.bio)
            )
            self._conn.commit()
            print("✅ User profile created successfully.")
        except sqlite3.IntegrityError:
            print("❌ Error: Username already exists.")

    def read_user(self, username: str):
        self._cursor.execute("SELECT email, password, bio FROM users WHERE username = ?", (username,))
        result = self._cursor.fetchone()
        if result:
            email, password, bio = result
            print(f"\nUsername: {username}")
            print(f"Email: {email}")
            print(f"Password: {Base64Encoder.decode(password)}")
            print(f"Bio: {Base64Encoder.decode(bio)}")
        else:
            print("❌ Error: User not found.")

    def update_user(self, username: str, email: str, password: str, bio: str):
        encoded_password = Base64Encoder.encode(password)
        encoded_bio = Base64Encoder.encode(bio)
        self._cursor.execute(
            "UPDATE users SET email = ?, password = ?, bio = ? WHERE username = ?",
            (email, encoded_password, encoded_bio, username)
        )
        if self._cursor.rowcount == 0:
            print("❌ Error: User not found.")
        else:
            self._conn.commit()
            print("✅ User profile updated successfully.")

    def delete_user(self, username: str):
        self._cursor.execute("DELETE FROM users WHERE username = ?", (username,))
        if self._cursor.rowcount == 0:
            print("❌ Error: User not found.")
        else:
            self._conn.commit()
            print("✅ User profile deleted successfully.")

    def close(self):
        self._conn.close()


class UserCLI:
    """CLI for user profile management."""
    
    def __init__(self, db: UserProfileManager):
        self._db = db

    def _prompt(self, message: str) -> str:
        return input(message).strip()

    def create_profile(self):
        username = self._prompt("Enter username: ")
        email = self._prompt("Enter email: ")
        password = self._prompt("Enter password: ")
        bio = self._prompt("Enter bio: ")
        user = User(username, email, password, bio)
        self._db.create_user(user)

    def view_profile(self):
        username = self._prompt("Enter username to view: ")
        self._db.read_user(username)

    def update_profile(self):
        username = self._prompt("Enter username to update: ")
        email = self._prompt("Enter new email: ")
        password = self._prompt("Enter new password: ")
        bio = self._prompt("Enter new bio: ")
        self._db.update_user(username, email, password, bio)

    def delete_profile(self):
        username = self._prompt("Enter username to delete: ")
        self._db.delete_user(username)

    def display_menu(self):
        print("\nUser Profile System")
        print("[1] Create User Profile")
        print("[2] View User Profile")
        print("[3] Update User Profile")
        print("[4] Delete User Profile")
        print("[5] Exit")

    def run(self):
        while True:
            self.display_menu()
            choice = self._prompt("Choose an option (1-5): ")

            actions = {
                "1": self.create_profile,
                "2": self.view_profile,
                "3": self.update_profile,
                "4": self.delete_profile,
                "5": lambda: print("👋 Goodbye!")
            }

            action = actions.get(choice)
            if action:
                if choice == "5":
                    self._db.close()
                    break
                action()
            else:
                print("❌ Invalid option. Please choose between 1 and 5.")


if __name__ == "__main__":
    database = UserDatabase()
    cli = UserCLI(database)
    cli.run()
