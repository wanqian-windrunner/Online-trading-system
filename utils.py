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
    for good in goods:
        print(good+'.',goods[good]['name'], ' price:',goods[good]['price'],' count:',goods[good]['count'])


if __name__ == '__main__':
    show_goods()
