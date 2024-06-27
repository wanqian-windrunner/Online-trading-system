import json
from utils import Data_process
import hashlib
import random

class LoginSystem:
    def __init__(self):
        self.login_status = False
        # 读取所有数据
        self.totaldata = Data_process.read()
        # 提取用户数据
        self.user_data = self.totaldata['users']

    def login(self):
        # 输入用户名和密码
        self.username = input("请输入您的用户名: ")
        self.password = input("请输入您的密码: ")
        # 打印输入的用户名和密码 (用于调试)
        # print(self.username, self.password)
        
        # 判断用户名和密码是否正确，正确则存储数据，否则提示错误，为了保证密码安全，我们使用hashlib库对密码进行加密
        if self.username in self.user_data and self.user_data[self.username]['password'] == hashlib.sha256(self.password.encode()).hexdigest():
            print("\033[32m登录成功！欢迎, \033[0m" + self.username + "\033[32m!\033[0m")
            # 存储用户数据
            self.userdata = self.user_data[self.username]
            self.login_status = True
        else:
            print("\033[31m无效的用户名或密码。\033[0m")

    def register(self):
        # 输入新用户名
        self.username = input("请输入您的用户名: ")
        # 检查用户名是否已存在
        if self.username in self.user_data:
            print("\033[34m用户名已存在！请尝试一个新名字或登录。\033[0m")
            return 0
        # 输入密码
        self.password = input("请输入您的密码: ")  
        # 确认密码是否一致
        if input("请再次输入您的密码: ") != self.password:
            print('\033[31m抱歉，再见~\033[0m')
            return 0
        # 输入余额
        # self.balance = input("请输入您的余额: ")
        # 创建用户数据字典
        self.userdata = {
            'name': self.username,
            'password': hashlib.sha256(self.password.encode()).hexdigest(),
            'balance': 1000,
            'bag': {},
            'cart':{}
        }
        # 将新用户数据添加到总数据中
        self.totaldata['users'][self.username] = self.userdata
        # 将总数据写回文件
        Data_process.write(self.totaldata)
        self.login_status = True
        
    def logout(self):
        # 退出程序
        exit(0)

if __name__ == '__main__':
    # 创建登录系统实例
    login = LoginSystem()
    # 执行登录
    login.login()
    # 打印用户数据 (用于调试)
    print(login.userdata)
