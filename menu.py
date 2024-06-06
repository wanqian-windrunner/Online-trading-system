import json
class Menu:
    def __init__(self):
        self.logged_in = True



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
            print("3. Bag")
            print("4. Sell stocks")
            print("5. Logout")

            choice = input("Enter your choice: ")

            if choice == "1":
                # Logic for viewing account balance
                print("Your account balance is $1000\n")
            elif choice == "2":
                # Logic for buying stocks
                print("Buying stocks...\n")
                self.buy_stocks_menu()
            elif choice == "3":
                print('no bag\n')
            elif choice == "4":
                # Logic for selling stocks
                print("Selling stocks...\n")
            elif choice == "5":
                self.logged_in = False
                print("Logout successful!\n")
            else:
                print("Invalid choice. Please try again.\n")




    def buy_stocks_menu(self):

        with open('.\data.json', 'r') as file:
            good_data = json.load(file)
        good = good_data["goods"]
        print('1.'+good['1']['name'])
        print('2.'+good['2']['name'])
        print('3.'+good['3']['name'])
        print('4.Back')
        print()
        good_number = input('\nPlease input your choice: ')

        if good_number not in '1' and good_number not in '2' and good_number not in '3' and good_number not in '4':
            print("Invalid choice. Please try again.\n")
            self.buy_stocks_menu()

# 这下面的每个选项都需要一个背包函数把东西放进去

        elif good_number == '1':
            print('\nprice: '+str(good['1']['price'])+'$')
            print('count: '+str(good['1']['count'])+'\n')
            self.buy_time()
        elif good_number == '2':
            print('\nprice: '+str(good['2']['price'])+'$')
            print('count: '+str(good['2']['count'])+'\n')
            self.buy_time()
        elif good_number == '3':
            print('\nprice: '+str(good['3']['price']+'$'))
            print('count: '+str(good['3']['count'])+'\n')
            self.buy_time()
        elif good_number == '4':
            print()
            self.function_menu()

    def buy_time(self):
        print('1.Buy')
        print('2.Back\n')
        buy_choice = input('Please input your choice: ')
        print()
        if buy_choice == '1':
            buy_num = input('\nPlease input how many you want to buy: ')
            #背包未实装，故不写接下来的减法
            print('OK!')
            input('Press Enter to continue...\n')
            self.buy_stocks_menu()
        elif buy_choice == '2':
            self.buy_stocks_menu()
        else:
            print('Invalid choice. Please try again.\n')
