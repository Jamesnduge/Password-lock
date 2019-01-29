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
