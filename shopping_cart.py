import json
from utils import Data_process, show_goods


class Shopping_cart:
    def __init__(self, userdata):
        self.balance = userdata['balance']
        self.goodsdata = Data_process.read()['goods']
        self.shopping_cart = userdata['shopping_cart']  # userdata需要更改

    def choose_stocks(self, good_number):  # 选择商品
        while self.logged_in:
            show_goods()
            print()
            choice = input('Please enter your choice: ')
            print()
            if choice == self.goodsdata[str(good_number)]:
                print(self.goodsdata[str(good_number)]['name'],
                      self.goodsdata[str(good_number)]['price'], sep="\n")
                print()
                self.add_time(self.goodsdata,good_number)
            else:
                print('Invalid choice. Please try again.\n')
                self.choose_stocks(self)

    def add_time(self, good, good_number):  # 加入个数
        good_number = int(good_number)
        print("1.Add to shopping cart")
        print("2.Back\n")
        add_choice = input("Please input your choice: ")
        print()
        if add_choice == '1':
            add_num = int(input("\nPlease input how many you want to add: "))
            if add_num > int(good[str(good_number)]['count']):
                print('The quantity you selected is greater than the quantity in stock.\n'
                      'The maximum quantity ' + good[str(good_number)]['count'] +
                      'has been added for you')
                add_num = int(good[str(good_number)]['count'])
            else:
                print('Add Shopping Cart Successfully!\n')

            # 更改 userdata['shopping_cart']

        elif add_choice == '2':
            self.choose_stocks(good_number)

        else:
            print('Invalid choice. Please try again.\n')
            self.add_time(self.goodsdata,good_number)
