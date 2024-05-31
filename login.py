import json

class LoginSystem:
    def __init__(self):
        self.login_status = False

    def login(self):
        self.username = input("input your username: ")
        self.password = input("input your password:")
        print(self.username,self.password)
        with open('.\data.json', 'r') as file:
            data = json.load(file)
            # print(file)
            print(data['users'])
            print(data['users'][self.username]['password'] )
            if self.username in data and data['users'][self.username]['password'] == self.password:
                print("Login successful!")
                self.login_status = True
            else:
                print("Invalid username or password.")

login = LoginSystem()
login.login()