import random
import string
class User:
    users_list = []
    """
    Args:
    username = new username
    password = new password
    """

    def __init__(self, username, password):
        self.username = username
        self.password = password

    def save_user(self):
        User.users_list.append(self)
    @classmethod
    def display_users(cls):
        '''
        method that returns the accounts list
        '''
        return cls.users_list




class Credentials:
    accounts_list = []
    """
    Args:
    account_name = new account_name
    user_name = new user_name
    key = new password
    """
    def __init__(self, account_name, user_name, key):
        self.account_name = account_name
        self.user_name = user_name
        self.key = key

    def save_account(self):
        Credentials.accounts_list.append(self)

    def generate_password(num):
        gen_pass = ""
        num = 8

        for n in range(num):
            x = random.randint(10,34)
            gen_pass += string.printable[x]
        return gen_pass

    @classmethod
    def display_accounts(cls):
        '''
        method that returns the accounts list
        '''
        return cls.accounts_list
