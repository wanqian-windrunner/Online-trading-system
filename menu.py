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
            print("5. Logout\n")

            choice = input("Enter your choice number: ")
            print()

            if choice == "1":
                # Logic for viewing account balance
                print(f"Your account balance is ${self.balance}\n")
            elif choice == "2":
                # Logic for buying stocks
                print("Buying stocks...\n")
                self.buy_stocks_menu()
            elif choice == "3":
                print(str(self.bag)+'\n')
            elif choice == "4":
                self.sell_stocks_menu()
                # Logic for selling stocks
                print("Selling stocks...\n")
            elif choice == "5":
                self.logged_in = False
                print("Logout successful!\n")
            else:
                print("Invalid choice. Please try again.\n")




    def buy_stocks_menu(self):  #这函数是个买商品的函数

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



        elif good_number == '1':    #选择商品展示
            print('\nprice: '+str(good['1']['price'])+'$')
            print('count: '+str(good['1']['count'])+'\n')
            self.buy_time(good,good_number)
        elif good_number == '2':
            print('\nprice: '+str(good['2']['price'])+'$')
            print('count: '+str(good['2']['count'])+'\n')
            self.buy_time(good,good_number)
        elif good_number == '3':
            print('\nprice: '+str(good['3']['price'])+'$')
            print('count: '+str(good['3']['count'])+'\n')
            self.buy_time(good,good_number)
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

            good[str(good_number)]['count'] -= buy_num
            self.balance -= buy_num * good[str(good_number)]['price']  #减钱的
            the_reduce = buy_num * good[str(good_number)]['price']
            self.bag[self.change(good_number)] += buy_num   #算数量的

            print(f'OK!You cost {the_reduce}$\n')


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


    def sell_stocks_menu(self):
        good = self.goodsdata
        print('What do you want to sell?\n')
        print('1.Apple\n2.Banana\n3.Fish\n4.Back\n')

        try:
            sell_choice = int(input('Please input your choice: '))
        except:
            print('Please input a number.\n')
            self.sell_stocks_menu()

        if sell_choice == 4:
            print()
            self.function_menu()

        if sell_choice not in [1,2,3,4]:
            print('Invalid choice. Please try again.\n')


        sell_sure = input('Are you sure to sell?(y/n): ')
        print()

        if sell_sure == 'y' or sell_sure == 'Y' or sell_sure == '':
            self.sell_time(good,sell_choice)
        elif sell_sure == 'n' or sell_sure == 'N':
            self.sell_stocks_menu()
        else:
            print('Invalid choice. Please try again.\n')
            self.sell_stocks_menu()

    def sell_time(self,good,sell_choice):   #卖的时候出来的东西
        have_number = self.bag[self.change(sell_choice)]
        print(f'You have {have_number} {self.change(sell_choice)} in your bag.')
        try:
            sell_num = int(input('\nPlease input how many you want to sell and input 0 to exit.\n'))
        except:
            print('Please input a number.\n')
            self.sell_time(good,sell_choice)
        if sell_num == 0:
            self.sell_stocks_menu()

        if sell_num > int(self.bag[self.change(sell_choice)]):
            print("You don't have enough.\n")
            self.sell_time(good,sell_choice)

        good[str(sell_choice)]['count'] += sell_num
        self.balance += sell_num * good[str(sell_choice)]['price']
        the_rise = sell_num * good[str(sell_choice)]['price']
        self.bag[self.change(sell_choice)] -= sell_num

        print(f'OK!You get {the_rise}$\n')

        input('Press Enter to continue...\n')
        self.sell_stocks_menu()



if __name__ == '__main__':
    a = Menu(True)
    a.function_menu()

