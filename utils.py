import json

class Data_process:
    def data_init():
        goods_len=len(Data_process.read()['goods'])
        data = Data_process.read()
        for user in data['users']:
            for i in range(goods_len):
                if not data['users'][user]['bag'].get(str(i+1)):
                    data['users'][user]['bag'][str(i+1)] = 0
        Data_process.write(data)


    def read():
        with open('data.json', 'r') as file:
            data = json.load(file)
        return data
    def write(data):
        with open('data.json', 'w') as file:
            json.dump(data, file, indent=2)

def show_goods():
    goods = Data_process.read()['goods']
    max_len = max([len(goods[good]['name']) for good in goods])
    # print(max_len)
    for good in goods:
        print(good,'.',goods[good]['name'].ljust(max_len,' '), '  price: ',goods[good]['price'],'$ count: ',goods[good]['count'],sep='')


if __name__ == '__main__':
    show_goods()
