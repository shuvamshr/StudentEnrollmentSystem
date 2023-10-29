import time
from menu.admin_menu import AdminMenu
from utilities.color import *


class AdminAuthentication:
    def __init__(self):
        self.special_key = "admin3164"

    def enter_special_key(self):

        special_key_input = input(
            CYAN + "\nEnter the Admin Access Key: " + RESET)
        if special_key_input == self.special_key:
            print(YELLOW +
                  f"\nChecking credentials" + RESET, end=" ")
            time.sleep(2)
            print(BOLD + GREEN + "[LOGGED IN]" + RESET)
            time.sleep(1)
            admin_menu = AdminMenu(self)
            admin_menu.display_menu()
        else:
            time.sleep(1)
            print(RED + "\nAccess Denied. Invalid Access Key." + RESET)
