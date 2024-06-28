from menu import Menu
from login import LoginSystem
from utils import Data_process
from evaluatate import Evaluate_system 


loginsystem=LoginSystem()
# 登陆账户，然后存储用户数据
while not loginsystem.login_status:
    option = input("Choose your option:\n\t1.register\n\t2.login\n")
    if option == '1':
        loginsystem.register()
    elif option == '2':
        loginsystem.login()

Data_process.data_init()
userdata = Data_process.read()['users'][loginsystem.username]

# print(userdata)


menusystem = Menu(loginsystem.login_status,userdata)
menusystem.function_menu()

evalutatesystem = Evaluate_system(userdata['name'])
evalutatesystem.score()
evalutatesystem.comment()
evalutatesystem.submit()
evalutatesystem.show_stars()

# 