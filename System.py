from Student import Student
from Admin import Admin
from utils.Input import In
from utils.Color import *
import random
import string


class System:
    def __init__(self):
        self.students = []

    def main_menu(self):
        while True:
            choice = input(BLUE +
                           "\nUniversity System: (A)dmin, (S)tudent, or X: " + RESET).lower()

            if choice == 's':
                self.student_menu()
            elif choice == 'a':
                self.admin_menu()
            elif choice == 'x':
                print(YELLOW + "Thank you" + RESET)
            else:
                print(RED + "Invalid choice." + RESET)

    def student_menu(self):
        while True:
            choice = input(BLUE + "\nStudent System (l/r/x): " + RESET).lower()

            if choice == 'l':
                self.student_login()
            elif choice == 'r':
                self.student_registration()
            elif choice == 'x':
                self.main_menu()
            else:
                print(
                    "Invalid choice.")

    def admin_menu(self):
        while True:
            choice = input(
                BLUE + "\nAdmin System (c/g/p/r/s/x): " + RESET).lower()

            if choice == 'c':
                Admin.display_students(self.students)
            elif choice == 'x':
                self.main_menu()
            else:
                print("Invalid choice.")

    def student_registration(self):
        print(GREEN + "\nStudent Sign Up" + RESET)
        first_name = In.get_valid_string(
            "First Name: ", lambda x: x.isalpha())
        last_name = In.get_valid_string("Last Name: ", lambda x: x.isalpha())

        email = In.get_valid_email("Email: ", In.is_valid_email)
        password = In.get_valid_password("Password: ", In.is_valid_password)

        student_id = self.generate_student_id()

        new_student = Student(student_id, first_name,
                              last_name, email, password)
        self.students.append(new_student)

        print(
            YELLOW + f"\nEnrolling {first_name} {last_name} with ID: {student_id}" + RESET)

    def generate_student_id(self):

        # Generate a random 6-digit student ID
        return ''.join(random.choice(string.digits) for _ in range(6))

    def student_login(self):

        email = input("Enter your email: ")
        password = input("Enter your password: ")

        print(GREEN + "\nStudent Sign Up" + RESET)


if __name__ == "__main__":
    system = System()
    system.main_menu()
