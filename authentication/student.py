import os
import json
import time
import random
from utilities.input_validation import validate_email, validate_password, validate_name
from menu.student_menu import StudentMenu
from utilities.color import *


class StudentAuthentication:
    def __init__(self):
        self.student_data_file = 'student.data'
        self.students = self.load_students()

    def load_students(self):
        if os.path.exists(self.student_data_file):
            with open(self.student_data_file, 'r') as file:
                students = json.load(file)
            return students
        else:
            return []

    def save_students(self):
        with open(self.student_data_file, 'w') as file:
            json.dump(self.students, file, indent=4)

    def register(self):
        print(BOLD + UNDERLINE + "\nStudent Registeration" + RESET)
        print()
        first_name = validate_name("Enter First Name: ")
        last_name = validate_name("Enter Last Name: ")
        email = validate_email("Enter Email Address: ", first_name, last_name)
        password = validate_password("Enter Password: ")

        student_id = str(self.generate_student_id())
        student = {
            'id': student_id,
            'first_name': first_name,
            'last_name': last_name,
            'email': email,
            'password': password,
            'subject': {}
        }
        self.students.append(student)
        self.save_students()
        print(YELLOW +
              f"\nRegistering {first_name} {last_name} with ID: {student_id}" + RESET, end=" ")
        time.sleep(2)
        print(BOLD + GREEN + "[SUCCESS]" + RESET)
        time.sleep(1)

    def login(self):
        print(BOLD + UNDERLINE + "\nStudent Login" + RESET)
        print()
        email = input("Enter Email Address: ")
        password = input("Enter Password: ")

        for student in self.students:
            if student['email'] == email and student['password'] == password:
                print(YELLOW +
                      f"\nChecking credentials" + RESET, end=" ")
                time.sleep(2)
                print(BOLD + GREEN + "[LOGGED IN]" + RESET)
                time.sleep(1)
                student_menu = StudentMenu(
                    student, self.students)
                student_menu.display_menu()
                return
        time.sleep(1)
        print(RED + "Incorrect Email or Password. Please Try Again." + RESET)

    def generate_student_id(self):
        # Update so that it starts from 0
        return str(random.randint(100000, 999999))
