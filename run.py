#!/usr/bin/env python3.7
from passwordLocker import User
from passwordLocker import Credentials
import string, random

def create_user(username,password):
    '''
    Function to create a new contact
    '''
    new_user = User(username,password)
    return new_user

def save_user(new_user):
    '''
    Function to save user
    '''
    new_user.save_user()

def create_account(account_name, user_name, key):
    '''
    Function to create a new account
    '''
    new_account = Credentials(account_name, user_name, key)
    return new_account

def save_account(new_account):
    '''
    Function to save an account
    '''
    new_account.save_account()

def generate_password():
	'''
	Function to generate a password automatically
	'''
	gen_pass = Credentials.generate_password(8)
	return gen_pass


def display_accounts():
    '''
    Function that returns all the saved accounts
    '''
    return Credentials.display_accounts()
def main():

    print("Hello Welcome to Password-Locker.Enter a username: ")
    username = input()
    print("Enter a password: ")
    password = input()
    save_user(create_user(username,password))
    print ('\n')
    print(f"New Locker account: {username} created")
    print('\n')

    while True:
        print("Enter 'ok' to continue or 'exit' to exit app:")
        proceed = input().lower().strip()

        if proceed == 'exit':
            print("Exited account")
            break
        elif proceed == 'ok':
            print(f"Hello {username}. what would you like to do?")
            print('\n')

            while True:
                    print("Use these short codes : new - Create new Credentials, disp - Display all accounts, ex -Exit the credentials list ")

                    short_code = input().lower().strip()

                    if short_code == 'new':
                            print("New Account")
                            print("-"*10)

                            print ("Enter Account name ....")
                            account_name = input()

                            print("Enter Username ...")
                            user_name = input()
                            while True:
                                print("Use 'create' keyword for existing password or use 'generate' to get random password...")
                                ke = input().lower().strip()
                                if ke == 'generate':
                                    key = generate_password()
                                    print(f"Your password for {account_name} is {key}")
                                    break
                                elif ke == 'create':
                                    print("Enter a prefered password:")
                                    key = input()
                                    break
                                else:
                                    print("Oops! Please use a correct keyword('create' or 'generate')")
                            save_account(create_account(account_name, user_name, key))

                    elif short_code == 'disp':

                            if display_accounts():
                                    print("Here is a list of all your accounts:")
                                    print('\n')

                                    for account in display_accounts():
                                            print(f"{account.account_name} username: {account.user_name} pass: {account.key}")

                                    print('\n')
                            else:
                                    print('\n')
                                    print("You dont seem to have any accounts saved yet")
                                    print('\n')

                    elif short_code == 'ex':
                        print("Bye...")
                        break
                    else:
                        print("Please use the provided shortcodes")
        else:
            print("Please choose action!")

if __name__ == '__main__':

    main()
