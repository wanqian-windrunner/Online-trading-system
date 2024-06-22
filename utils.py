import json

class Data_process:
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
    print(max_len)
    for good in goods:
        print(good,'.',goods[good]['name'].ljust(max_len,' '), '  price: ',goods[good]['price'],'$ count: ',goods[good]['count'],sep='')


if __name__ == '__main__':
    show_goods()
