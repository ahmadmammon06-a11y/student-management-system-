class Student:
    def __init__(self, student_id, name, age, department, marks):
        self.__student_id = student_id
        self.__name = name
        self.__age = age
        self.__department = department
        self.__marks = marks

    # Getter methods
    def get_student_id(self):
        return self.__student_id

    def get_name(self):
        return self.__name

    def get_age(self):
        return self.__age

    def get_department(self):
        return self.__department

    def get_marks(self):
        return self.__marks

    # Setter methods
    def set_name(self, name):
        self.__name = name

    def set_age(self, age):
        self.__age = age

    def set_department(self, department):
        self.__department = department

    def set_marks(self, marks):
        self.__marks = marks

    # Percentage
    def get_percentage(self):
        total_marks = 500
        return (self.__marks / total_marks) * 100

    # Grade
    def get_grade(self):
        percentage = self.get_percentage()

        if percentage >= 80:
            return "A+"
        elif percentage >= 70:
            return "A"
        elif percentage >= 60:
            return "B"
        elif percentage >= 50:
            return "C"
        elif percentage >= 40:
            return "D"
        else:
            return "F"

    # Display student
    def display(self):
        print("\n------------------------------")
        print("Student ID:", self.__student_id)
        print("Name:", self.__name)
        print("Age:", self.__age)
        print("Department:", self.__department)
        print("Marks:", self.__marks, "/ 500")
        print("Percentage:", round(self.get_percentage(), 2), "%")
        print("Grade:", self.get_grade())
        print("------------------------------")


class StudentManagementSystem:

    def __init__(self):
        self.students = []

    # Add student
    def add_student(self):
        print("\n===== Add Student =====")

        student_id = input("Enter Student ID: ")

        # Check duplicate ID
        for student in self.students:
            if student.get_student_id() == student_id:
                print("Student ID already exists.")
                return

        name = input("Enter Student Name: ")

        while True:
            try:
                age = int(input("Enter Age: "))

                if age <= 0:
                    print("Age must be greater than 0.")
                else:
                    break

            except ValueError:
                print("Please enter a valid number.")

        department = input("Enter Department: ")

        while True:
            try:
                marks = float(input("Enter Total Marks (out of 500): "))

                if marks < 0 or marks > 500:
                    print("Marks must be between 0 and 500.")
                else:
                    break

            except ValueError:
                print("Please enter a valid number.")

        student = Student(
            student_id,
            name,
            age,
            department,
            marks
        )

        self.students.append(student)

        print("\nStudent added successfully.")


    # View all students
    def view_students(self):
        print("\n===== All Students =====")

        if len(self.students) == 0:
            print("No students found.")
            return

        for student in self.students:
            student.display()


    # Search student
    def search_student(self):
        print("\n===== Search Student =====")

        student_id = input("Enter Student ID: ")

        for student in self.students:

            if student.get_student_id() == student_id:
                student.display()
                return

        print("Student not found.")


    # Update student
    def update_student(self):
        print("\n===== Update Student =====")

        student_id = input("Enter Student ID: ")

        for student in self.students:

            if student.get_student_id() == student_id:

                print("\n1. Update Name")
                print("2. Update Age")
                print("3. Update Department")
                print("4. Update Marks")

                choice = input("Enter your choice: ")

                if choice == "1":
                    new_name = input("Enter new name: ")
                    student.set_name(new_name)
                    print("Name updated successfully.")

                elif choice == "2":

                    try:
                        new_age = int(input("Enter new age: "))

                        if new_age <= 0:
                            print("Invalid age.")
                        else:
                            student.set_age(new_age)
                            print("Age updated successfully.")

                    except ValueError:
                        print("Invalid input.")

                elif choice == "3":
                    new_department = input("Enter new department: ")
                    student.set_department(new_department)
                    print("Department updated successfully.")

                elif choice == "4":

                    try:
                        new_marks = float(input("Enter new marks: "))

                        if 0 <= new_marks <= 500:
                            student.set_marks(new_marks)
                            print("Marks updated successfully.")
                        else:
                            print("Marks must be between 0 and 500.")

                    except ValueError:
                        print("Invalid marks.")

                else:
                    print("Invalid choice.")

                return

        print("Student not found.")


    # Delete student
    def delete_student(self):
        print("\n===== Delete Student =====")

        student_id = input("Enter Student ID: ")

        for student in self.students:

            if student.get_student_id() == student_id:

                self.students.remove(student)

                print("Student deleted successfully.")
                return

        print("Student not found.")


    # Highest percentage
    def highest_student(self):
        print("\n===== Highest Percentage =====")

        if len(self.students) == 0:
            print("No students found.")
            return

        highest = max(
            self.students,
            key=lambda student: student.get_percentage()
        )

        highest.display()


    # Lowest percentage
    def lowest_student(self):
        print("\n===== Lowest Percentage =====")

        if len(self.students) == 0:
            print("No students found.")
            return

        lowest = min(
            self.students,
            key=lambda student: student.get_percentage()
        )

        lowest.display()


    # Total students
    def total_students(self):
        print("\nTotal Students:", len(self.students))


# Create object
system = StudentManagementSystem()


# Main menu
while True:

    print("\n================================")
    print("     STUDENT MANAGEMENT SYSTEM")
    print("================================")

    print("1. Add Student")
    print("2. View All Students")
    print("3. Search Student")
    print("4. Update Student")
    print("5. Delete Student")
    print("6. Highest Percentage")
    print("7. Lowest Percentage")
    print("8. Total Students")
    print("9. Exit")

    choice = input("\nEnter your choice: ")

    if choice == "1":
        system.add_student()

    elif choice == "2":
        system.view_students()

    elif choice == "3":
        system.search_student()

    elif choice == "4":
        system.update_student()

    elif choice == "5":
        system.delete_student()

    elif choice == "6":
        system.highest_student()

    elif choice == "7":
        system.lowest_student()

    elif choice == "8":
        system.total_students()

    elif choice == "9":
        print("\nThank you for using Student Management System.")
        break

    else:
        print("\nInvalid choice. Please try again.")