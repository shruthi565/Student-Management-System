import json

# -----------------------------
# File name
# -----------------------------
FILE_NAME = "students.json"


# -----------------------------
# Load students from JSON file
# -----------------------------
def load_students():
    try:
        with open(FILE_NAME, "r") as file:
            return json.load(file)

    except FileNotFoundError:
        return []

    except json.JSONDecodeError:
        print("Error reading student data. Starting with empty data.")
        return []


# -----------------------------
# Save students to JSON file
# -----------------------------
def save_students(students):
    with open(FILE_NAME, "w") as file:
        json.dump(students, file, indent=4)


# -----------------------------
# Add Student
# -----------------------------
def add_student(students):
    try:
        student_id = int(input("Enter student ID: "))

        # Check duplicate ID
        for student in students:
            if student["id"] == student_id:
                print("Student ID already exists.")
                return

        name = input("Enter student name: ").strip()

        if name == "":
            print("Name cannot be empty.")
            return

        mark1 = float(input("Enter marks for Subject 1: "))
        mark2 = float(input("Enter marks for Subject 2: "))
        mark3 = float(input("Enter marks for Subject 3: "))

        # Check marks
        if not (0 <= mark1 <= 100):
            print("Subject 1 marks must be between 0 and 100.")
            return

        if not (0 <= mark2 <= 100):
            print("Subject 2 marks must be between 0 and 100.")
            return

        if not (0 <= mark3 <= 100):
            print("Subject 3 marks must be between 0 and 100.")
            return

        student = {
            "id": student_id,
            "name": name,
            "marks": [mark1, mark2, mark3]
        }

        students.append(student)
        save_students(students)

        print("Student added successfully!")

    except ValueError:
        print("Please enter valid numbers.")


# -----------------------------
# View Students
# -----------------------------
def view_students(students):
    if len(students) == 0:
        print("No students found.")
        return

    print("\n========== STUDENT DETAILS ==========")

    for student in students:
        print("ID:", student["id"])
        print("Name:", student["name"])
        print("Marks:", student["marks"])
        print("-------------------------------------")


# -----------------------------
# Search Student
# -----------------------------
def search_student(students):
    try:
        search_id = int(input("Enter student ID to search: "))

        for student in students:
            if student["id"] == search_id:
                print("\n========== STUDENT FOUND ==========")
                print("ID:", student["id"])
                print("Name:", student["name"])
                print("Marks:", student["marks"])
                return

        print("Student not found.")

    except ValueError:
        print("Please enter a valid student ID.")


# -----------------------------
# Update Student
# -----------------------------
def update_student(students):
    try:
        update_id = int(input("Enter student ID to update: "))

        for student in students:
            if student["id"] == update_id:

                print("\nStudent found!")

                name = input("Enter new name: ").strip()

                if name == "":
                    print("Name cannot be empty.")
                    return

                mark1 = float(input("Enter new marks for Subject 1: "))
                mark2 = float(input("Enter new marks for Subject 2: "))
                mark3 = float(input("Enter new marks for Subject 3: "))

                if not (0 <= mark1 <= 100):
                    print("Marks must be between 0 and 100.")
                    return

                if not (0 <= mark2 <= 100):
                    print("Marks must be between 0 and 100.")
                    return

                if not (0 <= mark3 <= 100):
                    print("Marks must be between 0 and 100.")
                    return

                student["name"] = name
                student["marks"] = [mark1, mark2, mark3]

                save_students(students)

                print("Student updated successfully!")
                return

        print("Student not found.")

    except ValueError:
        print("Please enter valid numbers.")


# -----------------------------
# Delete Student
# -----------------------------
def delete_student(students):
    try:
        delete_id = int(input("Enter student ID to delete: "))

        for student in students:
            if student["id"] == delete_id:

                students.remove(student)
                save_students(students)

                print("Student deleted successfully!")
                return

        print("Student not found.")

    except ValueError:
        print("Please enter a valid student ID.")


# -----------------------------
# Calculate Average
# -----------------------------
def calculate_average(students):
    try:
        search_id = int(input("Enter student ID: "))

        for student in students:

            if student["id"] == search_id:

                marks = student["marks"]

                total = sum(marks)
                average = total / len(marks)

                print("\n========== RESULT ==========")
                print("Name:", student["name"])
                print("Total Marks:", total)
                print("Average:", round(average, 2))

                if average >= 40:
                    print("Result: PASS")
                else:
                    print("Result: FAIL")

                return

        print("Student not found.")

    except ValueError:
        print("Please enter a valid student ID.")


# -----------------------------
# Find Top Student
# -----------------------------
def top_student(students):

    if len(students) == 0:
        print("No students found.")
        return

    best_student = students[0]

    best_average = (
        sum(best_student["marks"]) /
        len(best_student["marks"])
    )

    for student in students:

        average = (
            sum(student["marks"]) /
            len(student["marks"])
        )

        if average > best_average:
            best_student = student
            best_average = average

    print("\n========== TOP STUDENT ==========")
    print("ID:", best_student["id"])
    print("Name:", best_student["name"])
    print("Marks:", best_student["marks"])
    print("Average:", round(best_average, 2))


# -----------------------------
# Main Program
# -----------------------------
def main():

    students = load_students()

    while True:

        print("\n====================================")
        print("      STUDENT MANAGEMENT SYSTEM")
        print("====================================")

        print("1. Add Student")
        print("2. View Students")
        print("3. Search Student")
        print("4. Update Student")
        print("5. Delete Student")
        print("6. Calculate Average")
        print("7. Show Top Student")
        print("8. Exit")

        choice = input("\nEnter your choice: ")

        if choice == "1":
            add_student(students)

        elif choice == "2":
            view_students(students)

        elif choice == "3":
            search_student(students)

        elif choice == "4":
            update_student(students)

        elif choice == "5":
            delete_student(students)

        elif choice == "6":
            calculate_average(students)

        elif choice == "7":
            top_student(students)

        elif choice == "8":
            print("\nThank you for using Student Management System!")
            break

        else:
            print("Invalid choice. Please enter 1 to 8.")


# -----------------------------
# Start Program
# -----------------------------
if __name__ == "__main__":
    main()