import time
from authentication.student import StudentAuthentication
from authentication.admin import AdminAuthentication
from utilities.color import *


def main_menu():
    while True:
        print(BLUE + BOLD + UNDERLINE + "\nUniversity System" + RESET)
        choice = input(
            CYAN + "\n(S)tudent, (A)dmin, or E(x)it: " + RESET).lower()

        if choice == 's':
            student_system()
        elif choice == 'a':
            admin_system()
        elif choice == 'x':
            time.sleep(1)
            print(YELLOW + "\nExiting System\n" + RESET)
            time.sleep(1)
            exit()
        else:
            print(RED + "Invalid choice" + RESET)


def student_system():
    student_auth = StudentAuthentication()
    while True:
        choice = input(
            BLUE + BOLD + UNDERLINE + "\nStudent System\n" + RESET + CYAN + "\n(L)ogin, (R)egister or E(x)it: " + RESET).lower()

        if choice == 'l':
            student_auth.login()
        elif choice == 'r':
            student_auth.register()
        elif choice == 'x':
            main_menu()
        else:
            print(RED + "Invalid choice" + RESET)


def admin_system():
    print(BLUE + BOLD + UNDERLINE + "\nAdmin System" + RESET)
    admin_auth = AdminAuthentication()
    admin_auth.enter_special_key()


if __name__ == "__main__":
    while True:
        main_menu()
