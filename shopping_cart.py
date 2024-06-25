import json
from utils import Data_process, Showshowway


class Shopping_cart:
    def __init__(self, userdata):
        self.goods_data = Data_process.read()['goods']
        self.shopping_cart = userdata['cart']  # userdata需要更改
        self.show_goods = Showshowway
        self.goods_count = userdata.read()['count']

    def add_time(self,g_n,goods):  # 加入个数
        while True:     # 即在menu中选择加入购物车
            print("1.Add to shopping cart")
            print("2.Back\n")
            add_choice = input("Please input your choice: ")
            print()
            if add_choice == '1':
                while 1:
                    add_num = int(input("\nPlease input how many you want to add: "))
                    if add_num > int(goods[str(g_n)]['count']):
                        print('The quantity you selected is greater than the quantity in stock.\n'
                              'Please try again.')
                    else:
                        print('Add Shopping Cart Successfully!\n')
                        #   self.shopping_cart()
                        break   # 更改 userdata['shopping_cart']
            elif add_choice == '2':
                    # back to menu
                break

            else:
                print('Invalid choice. Please try again.\n')
