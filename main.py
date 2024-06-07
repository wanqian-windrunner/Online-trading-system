from time import sleep
from menu import Menu
from login import LoginSystem

loginsystem=LoginSystem()
# 登陆账户，然后存储用户数据
while not loginsystem.login_status:
    option = input("Choose your option:\n\t1.register\n\t2.login\n")
    if option == '1':    
        loginsystem.register()
    elif option == '2':
        loginsystem.login()
    # sleep(2)
userdata = loginsystem.userdata

print(userdata)
# sleep(2)
# 然后展示菜单

from menu import Menu
menusystem = Menu(loginsystem.login_status,userdata)
menusystem.function_menu()
