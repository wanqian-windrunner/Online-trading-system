# from menu import Menu
# from login import LoginSystem
# from utils import Data_process
#
# Data_process.data_init()
# loginsystem=LoginSystem()
# # 登陆账户，然后存储用户数据
# while not loginsystem.login_status:
#     option = input("Choose your option:\n\t1.register\n\t2.login\n")
#     if option == '1':
#         loginsystem.register()
#     elif option == '2':
#         loginsystem.login()
#
# userdata = loginsystem.userdata
#
# print(userdata)
#
# # 然后展示菜单
#
# from menu import Menu
# menusystem = Menu(loginsystem.login_status,userdata)
# menusystem.function_menu()


from login import LoginSystem
from utils import Data_process

# 初始化数据
Data_process.data_init()

# 创建登录系统实例
loginsystem = LoginSystem()

# 登陆账户，然后存储用户数据
while not loginsystem.login_status:
    option = input("Choose your option:\n\t1.register\n\t2.login\n")
    if option == '1':
        loginsystem.register()
    elif option == '2':
        loginsystem.login()

# 获取用户数据
userdata = loginsystem.userdata
print(userdata)

# 延迟导入Menu类
from menu import Menu

# 展示菜单
menusystem = Menu(loginsystem.login_status, userdata)
menusystem.function_menu()


