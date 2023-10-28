import time
import json
import os
from utilities.color import *
from utilities.mark_check import grade_check, status_check


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
                self.logout()
                return
            elif choice == 'help':
                self.help()
            else:
                print(RED + "Invalid choice" + RESET)

    def view_students(self):
        print(BOLD + GREEN + UNDERLINE + "\nStudent List" + RESET)
        print()
        try:
            with open('student.data', 'r') as file:
                students_data = json.load(file)

                if not students_data:
                    print(BOLD + MAGENTA +
                          " <Nothing to display> No student data found.")
                else:
                    for student in students_data:
                        print(
                            f"{student['first_name']} {student['last_name']} :: {student['id']} --> {student['email']}" + RESET)

        except FileNotFoundError:
            print(RED + "\nThe 'student.data' file does not exist.")

    def view_students_grade(self):
        print(BOLD + GREEN + UNDERLINE + "\nView Students By Grade" + RESET)
        print()
        try:
            with open('student.data', 'r') as file:
                students_data = json.load(file)

                if not students_data:
                    print(MAGENTA + "\nNo student data found.")
                else:
                    grade_to_view = input(
                        CYAN + "Enter the grade to view (HD/D/C/P/F): ").upper()

                    if grade_to_view not in ('HD', 'D', 'C', 'P', 'F'):
                        print(BOLD + MAGENTA +
                              "\nInvalid grade. Please enter HD, D, C, P, or F.")
                    else:
                        found_students = False
                        print(BOLD + GREEN +
                              f"\nStudents with Grade {grade_to_view}:" + RESET)
                        for student in students_data:
                            grades = student.get("subject", {})

                            for value in grades.values():
                                if isinstance(value, int):
                                    student_grade = grade_check(value)

                                    if student_grade == grade_to_view:
                                        print(
                                            f"{grade_to_view} --> [ {student['first_name']} {student['last_name']} :: {student['id']} --> GRADE: {grade_to_view} - Mark : {value} ]")
                                        found_students = True
                        if not found_students:
                            print(
                                MAGENTA + "\nStudent not found for the specified grade.")

        except FileNotFoundError:
            print(RED + "\nThe 'student.data' file does not exist.")

    def view_students_status(self):
        print(BOLD + GREEN + UNDERLINE +
              "\nView Students By PASS/FAIL Status" + RESET)
        print()
        try:
            with open('student.data', 'r') as file:
                students_data = json.load(file)

                if not students_data:
                    print(MAGENTA + "No student data found.")
                else:
                    pass_students = []
                    fail_students = []

                    for student in students_data:
                        grades = student.get("subject", {})
                        student_status = "PASS"

                        for value in grades.values():
                            if isinstance(value, int):
                                student_status = status_check(value)

                                if student_status == "PASS":
                                    formatted_string = f"{student['first_name']} {student['last_name']} :: {student['id']} --> GRADE: {student_status} - Mark : {value}"
                                    pass_students.append(formatted_string)
                                else:
                                    formatted_string = f"{student['first_name']} {student['last_name']} :: {student['id']} --> GRADE: {student_status} - Mark : {value}"
                                    fail_students.append(formatted_string)

                    if pass_students:
                        pass_students_string = ', '.join(pass_students)
                        print(BOLD + BLUE + "PASS --> " + RESET +
                              "[" + f"{pass_students_string}" + "]")
                        print()

                    if fail_students:
                        fail_students_string = ', '.join(fail_students)
                        print(BOLD + MAGENTA + "FAIL --> " + RESET +
                              "[" + f"{fail_students_string}" + "]")

        except FileNotFoundError:
            print(RED + "\nThe 'student.data' file does not exist.")

    def remove_student(self):
        print(BOLD + GREEN + UNDERLINE + "\nRemove Student By ID" + RESET)
        print()
        try:
            with open('student.data', 'r') as file:
                students_data = json.load(file)

            student_id_to_remove = input(
                CYAN + "Enter the student ID to remove: " + RESET)
            updated_students_data = [student for student in students_data if student.get(
                "id") != student_id_to_remove]

            if len(updated_students_data) < len(students_data):
                with open('student.data', 'w') as file:
                    json.dump(updated_students_data, file, indent=4)

                print("\nStudent with ID" + BOLD + YELLOW +
                      f"{student_id_to_remove}" + RESET + "removed successfully.")
            else:
                print(MAGENTA + "\nNo student found with ID" + BOLD +
                      YELLOW + f" {student_id_to_remove} " + RESET)

        except FileNotFoundError:
            print(RED + "\nThe 'student.data' file does not exist." + RESET)

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
