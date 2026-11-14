
import json
import os


class StudentManagementSystem:

    def __init__(self):
        self.filename = "students.json"
        self.students = self.load_students()

    # Load student records from file
    def load_students(self):
        if os.path.exists(self.filename):
            try:
                with open(self.filename, "r") as file:
                    return json.load(file)
            except (json.JSONDecodeError, OSError):
                print("Warning: Could not read student file.")
                return []
        return []

    # Save student records
    def save_students(self):
        with open(self.filename, "w") as file:
            json.dump(self.students, file, indent=4)

    # Add student
    def add_student(self):
        print("\n--- Add Student ---")

        try:
            student_id = input("Enter Student ID: ")

            if any(s["id"] == student_id for s in self.students):
                print("Student ID already exists!")
                return

            name = input("Enter Student Name: ")
            age = int(input("Enter Age: "))
            course = input("Enter Course: ")
            marks = float(input("Enter Marks: "))

            if age <= 0 or not 0 <= marks <= 100:
                print("Invalid age or marks!")
                return

            student = {
                "id": student_id,
                "name": name,
                "age": age,
                "course": course,
                "marks": marks
            }

            self.students.append(student)
            self.save_students()

            print("Student added successfully!")

        except ValueError:
            print("Please enter valid numeric values.")

    # View all students
    def view_students(self):
        print("\n--- Student Records ---")

        if not self.students:
            print("No student records found.")
            return

        for student in self.students:
            print("------------------------")
            print("ID:", student["id"])
            print("Name:", student["name"])
            print("Age:", student["age"])
            print("Course:", student["course"])
            print("Marks:", student["marks"])

    # Search student
    def search_student(self):
        student_id = input("\nEnter Student ID to search: ")

        for student in self.students:
            if student["id"] == student_id:
                print("\nStudent Found!")
                print(student)
                return

        print("Student not found.")

    # Update student
    def update_student(self):
        student_id = input("\nEnter Student ID to update: ")

        for student in self.students:
            if student["id"] == student_id:
                print("Leave a field blank to keep its current value.")

                name = input("Enter New Name: ")
                age = input("Enter New Age: ")
                course = input("Enter New Course: ")
                marks = input("Enter New Marks: ")

                if name:
                    student["name"] = name

                try:
                    if age:
                        if int(age) <= 0:
                            print("Invalid age!")
                            return
                        student["age"] = int(age)

                    if marks:
                        if not 0 <= float(marks) <= 100:
                            print("Invalid marks!")
                            return
                        student["marks"] = float(marks)

                except ValueError:
                    print("Invalid numeric input!")
                    return

                if course:
                    student["course"] = course

                self.save_students()
                print("Student updated successfully!")
                return

        print("Student not found.")

    # Delete student
    def delete_student(self):
        student_id = input("\nEnter Student ID to delete: ")

        for student in self.students:
            if student["id"] == student_id:
                self.students.remove(student)
                self.save_students()
                print("Student deleted successfully!")
                return

        print("Student not found.")

    # Display statistics
    def show_statistics(self):
        if not self.students:
            print("No student records available.")
            return

        total = len(self.students)
        average = sum(s["marks"] for s in self.students) / total
        highest = max(self.students, key=lambda s: s["marks"])

        print("\n--- Student Statistics ---")
        print("Total Students:", total)
        print("Average Marks:", round(average, 2))
        print("Top Student:", highest["name"])
        print("Highest Marks:", highest["marks"])

    # Main menu
    def run(self):
        while True:
            print("\n================================")
            print("   STUDENT MANAGEMENT SYSTEM")
            print("================================")
            print("1. Add Student")
            print("2. View All Students")
            print("3. Search Student")
            print("4. Update Student")
            print("5. Delete Student")
            print("6. Student Statistics")
            print("7. Exit")

            choice = input("\nEnter your choice: ")

            if choice == "1":
                self.add_student()

            elif choice == "2":
                self.view_students()

            elif choice == "3":
                self.search_student()

            elif choice == "4":
                self.update_student()

            elif choice == "5":
                self.delete_student()

            elif choice == "6":
                self.show_statistics()

            elif choice == "7":
                print("Thank you for using Student Management System!")
                break

            else:
                print("Invalid choice! Please try again.")


#create object & start application
if __name__ == "__main__":
    system = StudentManagementSystem()
    system.run()