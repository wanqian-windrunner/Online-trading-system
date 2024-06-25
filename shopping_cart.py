import json
from utils import Data_process, Showshowway
from trade import Trade


class Shopping_cart:
    choice_number = None
    def __init__(self, userdata):
        self.goods_data = Data_process.read()['goods']
        self.shopping_cart = userdata['cart']
        self.goods_count = userdata.read()['count']


    def add_time(userdata):  # 加入个数
        goods = Data_process.read()['goods']
        Showshowway.show_goods()
        print()
        Shopping_cart.choice_number = input("Input which you want to add in?(q to quit):")
        if Shopping_cart.choice_number == 'q':
            print()
            Shopping_cart.add_time(userdata)
            return
        try:
            Shopping_cart.choice_number = int(Shopping_cart.choice_number)
        except :
            print('\nwhat\n')
            Shopping_cart.add_time(userdata)
        if Shopping_cart.choice_number not in range(1,len(goods)+1):
            print('\nNO\n')
            Shopping_cart.add_time(userdata)
            return
        
        Showshowway.show_detail(str(Shopping_cart.choice_number))
        print()
        while True:
            add_num = int(input("Please input how many you want to add:(q to quit)"))
            print()
            if add_num > int(goods[str(Shopping_cart.choice_number)]['count']):
                print('The quantity you selected is greater than the quantity in stock.\n'
                    'Please try again.')
            else:
                print('Add Shopping Cart Successfully!\n')
                trade = Trade(userdata)
                trade.cart(str(Shopping_cart.choice_number),add_num)
                break

from menu import Menu