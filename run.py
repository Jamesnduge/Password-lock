#!/usr/bin/env python3.7
from passwordLocker import User, Credentials

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
