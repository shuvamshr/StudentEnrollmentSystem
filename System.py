from Student import Student
from Admin import Admin
from utils.Input import In
from utils.Color import *
import random
import string
import sys
import time


class System:
    def __init__(self):
        self.students = {}
        self.active_student = None
        self.admin_access_key = "enr0llm3nt"

    def main_menu(self):
        while True:
            choice = input(BLUE +
                           "\nUniversity System\n" + CYAN + "(A)dmin, (S)tudent, or E(x)it: " + RESET).lower()

            if choice == 's':
                self.student_menu()
            elif choice == 'a':
                self.admin_menu()
            elif choice == 'x':
                print(YELLOW + "\nExiting System\n" + RESET)
                sys.exit()
            else:
                print(RED + "Invalid choice" + RESET)

    def student_menu(self):
        while True:
            choice = input(
                BLUE + "\nStudent System\n" + CYAN + "(L)ogin, (R)egister or E(x)it: " + RESET).lower()

            if choice == 'l':
                self.student_login()
            elif choice == 'r':
                self.student_registration()
            elif choice == 'x':
                self.main_menu()
            else:
                print(RED + "Invalid choice" + RESET)

    def admin_menu(self):
        admin_key = input(CYAN + "\nEnter the Admin Access Key: " + RESET)

        if admin_key == self.admin_access_key:
            print(YELLOW + "\nLogged in as Admin" + RESET)
            while True:
                choice = input(
                    BLUE + "\nAdmin Menu [Logged in: Admin]\n" + CYAN + "(V/G/S/R/C/X/help): " + RESET).lower()

                if choice == 'v':
                    Admin.display_students(self.students)
                elif choice == 'x':
                    print(YELLOW + "\nLogged out of Admin" + RESET)
                    self.main_menu()
                elif choice == 'help':
                    print("\nCommand Details\n===============\nV: View All Students\nG: View Students By Grade\nS: View Students By PASS/FAIL Status\nR: Remove Student\nC: Clear Student Data\nX: Logout of Admin System\n\nNote: Commands are not case-sensitive")
                else:
                    print(RED + "Invalid choice" + RESET)
        else:
            print(RED + "Access Denied. Invalid Access Key." + RESET)

    def student_registration(self):
        print(GREEN + "\nStudent Sign Up" + RESET)
        first_name = In.get_valid_string(
            "First Name: ", lambda x: x.isalpha())
        last_name = In.get_valid_string("Last Name: ", lambda x: x.isalpha())

        email = In.get_valid_email("Email: ", In.is_valid_email)
        password = In.get_valid_password("Password: ", In.is_valid_password)

        student_id = self.generate_student_id()

        self.students[student_id] = Student(
            student_id, first_name, last_name, email, password)

        time.sleep(1)

        print(
            YELLOW + f"\nEnrolling {first_name} {last_name} with ID: {student_id}" + RESET, end=" ")

        time.sleep(2)
        print(GREEN + "[SUCCESS]" + RESET)
        time.sleep(1)

    def generate_student_id(self):

        # Generate a random 6-digit student ID
        return ''.join(random.choice(string.digits) for _ in range(6))

    def student_login(self):

        print(GREEN + "\nStudent Sign In" + RESET)

        email = input("Enter your email: ")
        password = input("Enter your password: ")

        self.active_student = self.find_student_by_email_password(
            email, password)

        time.sleep(1)

        if self.active_student:
            print(
                YELLOW + f"\nLogged in as {self.active_student.first_name} {self.active_student.last_name}" + RESET)
            time.sleep(2)
            self.student_option()
        else:
            print(RED + "Login failed. Email or password is incorrect." + RESET)

    def student_option(self):
        while True:
            choice = input(
                BLUE + f"\nStudent Menu [Logged in: {self.active_student.first_name} {self.active_student.last_name}]\n" + CYAN + "(E/V/R/C/X/help): " + RESET).lower()

            if choice == 'c':
                self.print_student_details()
            elif choice == 'x':
                print(
                    YELLOW + f"\nLogged out of {self.active_student.first_name} {self.active_student.last_name}" + RESET)
                self.main_menu()
            else:
                print("Invalid choice.")

    def find_student_by_email_password(self, email, password):
        for student in self.students.values():
            if student.email == email and student.password == password:
                return student
        return None

    def print_student_details(self):
        if self.active_student:
            print(
                GREEN + f"\nStudent Details for {self.active_student.first_name} {self.active_student.last_name} (ID: {self.active_student.student_id})" + RESET)
            print(f"Email: {self.active_student.email}")
            # Add more details to print as needed
        else:
            print(RED + "Student not found." + RESET)


if __name__ == "__main__":
    system = System()
    system.main_menu()
