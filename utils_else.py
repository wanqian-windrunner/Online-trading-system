# 对本交易系统使用体验的评价，在登出前执行
import json

class Data_process:
    def __init__(self):
        # 读取所有数据
        self.all_data = Data_porcess.read()
        # 读取用户数据
    def read():
        with open('evaluation.json','r') as file:
            data = json.load(file)
        return data
    def write(data):
        with open('evaluation.json','w') as file:
            json.dump(data,file,indent=2)

