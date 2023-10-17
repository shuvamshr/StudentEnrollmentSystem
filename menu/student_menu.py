import json
import time
import random
import string
from utilities.input_validation import validate_password
from utilities.mark_check import grade_check, status_check
from utilities.color import *


class StudentMenu:
    def __init__(self, student, students_data):
        self.student = student
        self.students_data = students_data

    def display_menu(self):
        print(BLUE + BOLD + UNDERLINE + "\nStudent System" + RESET + BLUE + BOLD +
              f" [Logged in: {self.student['first_name']} {self.student['last_name']}]" + RESET)

        while True:
            choice = input(CYAN + "\n(E/V/R/C/X/help): " + RESET).lower()

            match choice:
                case 'e':
                    self.enroll_subject()
                case 'v':
                    self.view_enrollment()
                case 'r':
                    self.remove_subject()
                case 'c':
                    self.change_password()
                case 'help':
                    self.help()
                case 'x':
                    self.logout()
                    return
                case _:
                    print(RED + "Invalid choice" + RESET)

    def enroll_subject(self):
        time.sleep(1)
        print(YELLOW +
              f"\nEnrolling into Subject" + RESET, end=" ")
        time.sleep(2)
        print(BOLD + GREEN + "[SUCCESS]" + RESET)
        time.sleep(1)

        subject_code = ''.join(random.choice(string.digits) for _ in range(3))

        mark = random.randint(40, 100)

        self.student['subject'][subject_code] = mark

        for student_data in self.students_data:
            if student_data['id'] == self.student['id']:
                student_data['subject'] = self.student['subject']

        with open('student.data', 'w') as file:
            json.dump(self.students_data, file, indent=4)

        print(
            BOLD + f"\nSubject Code: {subject_code} || Mark: {mark} || Grade: {grade_check(mark)} || Status: {status_check(mark)}" + RESET)

    def view_enrollment(self):
        print("View Enrollment Logic Here")

    def remove_subject(self):
        print("Remove Subject Logic Here")

    def change_password(self):
        print(BOLD + UNDERLINE + "\nChange Password" + RESET)
        print()
        new_password = validate_password("Enter New Password: ")

        for student_data in self.students_data:
            if student_data['id'] == self.student['id']:
                student_data['password'] = new_password

        with open('student.data', 'w') as file:
            json.dump(self.students_data, file, indent=4)

        print(YELLOW +
              f"\nUpdating password" + RESET, end=" ")
        time.sleep(2)
        print(BOLD + GREEN + "[SUCCESS]" + RESET)
        time.sleep(1)

    def help(self):
        print(BOLD + UNDERLINE + "\nCommand Details" + RESET)
        print()
        print("E: Enroll Into Subject")
        print("V: View Current Enrollments")
        print("R: Remove Subject")
        print("C: Change Password")
        print("X: Logout of Student System")
        print()
        print("Note: Commands are not case-sensitive")

    def logout(self):
        print(YELLOW +
              f"\nLogging Out" + RESET, end=" ")
        time.sleep(2)
        print(BOLD + GREEN + "[LOGGED OUT]" + RESET)
        time.sleep(1)
