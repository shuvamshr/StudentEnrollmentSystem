import re


def validate_name(input_string):
    while True:
        name = input(input_string)
        # check if name is string, if true 'return name', else 'print('error')'
        return name


def validate_email(input_string, first_name, last_name):
    while True:
        email = input(input_string)
        # check if email is valid against first_name and last_name, if true 'return email', else 'print('error')'
        return email


def validate_password(input_string):
    while True:
        password = input(input_string)
        # check if password is valid, if true 'return email', else 'print('error')'
        return password
