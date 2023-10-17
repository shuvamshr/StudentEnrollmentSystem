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

            match choice:
                case 'v':
                    self.view_students()
                case 'g':
                    self.view_students_grade()
                case 's':
                    self.view_students_status()
                case 'r':
                    self.remove_student()
                case 'c':
                    self.clear_data()
                case 'x':
                    self.logout()
                    return
                case 'help':
                    self.help()
                case _:
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

    def logout(self):
        print(YELLOW +
              f"\nLogging Out" + RESET, end=" ")
        time.sleep(2)
        print(BOLD + GREEN + "[LOGGED OUT]" + RESET)
        time.sleep(1)
