import tkinter as tk
from tkinter import ttk, messagebox
import json
import random


class GUISystem:
    def __init__(self, window):
        self.window = window
        self.window.title("Login Application")

        with open("student.data", "r") as file:
            self.student_data = json.load(file)

        self.create_widgets()

    def create_widgets(self):
        style = ttk.Style()
        style.configure("TLabel", font=("Arial", 12))
        style.configure("TButton", font=("Arial", 12))

        self.frame = ttk.Frame(self.window)
        self.frame.pack(padx=20, pady=20)

        self.email_label = ttk.Label(self.frame, text="Email:")
        self.email_label.grid(row=0, column=0, sticky="w", padx=10, pady=5)
        self.email_entry = ttk.Entry(self.frame)
        self.email_entry.grid(row=0, column=1, padx=10, pady=5)

        self.password_label = ttk.Label(self.frame, text="Password:")
        self.password_label.grid(row=1, column=0, sticky="w", padx=10, pady=5)
        self.password_entry = ttk.Entry(self.frame, show="*")
        self.password_entry.grid(row=1, column=1, padx=10, pady=5)

        self.login_button = ttk.Button(
            self.frame, text="Login", command=self.validate_login)
        self.login_button.grid(row=2, columnspan=2, pady=10)

    def validate_login(self):
        entered_email = self.email_entry.get()
        entered_password = self.password_entry.get()

        for student in self.student_data:
            if student["email"] == entered_email and student["password"] == entered_password:
                self.open_subjects_window(student)
                return

        messagebox.showerror("Login Failed", "Invalid email or password")

    def open_subjects_window(self, student):
        subject_window = tk.Toplevel(self.window)
        subject_window.title("Subject Codes and Marks")
        subject_frame = ttk.Frame(subject_window)
        subject_frame.pack(padx=20, pady=20)

        ttk.Label(subject_frame, text="Subject Code").grid(
            row=0, column=0, padx=10, pady=5)
        ttk.Label(subject_frame, text="Marks").grid(
            row=0, column=1, padx=10, pady=5)

        row = 1
        for subject_code, marks in student["subject"].items():
            ttk.Label(subject_frame, text=subject_code).grid(
                row=row, column=0, padx=10, pady=5)
            ttk.Label(subject_frame, text=marks).grid(
                row=row, column=1, padx=10, pady=5)
            row += 1

        enroll_button = ttk.Button(
            subject_frame, text="Enroll New Subject", command=lambda: self.enroll_new_subject(student))
        enroll_button.grid(row=row, columnspan=2, pady=10)

    def enroll_new_subject(self, student):
        if len(student["subject"]) >= 4:
            messagebox.showerror(
                "Error", "You can enroll a maximum of 4 subjects.")
        else:
            new_subject_code = str(random.randint(100, 999))
            new_subject_mark = random.randint(0, 100)

            student["subject"][new_subject_code] = new_subject_mark
            messagebox.showinfo(
                "New Subject Enrolled", f"Subject {new_subject_code} added with marks {new_subject_mark}")

            with open("student.data", "w") as file:
                json.dump(self.student_data, file)

            self.open_subjects_window(student)


if __name__ == "__main__":
    app = tk.Tk()
    system = GUISystem(app)
    app.geometry("300x200")
    app.mainloop()
