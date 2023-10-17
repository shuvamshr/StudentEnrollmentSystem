import os
import json
import time
from authentication.student import StudentAuthentication
from authentication.admin import AdminAuthentication
from utilities.color import *


class System:
    def main_menu(self):
        while True:
            print(BLUE + BOLD + UNDERLINE + "\nUniversity System" + RESET)
            choice = input(
                CYAN + "\n(S)tudent, (A)dmin, or E(x)it: " + RESET).lower()

            if choice == 's':
                self.student_system()
            elif choice == 'a':
                self.admin_system()
            elif choice == 'x':
                time.sleep(1)
                print(YELLOW + "\nExiting System\n" + RESET)
                time.sleep(1)
                exit()
            else:
                print(RED + "Invalid choice" + RESET)

    def student_system(self):
        student_auth = StudentAuthentication()
        while True:
            choice = input(
                BLUE + BOLD + UNDERLINE + "\nStudent System\n" + RESET + CYAN + "\n(L)ogin, (R)egister or E(x)it: " + RESET).lower()

            if choice == 'l':
                student_auth.login()
            elif choice == 'r':
                student_auth.register()
            elif choice == 'x':
                self.main_menu()
            else:
                print(RED + "Invalid choice" + RESET)

    def admin_system(self):
        print(BLUE + BOLD + UNDERLINE + "\nAdmin System" + RESET)
        admin_auth = AdminAuthentication()
        admin_auth.enter_special_key()


if __name__ == "__main__":
    system = System()
    while True:
        system.main_menu()
