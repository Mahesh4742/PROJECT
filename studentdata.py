#-------------------------------------------------------------------------------
# Name:        module3
# Purpose:
#
# Author:      Mahesh
#
# Created:     18-05-2023
# Copyright:   (c) Mahesh 2023
# Licence:     <your licence>
#-------------------------------------------------------------------------------
import json

class StudentDatabase:
    def __init__(self):
        self.students = {}
        self.file_path = "student_data.json"

    def load_data(self):
        try:
            with open(self.file_path, "r") as file:
                self.students = json.load(file)
        except FileNotFoundError:
            pass

    def save_data(self):
        with open(self.file_path, "w") as file:
            json.dump(self.students, file)

    def add_student(self, student_id, name, age, grade):
        if student_id in self.students:
            print("Student with the given ID already exists.")
        else:
            self.students[student_id] = {
                "name": name,
                "age": age,
                "grade": grade
            }
            print("Student added successfully.")
            self.save_data()

    def remove_student(self, student_id):
        if student_id in self.students:
            del self.students[student_id]
            print("Student removed successfully.")
            self.save_data()
        else:
            print("Student with the given ID does not exist.")

    def get_student_by_id(self, student_id):
        if student_id in self.students:
            student = self.students[student_id]
            return f"Name: {student['name']}\nID: {student_id}\nAge: {student['age']}\nGrade: {student['grade']}"
        else:
            return "Student with the given ID does not exist."

    def get_all_students(self):
        if self.students:
            for student_id, student in self.students.items():
                print(f"Name: {student['name']}\nID: {student_id}\nAge: {student['age']}\nGrade: {student['grade']}")
        else:
            print("No students in the database.")


# Create a student database
database = StudentDatabase()
database.load_data()

while True:
    print("Menu:")
    print("1. Add student")
    print("2. Remove student")
    print("3. Get student by ID")
    print("4. Get all students")
    print("5. Exit")
    choice = input("Enter your choice (1-5): ")

    if choice == "1":
        student_id = input("Enter student ID: ")
        name = input("Enter student name: ")
        age = input("Enter student age: ")
        grade = input("Enter student grade: ")
        database.add_student(student_id, name, age, grade)
    elif choice == "2":
        student_id = input("Enter student ID to remove: ")
        database.remove_student(student_id)
    elif choice == "3":
        student_id = input("Enter student ID to search: ")
        found_student = database.get_student_by_id(student_id)
        print(found_student)
    elif choice == "4":
        database.get_all_students()
    elif choice == "5":
        print("Exiting...")
        database.save_data()
        break
    else:
        print("Invalid choice. Please try again.")
