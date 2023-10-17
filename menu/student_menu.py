import json
import time
from utilities.input_validation import validate_password
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
        print("Enroll Subject Logic Here")

    def view_enrollment(self):
        print("View Enrollment Subject Logic Here")

    def remove_subject(self):
        print("Remove Subject Logic Here")

    def change_password(self):
        print(BOLD + UNDERLINE + "\nChange Password" + RESET)
        print()
        new_password = validate_password("Enter New Password: ")

        # Update the password in the students_data list
        for student_data in self.students_data:
            if student_data['id'] == self.student['id']:
                student_data['password'] = new_password

        # Save the updated data to the student.data file
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
