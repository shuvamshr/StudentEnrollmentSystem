class Student:
    def __init__(self, student_id, first_name, last_name, email, password):
        self.student_id = student_id
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.password = password
        self.subjects = []

    def add_subject(self, subject):
        self.subjects.append(subject)

    def remove_subject(self, subject):
        if subject in self.subjects:
            self.subjects.remove(subject)

    def display_student_info(self):
        print(
            f"{self.first_name} {self.last_name} :: {self.student_id}  > {self.email}")
        # print(f"Name: {self.first_name} {self.last_name}")
        # print(f"Email: {self.email}")
        # print("Subjects Enrolled:")
        # for subject in self.subjects:
        #     print(subject)
