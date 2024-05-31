class Menu:
    def __init__(self):
        self.logged_in = False

    def login_menu(self):
        while not self.logged_in:
            username = input("Enter your username: ").strip()
            password = input("Enter your password: ").strip()

            # Perform login validation logic here
            # For example, check if the username and password are correct

            if username == "admin" and password == "password":
                self.logged_in = True
                print("Login successful!")
            else:
                print("Invalid username or password. Please try again.")

    def function_menu(self):
        while self.logged_in:
            print("1. View account balance")
            print("2. Buy stocks")
            print("3. Sell stocks")
            print("4. Logout")

            choice = input("Enter your choice: ")

            if choice == "1":
                # Logic for viewing account balance
                print("Your account balance is $1000")
            elif choice == "2":
                # Logic for buying stocks
                print("Buying stocks...")
            elif choice == "3":
                # Logic for selling stocks
                print("Selling stocks...")
            elif choice == "4":
                self.logged_in = False
                print("Logout successful!")
            else:
                print("Invalid choice. Please try again.")

