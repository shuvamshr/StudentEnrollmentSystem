import tkinter as tk
from utilities.color import *
from utilities.input_validation import validate_name, validate_email, validate_password


class GUISystem:
    def __init__(self, root):
        self.root = root
        self.root.title("University GUI System")
        self.root.geometry("400x300")
        self.frame = None
        self.label = tk.Label(root, text="Welcome to University")
        self.label.pack()
        self.student_button = tk.Button(
            root, text="Student System", command=self.switch_to_student)
        self.student_button.pack()
        self.admin_button = tk.Button(
            root, text="Admin System", command=self.switch_to_admin)
        self.admin_button.pack()
        self.admin_access_key = "enr0llm3nt"
        self.admin_authenticated = False

    def switch_to_student(self):
        if self.frame:
            self.frame.destroy()
            self.label.config(text="Welcome to University")
        self.student_button.pack_forget()
        self.admin_button.pack_forget()
        self.frame = tk.Frame(self.root)
        self.frame.pack()
        login_button = tk.Button(
            self.frame, text="Login", command=self.login_student)
        login_button.pack()
        register_button = tk.Button(
            self.frame, text="Register", command=self.register_student)
        register_button.pack()
        go_back_button = tk.Button(
            self.frame, text="Go Back", command=self.go_back)
        go_back_button.pack()

    def switch_to_admin(self):
        if self.frame:
            self.frame.destroy()
            self.label.config(text="Welcome to University")
        self.student_button.pack_forget()
        self.admin_button.pack_forget()
        self.frame = tk.Frame(self.root)
        self.frame.pack()
        if not self.admin_authenticated:
            admin_special_key_label = tk.Label(
                self.frame, text="Enter the Admin Access Key:")
            admin_special_key_label.pack()
            admin_special_key_entry = tk.Entry(
                self.frame, show="*")
            admin_special_key_entry.pack()
            admin_special_key_submit = tk.Button(
                self.frame, text="Submit", command=lambda: self.check_special_key(admin_special_key_entry))
            admin_special_key_submit.pack()
        else:
            admin_button1 = tk.Button(
                self.frame, text="View Students", command=self.view_students)
            admin_button1.pack()
            admin_button2 = tk.Button(
                self.frame, text="View Students By Grade", command=self.view_students_grade)
            admin_button2.pack()
            admin_button3 = tk.Button(
                self.frame, text="View Students By PASS/FAIL Status", command=self.view_students_status)
            admin_button3.pack()
            admin_button4 = tk.Button(
                self.frame, text="Remove Student", command=self.remove_student)
            admin_button4.pack()
            admin_button5 = tk.Button(
                self.frame, text="Clear Student Data", command=self.clear_data)
            admin_button5.pack()
        go_back_button = tk.Button(
            self.frame, text="Go Back", command=self.go_back)
        go_back_button.pack()

    def switch_to_registration(self):
        if self.frame:
            self.frame.destroy()
            self.label.config(text="Student Registration")
        self.student_button.pack_forget()
        self.admin_button.pack_forget()
        self.frame = tk.Frame(self.root)
        self.frame.pack()
        first_name_label = tk.Label(self.frame, text="First Name:")
        first_name_label.pack()
        first_name_entry = tk.Entry(self.frame)
        first_name_entry.pack()
        last_name_label = tk.Label(self.frame, text="Last Name:")
        last_name_label.pack()
        last_name_entry = tk.Entry(self.frame)
        last_name_entry.pack()
        email_label = tk.Label(self.frame, text="Email:")
        email_label.pack()
        email_entry = tk.Entry(self.frame)
        email_entry.pack()
        password_label = tk.Label(self.frame, text="Password:")
        password_label.pack()
        password_entry = tk.Entry(self.frame, show="*")
        password_entry.pack()
        register_submit_button = tk.Button(self.frame, text="Register", command=lambda: self.register_student(
            first_name_entry.get(), last_name_entry.get(), email_entry.get(), password_entry.get()))
        register_submit_button.pack()
        go_back_button = tk.Button(
            self.frame, text="Go Back", command=self.go_back)
        go_back_button.pack()

    def switch_to_student(self):
        if self.frame:
            self.frame.destroy()
            self.label.config(text="Welcome to University")
        self.student_button.pack_forget()
        self.admin_button.pack_forget()
        self.frame = tk.Frame(self.root)
        self.frame.pack()
        login_button = tk.Button(
            self.frame, text="Login", command=self.login_student)
        login_button.pack()
        register_button = tk.Button(
            self.frame, text="Register", command=self.switch_to_registration)
        register_button.pack()
        go_back_button = tk.Button(
            self.frame, text="Go Back", command=self.go_back)
        go_back_button.pack()

    def login_student(self):
        pass

    def register_student(self, first_name, last_name, email, password):
        if validate_name(first_name) and validate_name(last_name) and validate_email(email, first_name, last_name) and validate_password(password):

            print(BOLD + GREEN + "Registration successful." + RESET)

        else:
            print(BOLD + RED + "Registration failed. Please check your input." + RESET)

    def check_special_key(self, admin_special_key_entry):
        special_key = admin_special_key_entry.get()
        if special_key == self.admin_access_key:
            admin_special_key_entry.destroy()
            self.admin_authenticated = True
            self.switch_to_admin()
        else:
            admin_special_key_entry.delete(0, tk.END)

    def go_back(self):
        if self.frame:
            self.frame.destroy()
            self.label.config(text="Welcome to University")
        self.admin_authenticated = False
        self.admin_button.pack()
        self.student_button.pack()


if __name__ == "__main__":
    root = tk.Tk()
    app = GUISystem(root)
    root.mainloop()
