from utils import Data_process

class Trade:
    def __init__(self,user_data):
        self.user_data = user_data

    def purchase(self,good_id:str,quantity:int):
        self.goods_data = Data_process.read()['goods']
        # 添加到背包
        self.user_data["bag"][good_id] += quantity
        # 扣除钱包余额
        self.user_data["balance"] -= self.goods_data[good_id]["price"]*quantity
        # 减少商品
        self.goods_data[good_id]["count"] -= quantity

        # 写入json文件
        total_data = Data_process.read()
        total_data['users'][self.user_data['name']]=self.user_data
        total_data['goods']=self.goods_data
        Data_process.write(total_data)
    
    def cart(self,good_id:str,quantity:int):
        self.goods_data = Data_process.read()['goods']
        # 添加到购物车
        self.user_data["cart"][good_id] += quantity
        # 减少商品
        self.goods_data[good_id]["count"] -= quantity

        # 写入json文件
        total_data = Data_process.read()
        total_data['users'][self.user_data['name']]=self.user_data
        total_data['goods']=self.goods_data
        Data_process.write(total_data)

    def sell(self,good_id:str,quantity:int):
        self.goods_data = Data_process.read()['goods']
        # 从背包拿出
        self.user_data["bag"][good_id] -= quantity
        # 增加钱包余额
        self.user_data["balance"] += self.goods_data[good_id]["price"]*quantity//2
        # 增加商品
        self.goods_data[good_id]["count"] += quantity

        # 写入json文件
        total_data = Data_process.read()
        total_data['users'][self.user_data['name']]=self.user_data
        total_data['goods']=self.goods_data
        Data_process.write(total_data)
