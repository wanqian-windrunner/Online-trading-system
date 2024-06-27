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
            return 0
        try:
            Shopping_cart.choice_number = int(Shopping_cart.choice_number)
        except :
            print('\nInvalid choice. Please try again.\n')
            Shopping_cart.add_time(userdata)
        if Shopping_cart.choice_number not in range(1,len(goods)+1):
            print('\nInvalid choice. Please try again.\n')
            Shopping_cart.add_time(userdata)
        
        Showshowway.show_detail(str(Shopping_cart.choice_number))
        print()
        while True:
            add_num = input("Please input how many you want to add (q to quit): ")
            print()
            if add_num == "q":
                return 0
            try:
                if int(add_num) <= int(goods[str(Shopping_cart.choice_number)]['count']):

                    print('\033[32mAdd Shopping Cart Successfully!\033[0m\n')
                    trade = Trade(userdata)
                    trade.cart(str(Shopping_cart.choice_number),int(add_num))
                    break
                else:
                    print('\033[33mThe quantity you selected is greater than the quantity in stock.\033[0m\n'
                        'Please try again.')
            except:
                print('\nInvalid choice. Please try again.\n')
                continue
                
