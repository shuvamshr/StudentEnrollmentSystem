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

            if choice == 'e':
                self.enroll_subject()
            elif choice == 'v':
                self.view_enrollment()
            elif choice == 'r':
                self.remove_subject()
            elif choice == 'c':
                self.change_password()
            elif choice == 'x':
                self.logout()
                return
            elif choice == 'help':
                self.help()
            else:
                print(RED + "Invalid choice" + RESET)

    def enroll_subject(self):
        if len(self.student['subject']) >= 4:
            print(RED + "\nYou have already enrolled in four subjects for this semester. You will need to remove a subject to be able to enroll." + RESET)
        else:
            time.sleep(1)
            print(YELLOW + f"\nEnrolling into Subject" + RESET, end=" ")
            time.sleep(2)
            print(BOLD + GREEN + "[SUCCESS]" + RESET)
            time.sleep(1)

            subject_code = ''.join(random.choice(string.digits)
                                   for _ in range(3))

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
        print(BOLD + UNDERLINE + "\nCurrent Enrollments\n" + RESET)
        if len(self.student['subject']) == 0:
            print("You are not currently enrolled in any subjects.")
        else:
            print("Subject Code   |   Mark   |   Grade   |   Status")
            print("-" * 50)
            for subject_code, mark in self.student['subject'].items():
                grade = grade_check(mark)
                status = status_check(mark)
                print(
                    f"{subject_code}            |   {mark}     |    {grade}      |   {status}")

    def remove_subject(self):
        print(BOLD + UNDERLINE + "\nRemove Subject\n" + RESET)
        if len(self.student['subject']) == 0:
            print("You are not currently enrolled in any subjects.")
        else:
            subject_code = input("Enter the subject code to remove: ")
            if subject_code in self.student['subject']:
                del self.student['subject'][subject_code]

                for student_data in self.students_data:
                    if student_data['id'] == self.student['id']:
                        student_data['subject'] = self.student['subject']

                with open('student.data', 'w') as file:
                    json.dump(self.students_data, file, indent=4)

                print(YELLOW +
                      f"\nRemoving Subject" + RESET, end=" ")
                time.sleep(2)
                print(BOLD + GREEN + "[REMOVED]" + RESET)
                time.sleep(1)
            else:
                print(RED + "Subject code not found in your enrollments." + RESET)

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
