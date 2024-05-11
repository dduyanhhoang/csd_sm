import os
from student_manager import Student
from student_manager import StudentManager

# Not in use
def clear_screen():
    # For Windows
    if os.name == 'nt':
        os.system('cls')
    # For Unix (Linux, macOS)
    else:
        os.system('clear')

def menu():
    students = StudentManager()

    while True:
        print("1. Add student")
        print("2. Show students list")
        print("3. Remove student by code")
        print("4. Search student by name")
        print("5. Update student by code")
        print("6. Exit")
        option = input("Enter option: ")
        if option == "1":
            print()
            code = input("Enter student code: ")
            name = input("Enter student name: ")

            student = Student(code, name)
            students.add_student(student)
            print("\n**Student added successfully!\n")
            
        elif option == "2":
            print(students)
        elif option == "3":
            code = input("\nEnter student code: ")
            students.remove_student_by_code(code)
        elif option == "4":
            name = input("\nEnter student name: ")
            students.get_student_by_name(name)
        elif option == "5":
            code = input("\nEnter student code: ")
            students.update_student_by_code(code)
        elif option == "6":
            print("\n** Student manager stopped by user\n")
            break


def main():
    menu()


if __name__ == "__main__":
    main()
