class User:
    users_list = []

    def __init__(self, username, password):
        self.username = username
        self.password = password

    def save_user(self):
        User.users_list.append(self)



class Credentials:
    accounts_list = []
    def __init__(self, account_name, user_name, pass):
        self.account_name = account_name
        self.user_name = user_name
        self.pass = pass
