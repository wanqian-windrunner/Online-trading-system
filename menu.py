import json
from utils import Data_process

class Menu:
    def __init__(self,status,userdata):
        self.logged_in = status
        self.balance = userdata['balance']
        self.goodsdata = Data_process.read()['goods']
        self.bag = userdata['bag']

    def f_m(self):
        while self.logged_in:
            print('1.balance\n2.buy\n3.bag\n4.sell\n5.logout\n')
            choice = input('Enter your choice: ')
            print()
            if choice == "1":
                print(f"Your account balance is ${self.balance}\n")
            elif choice == "2":
                self.bbbbuy()
            elif choice == "3":
                2
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
        goods = Data_process.read()['goods']
        max_len = max([len(goods[good]['name']) for good in goods])
        for good in goods:
            print(good, '.', goods[good]['name'].ljust(max_len, ' '), '  price: ', goods[good]['price'], '$ count: ',
                  goods[good]['count'], sep='')
        g_n = input('\nEnter your choice(input q to quit):\n')
        if g_n == 'q':
            print()
            self.f_m()
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
            self.f_m()
            return
        try:
            buy_num = int(buy_num)
        except:
            print('\nNO\n')
            self.bbbbuy()
        if buy_num > int(goods[str(g_n)]['count']):
            print('\nToo many!\n')
            self.bbbbuy()
#——————————————————————————————————————————————————————————————————————————————————————————————————————————————

        goods[str(g_n)]['count'] -= buy_num          #这一行不生效
        self.balance -= buy_num * goods[str(g_n)]['price']
        reduce = buy_num * goods[str(g_n)]['price']
                                                    #这里需要计算bag
#——————————————————————————————————————————————————————————————————————————————————————————————————————————————
        print(f'OK!You cost {reduce}$\n')
        input('Press Enter to continue...\n')
        self.bbbbuy()


    def sellsellsell(self):


























if __name__ == '__main__':
    userdata = {'name': 'user1', 'password': 'password1', 'balance': 1000, 'bag': {'Apple': 0, 'Banana': 0, 'Fish': 0}}
    a = Menu(True,userdata)
    a.f_m()
