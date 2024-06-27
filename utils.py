import json
import random

class Data_process:
    def data_init():
        goods_len=len(Data_process.read()['goods'])
        data = Data_process.read()
        for user in data['users']:
            for i in range(goods_len):
                if not data['users'][user]['bag'].get(str(i+1)):
                    data['users'][user]['bag'][str(i+1)] = 0

        for user in data['users']:
            for i in range(goods_len):
                if not data['users'][user]['cart'].get(str(i+1)):
                    data['users'][user]['cart'][str(i+1)] = 0
        Data_process.write(data)


    def read():
        with open('data.json', 'r') as file:
            data = json.load(file)
        return data
    def write(data):
        with open('data.json', 'w') as file:
            json.dump(data, file, indent=2)


class Showshowway:
    def show_goods():
        goods = Data_process.read()['goods']
        max_len = max([len(goods[good]['name']) for good in goods])
        # print(max_len)
        for good in goods:
            print(good,'.',goods[good]['name'])

    def show_detail(good_id:str):
        goods = Data_process.read()['goods']
        print(good_id,'.',goods[good_id]['name'], '\n    price: ',goods[good_id]['price'],'$\n    count: ',goods[good_id]['count'],'\n    comment: ',random.randint(1, 5)*'*',sep='')


    def show_bag(user_data):
        goods = Data_process.read()['goods']
        max_len = max([len(goods[good]['name']) for good in goods])
        # print(max_len)
        for user_good in user_data['bag']:
            print(f'{user_good}     ',goods[user_good]['name'].ljust(max_len,' '), '  count: ',user_data['bag'][user_good],sep='')

    def show_bag(user_data):
        goods = Data_process.read()['goods']
        max_len = max([len(goods[good]['name']) for good in goods])
        # print(max_len)
        for user_good in user_data['cart']:
            print(f'{user_good}     ',goods[user_good]['name'].ljust(max_len,' '), '  count: ',user_data['cart'][user_good],sep='')    


if __name__ == '__main__':
    a = Showshowway()
    a.show_goods()
    a.show_detail()
