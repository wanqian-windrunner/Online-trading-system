import json
from utils import Data_process , Showshowway
from trade import Trade

class Menu:
    def __init__(self,status,userdata):
        self.logged_in = status
        self.balance = userdata['balance']
        self.goodsdata = Data_process.read()['goods']
        self.bag = userdata['bag']

#——————————————————————————————————————————————————————————————————————————————————————————————————————————————
    def function_menu(self,userdata):
        while self.logged_in:
            print('1.balance\n2.buy\n3.bag\n4.sell\n5.logout\n')
            choice = input('Enter your choice: ')
            print()
            if choice == "1":
                print(f"Your account balance is ${self.balance}\n")
            elif choice == "2":
                self.bbbbuy()
            elif choice == "3":
                Showshowway.show_bag(userdata)
                print()
            elif choice == "4":
                self.sellsellsell()
            elif choice == "5":
                self.logged_in = False
                print("Logout\n")
                exit(0)
            else:
                print("\nNO\n")

#——————————————————————————————————————————————————————————————————————————————————————————————————————————————


    #这里是购买
    def bbbbuy(self):
        Showshowway.show_goods()
        goods = Data_process.read()['goods']
        g_n = input('\nEnter your choice(input q to quit):\n')
        if g_n == 'q':
            print()
            self.function_menu()
            return
        try:
            g_n = int(g_n)
        except :
            print('\nwhat\n')
            self.bbbbuy()
        if g_n not in range(1,len(goods)+1):
            print('\nNO\n')
            self.bbbbuy()
            return
        

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
            print('\nToo many!\n')
            self.bbbbuy()

        trade = Trade(userdata)
        trade.purchase(str(g_n),buy_num)
        reduce = buy_num * goods[str(g_n)]['price']


        print(f'OK!You cost {reduce}$\n')
        input('Press Enter to continue...\n')
        self.bbbbuy()


    def sellsellsell(self,userdata):
        Showshowway.show_bag(userdata)
        print()
        sell_choice = input('Please input which one to sell(q to quit):\n')
        if sell_choice == 'q':
            self.function_menu(userdata)
            return
        try:
            sell_choice = int(sell_choice)
        except:
            print('Please input a number')
            self.sellsellsell()
            return

        self.sell_time(sell_choice)


    def sell_time(self,sell_choice):
        goods = Data_process.read()['goods']
        sell_number = input(f"\nInput how many you want to sell(you have {self.bag[str(sell_choice)]},q to quit):\n")
        if sell_number == 'q':
            self.sellsellsell(userdata)
            return
        try:
            sell_number = int(sell_number)
        except:
            print('\nA number,please')
            self.sellsellsell()
            return
        if sell_number > self.bag[str(sell_choice)]:
            print('\nWhat? HOW MANY?? U like zt')
            self.sell_time(sell_choice)
            return

        trade = Trade(userdata)
        trade.sell(str(sell_choice),sell_number)
        increase = sell_number * goods[str(sell_choice)]['price']

        print(f'OK!You get {increase}$\n')
        input('Press Enter to continue...\n')

        self.sellsellsell(userdata)















if __name__ == '__main__':
    userdata = {'name': 'user1', 'password': 'password1', 'balance': 1000, 'bag': {'1': 0, '2': 0, '3': 0}}
    a = Menu(True,userdata)
    a.function_menu(userdata)
    # Showshowway.show_bag(userdata)
