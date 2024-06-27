import json
import utils
from utils import Data_process , Showshowway
from trade import Trade
from shopping_cart import Shopping_cart

class Menu:
    def __init__(self,status,userdata):
        self.logged_in = status
        self.balance = userdata['balance']
        self.goodsdata = Data_process.read()['goods']
        self.bag = userdata['bag']
        self.userdata = userdata

#——————————————————————————————————————————————————————————————————————————————————————————————————————————————

    def function_menu(self):   # 先展示菜单栏，选择商品id之后显示detail，选择对应操作
        while self.logged_in:
                print('——————————————————————\n1.balance\n2.buy\n3.bag\n4.sell\n5.add in shopping cart\n6.logout\n——————————————————————')
                choice = input('Enter your choice: ')
                print()
                if choice == "1":
                    print(f"\033[34mYour account balance is ${self.balance}\033[0m\n")
                elif choice == "2":
                    self.bbbbuy()
                elif choice == "3":
                    Showshowway.show_bag(self.userdata)
                    print()
                elif choice == "4":
                    self.sellsellsell()
                elif choice == "5":
                    Shopping_cart.add_time(self.userdata)
                elif choice == "6":
                    self.logged_in = False
                    print("\033[34mLogout\033[0m\n")
                    exit(0)
                else:
                    print("\nNO\n")
#——————————————————————————————————————————————————————————————————————————————————————————————————————————————


    #这里是购买
    def bbbbuy(self):
        goods = Data_process.read()['goods']
        utils.Showshowway.show_goods()
        print()
        g_n = input("Input which you want to buy?(q to quit):\n")
        if g_n == 'q':
            print()
            self.function_menu()
            return
        try:
            g_n = int(g_n)
        except :
            print('\n\033[31mwhat\033[0m\n')
            self.bbbbuy()
        if g_n not in range(1,len(goods)+1):
            print('\n\033[31mNO\n')
            self.bbbbuy()
            return

        Showshowway.show_detail(str(g_n))



        self.maisuan(g_n,goods)
#return用于解决完成一个代码后仍然继续下面的内容
#——————————————————————————————————————————————————————————————————————————————————————————————————————————————



    def maisuan(self,g_n,goods):
        buy_num = input('\nPlease input how many you want to buy(q to quit):\n')
        if buy_num == 'q':
            print()
            self.function_menu()
            return
        try:
            buy_num = int(buy_num)
        except:
            print('\nNO\n')
            self.bbbbuy()
        if buy_num > int(goods[str(g_n)]['count']):
            print('\n\033[31mToo many!\033[0m\n')
            self.bbbbuy()

        trade = Trade(self.userdata)
        trade.purchase(str(g_n),buy_num)
        reduce = buy_num * goods[str(g_n)]['price']


        print(f'\033[34mOK!You cost {reduce}$\033[0m\n')
        input('Press Enter to continue...\n')
        self.bbbbuy()


    def sellsellsell(self):
        Showshowway.show_bag(self.userdata)
        print()
        sell_choice = input('Please input which one to sell(q to quit):\n')
        if sell_choice == 'q':
            self.function_menu()
            return
        try:
            sell_choice = int(sell_choice)
        except:
            print('Please input a number\n')
            self.sellsellsell()
            return

        self.sell_time(sell_choice)


    def sell_time(self,sell_choice):
        goods = Data_process.read()['goods']
        sell_number = input(f"\nInput how many you want to sell(you have {self.bag[str(sell_choice)]},q to quit):\n")
        if sell_number == 'q':
            self.sellsellsell()
            return
        try:
            sell_number = int(sell_number)
        except:
            print('\n\033[31mA number,please\033[0m')
            self.sellsellsell()
            return
        if sell_number > self.bag[str(sell_choice)]:
            print('\n\033[31mWhat? HOW MANY?? U like zt\033[0m')
            self.sell_time(sell_choice)
            return

        trade = Trade(userdata)
        trade.sell(str(sell_choice),sell_number)
        increase = sell_number * goods[str(sell_choice)]['price']

        print(f'\033[34mOK!You get {increase}$\033[0m\n')
        input('Press Enter to continue...\n')

        self.sellsellsell()


if __name__ == '__main__':
    userdata = {
      "name": "user1",
      "password": "0b14d501a594442a01c6859541bcb3e8164d183d32937b851835442f69d5c94e",
      "balance": 999,
      "bag": {
        "1": 1,
        "2": 0,
        "3": 0,
        "4": 0,
        "5": 0,
        "6": 0,
        "7": 0,
        "8": 0
      },
      "cart": {
        "1": 2,
        "2": 2,
        "3": 0,
        "4": 0,
        "5": 0,
        "6": 0
      }
    }
    a = Menu(True,userdata)
    a.function_menu()
    # Showshowway.show_bag(userdata)

