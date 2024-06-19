import json
from utils import Data_process

class LoginSystem:
    def __init__(self):
        self.login_status = False
        self.totaldata = Data_process.read()
        self.user_data = self.totaldata['users']

    def login(self):
        # 先是输入用户名和密码
        self.username = input("input your username: ")
        self.password = input("input your password:")
        # print(self.username,self.password)
        
        # 然后判断用户名和密码是否正确，正确则存储数据，否则提示错误
        if self.username in self.user_data and self.user_data[self.username]['password'] == self.password:
            print("Login successful!Welcome, "+self.username+"!")
            self.userdata = self.user_data[self.username]
            self.login_status = True
        else:
            print("Invalid username or password.")
    def register(self):
        self.username = input("Input your username: ")
        if self.username in self.user_data:
            print("Repeated name!Try a new name or login.")
            return 0
        self.password = input("Input your password:")  
        if input("Please input your password again:") != self.password:
            print('Sorry,goodbye~')
            return 0
        self.balance = input("Input your balance:")
        self.userdata={'name':self.username,
                        'password':self.password,
                        'balance':self.balance,
                        'bag':[]}
        self.totaldata['users'][self.username]=self.userdata
        Data_process.write(self.totaldata)
        self.login_status = True
        
    def logout(self):
        exit(0)


if __name__ == '__main__':
    login = LoginSystem()
    login.login()
    print(login.userdata)
    