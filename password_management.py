class PasswordManager:
    def __init__(self):
        self.passwords = {}

    def add_password(self, username, password):
        if username in self.passwords:
            print("Username already exists. Please choose another username.")
        else:
            self.passwords[username] = password
            print("Password added successfully.")

    def get_password(self, username):
        if username in self.passwords:
            return self.passwords[username]
        else:
            print("Username not found.")
            return None

    def delete_password(self, username):
        if username in self.passwords:
            del self.passwords[username]
            print("Password deleted successfully.")
        else:
            print("Username not found.")

if __name__ == "__main__":
    manager = PasswordManager()

    while True:
        print("\nPassword Management System")
        print("1. Add Password")
        print("2. Get Password")
        print("3. Delete Password")
        print("4. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            username = input("Enter username: ")
            password = input("Enter password: ")
            manager.add_password(username, password)
        elif choice == '2':
            username = input("Enter username: ")
            password = manager.get_password(username)
            if password:
                print("Password:", password)
        elif choice == '3':
            username = input("Enter username: ")
            manager.delete_password(username)
        elif choice == '4':
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please choose a valid option.")
