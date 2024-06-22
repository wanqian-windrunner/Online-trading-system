import json
from utils import Data_process

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
        
        # 判断用户名和密码是否正确，正确则存储数据，否则提示错误
        if self.username in self.user_data and self.user_data[self.username]['password'] == self.password:
            print("登录成功！欢迎, " + self.username + "!")
            # 存储用户数据
            self.userdata = self.user_data[self.username]
            self.login_status = True
        else:
            print("无效的用户名或密码。")

    def register(self):
        # 输入新用户名
        self.username = input("请输入您的用户名: ")
        # 检查用户名是否已存在
        if self.username in self.user_data:
            print("用户名已存在！请尝试一个新名字或登录。")
            return 0
        # 输入密码
        self.password = input("请输入您的密码: ")  
        # 确认密码是否一致
        if input("请再次输入您的密码: ") != self.password:
            print('抱歉，再见~')
            return 0
        # 输入余额
        self.balance = input("请输入您的余额: ")
        # 创建用户数据字典
        self.userdata = {
            'name': self.username,
            'password': self.password,
            'balance': self.balance,
            'bag': []
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
