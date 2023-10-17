import time
from utilities.color import *


class AdminMenu:
    def __init__(self, admin):
        self.admin = admin

    def display_menu(self):
        print(BLUE + BOLD + UNDERLINE + "\nAdmin System" + RESET + BLUE + BOLD +
              " [Logged in: Admin]" + RESET)
        while True:

            choice = input(CYAN + "\n(V/G/S/R/C/X/help): " + RESET).lower()

            if choice == 'v':
                self.view_students()

            elif choice == 'g':
                self.view_students_grade()

            elif choice == 's':
                self.view_students_status()

            elif choice == 'r':
                self.remove_student()

            elif choice == 'c':
                self.clear_data()

            elif choice == 'x':
                time.sleep(1)
                print(YELLOW + "\n<-- Logged out of Admin -->" + RESET)
                time.sleep(1)
                return

            elif choice == 'help':
                self.help()

            else:
                print(RED + "Invalid choice" + RESET)

    def view_students(self):
        print("View Students Logic Here")

    def view_students_grade(self):
        print("View Students By Grade Logic Here")

    def view_students_status(self):
        print("View Students By PASS/FAIL Status Logic Here")

    def remove_student(self):
        print("Remove Student Logic Here")

    def clear_data(self):
        print("Clear Data Logic Here")

    def help(self):
        print(BOLD + UNDERLINE + "\nCommand Details" + RESET)
        print()
        print("V: View All Students")
        print("G: View Students By Grade")
        print("S: View Students By PASS/FAIL Status")
        print("R: Remove Student")
        print("C: Clear Student Data")
        print("X: Logout of Admin System")
        print()
        print("Note: Commands are not case-sensitive")
