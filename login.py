import json

class LoginSystem:
    def __init__(self):
        self.login_status = False

    def login(self):
        self.username = input("input your username: ")
        self.password = input("input your password:")
        # print(self.username,self.password)
        with open('.\data.json', 'r') as file:
            data = json.load(file)
        user_data = data['users']
        print(user_data[self.username]['password'] )
        print(self.password)
        print(type(user_data[self.username]['password']))
        if self.username in user_data and user_data[self.username]['password'] == self.password:
            print("Login successful!")
            self.login_status = True
        else:
            print("Invalid username or password.")


if __name__ == '__main__':
    login = LoginSystem()
    login.login()
    