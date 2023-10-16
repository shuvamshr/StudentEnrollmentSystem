from utils.Color import *


class Admin:
    @staticmethod
    def display_students(students):
        if not students:
            print(RED + "No students registered" + RESET)
        else:
            print(YELLOW + "\nStudent List" + RESET)
            for student_id, student in students.items():
                student.display_student_info()
