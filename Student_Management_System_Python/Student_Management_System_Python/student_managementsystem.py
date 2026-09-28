students = []


def add_student():
    name = input("Enter student name: ")
    roll_no = input("Enter roll number: ")
    course = input("Enter course: ")
    marks = input("Enter marks: ")

    student = {
        "name": name,
        "roll_no": roll_no,
        "course": course,
        "marks": marks
    }

    students.append(student)
    print("Student added successfully!")


def view_students():
    if len(students) == 0:
        print("No student records found.")
        return

    print("\n--- Student List ---")
    for student in students:
        print("Name:", student["name"])
        print("Roll Number:", student["roll_no"])
        print("Course:", student["course"])
        print("Marks:", student["marks"])
        print("--------------------")


def search_student():
    roll_no = input("Enter roll number to search: ")

    for student in students:
        if student["roll_no"] == roll_no:
            print("\nStudent found:")
            print("Name:", student["name"])
            print("Roll Number:", student["roll_no"])
            print("Course:", student["course"])
            print("Marks:", student["marks"])
            return

    print("Student not found.")


def update_student():
    roll_no = input("Enter roll number to update: ")

    for student in students:
        if student["roll_no"] == roll_no:
            student["name"] = input("Enter new name: ")
            student["course"] = input("Enter new course: ")
            student["marks"] = input("Enter new marks: ")
            print("Student updated successfully!")
            return

    print("Student not found.")


def delete_student():
    roll_no = input("Enter roll number to delete: ")

    for student in students:
        if student["roll_no"] == roll_no:
            students.remove(student)
            print("Student deleted successfully!")
            return

    print("Student not found.")


# Main program
while True:
    print("\n================================")
    print("   STUDENT MANAGEMENT SYSTEM")
    print("================================")
    print("1. Add Student")
    print("2. View Students")
    print("3. Search Student")
    print("4. Update Student")
    print("5. Delete Student")
    print("6. Exit")

    choice = input("Enter from above options: ")

    if choice == "1":
        add_student()

    elif choice == "2":
        view_students()

    elif choice == "3":
        search_student()

    elif choice == "4":
        update_student()

    elif choice == "5":
        delete_student()

    elif choice == "6":
        print("Thank you for using Student Management System!")
        break

    else:
        print("Invalid choice. Please enter a number from 1 to 6.")
