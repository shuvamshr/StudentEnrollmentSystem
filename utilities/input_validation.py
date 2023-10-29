import re
from utilities.color import *


def validate_name(input_string):
    while True:
        name = input(input_string)
        if name.isalpha():
            return name
        else:
            print(RED + '\nError: Please enter a valid name\n' + RESET)
        # check if name is string, if true 'return name', else 'print('error')'


def validate_email(input_string, first_name, last_name):
    while True:
        email = input(input_string).lower()
        email_reg = first_name + r'\.' + last_name + r'.*@.*university\.com$'
        if re.match(email_reg, email, re.IGNORECASE):
            return email
        else:
            print(
                RED + "\nError: Email must be FirstName.LastName@university.com\n" + RESET)
        # check if email is valid against first_name and last_name, if true 'return email', else 'print('error')'


def validate_password(input_string):
    while True:
        password = input(input_string)
        if re.match(r"^[A-Z][a-zA-Z]{5,}[0-9]{3,}$", password):
            return password
        else:
            print(RED + "\nError: Password must start with an uppercase letter, have at least 6 letters, and be followed by at least 3 digits\n" + RESET)

        # check if password is valid, if true 'return email', else 'print('error')'
