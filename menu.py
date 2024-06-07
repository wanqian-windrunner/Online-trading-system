import json
from utils import Data_process

class Menu:
    def __init__(self,status,userdata):
        self.logged_in = status
        self.balance = userdata['balance']
        self.goodsdata = Data_process.read()['goods']
        self.bag = userdata['bag']

    def function_menu(self):

        while self.logged_in:
            print("1. View account balance")
            print("2. Buy stocks")
            print("3. Bag")
            print("4. Sell stocks")
            print("5. Logout")

            choice = input("Enter your choice number: ")
            print()

            if choice == "1":
                # Logic for viewing account balance
                print(f"Your account balance is ${self.balance}")
            elif choice == "2":
                # Logic for buying stocks
                print("Buying stocks...\n")
                self.buy_stocks_menu()
            elif choice == "3":
                print(str(self.bag)+'\n')
            elif choice == "4":
                # Logic for selling stocks
                print("Selling stocks...\n")
            elif choice == "5":
                self.logged_in = False
                print("Logout successful!\n")
            else:
                print("Invalid choice. Please try again.\n")




    def buy_stocks_menu(self):

        good = self.goodsdata
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
            self.buy_time(good,good_number)
        elif good_number == '2':
            print('\nprice: '+str(good['2']['price'])+'$')
            print('count: '+str(good['2']['count'])+'\n')
            self.buy_time(good,good_number)
        elif good_number == '3':
            print('\nprice: '+str(good['3']['price']+'$'))
            print('count: '+str(good['3']['count'])+'\n')
            self.buy_time()
        elif good_number == '4':
            print()
            self.function_menu()

    def buy_time(self,good,good_number):
        good_number = int(good_number)
        print('1.Buy')
        print('2.Back\n')
        buy_choice = input('Please input your choice: ')
        print()
        if buy_choice == '1':
            buy_num = int(input('\nPlease input how many you want to buy: '))
            if buy_num > int(good[str(good_number)]['count']):
                print('Too many!\n')
                self.buy_time(good,good_number)
            print('OK!')

            good[str(good_number)]['count'] -= buy_num
            self.balance -= buy_num * good[str(good_number)]['price']  #减钱的
            self.bag[self.change(good_number)] += buy_num   #算数量的

            input('Press Enter to continue...\n')
            self.buy_stocks_menu()
        elif buy_choice == '2':
            self.buy_stocks_menu()
        else:
            print('Invalid choice. Please try again.\n')


    def change(self,good_number):   #这个函数是把数字编号换成商品的
        if good_number == 1:
            return 'Apple'
        elif good_number == 2:
            return 'Banana'
        elif good_number == 3:
            return 'Fish'



if __name__ == '__main__':
    a = Menu(True)
    a.function_menu()

