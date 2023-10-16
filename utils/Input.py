from utils.Color import *
import getpass


class In:
    @staticmethod
    def get_valid_string(prompt, validation_func):
        while True:
            value = input(prompt)
            if validation_func(value):
                return value
            print(
                RED + "Invalid input. Requirement:: Must contain only letters.\n" + RESET)

    @staticmethod
    def get_valid_email(prompt, validation_func):
        while True:
            email = input(prompt)
            if validation_func(email):
                print(
                    YELLOW + "Valid Email" + RESET)
                return email
            print(
                RED + "Invalid email format. Requirement:: Correct format firstName.lastName@university.com" + RESET)

    @staticmethod
    def get_valid_password(prompt, validation_func):
        while True:
            password = getpass.getpass(prompt)
            if validation_func(password):
                print(
                    YELLOW + "Valid Password" + RESET)
                return password
            print(RED + "Invalid password. Requirement:: Starts with Upper-case, Minimum 4 Letters, Ends with 3+ Digits" + RESET)

    @staticmethod
    def is_valid_email(email):
        # Add your email validation logic here
        # For example, you can use a regular expression to check the email format
        return True

    @staticmethod
    def is_valid_password(password):
        # Add your password validation logic here
        # For example, you can check for minimum length, complexity, etc.
        return True
