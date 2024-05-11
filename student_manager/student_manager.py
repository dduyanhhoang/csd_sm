from .student import Student

class StudentManager(list):
    def __init__(self):
        self._students = list()

    def __str__(self) -> str:
        if not self._students:
            return f"\n** No students currently in the list\n"
        
        students = ""
        students += "\n** Students list\n"
        students += f"** Format: Code - Name - Marks\n"
        for student in self._students:
            students += str(student) + "\n"

        return students

    def add_student(self, student):
        if not isinstance(student, Student):
            raise ValueError("\n** You can only add Student objects\n")
        
        self._students.append(student)

    def remove_student_by_code(self, code):
        if not self._students:
            print(f"\n** No students currently in the list\n")
            return
        
        for student in self._students:
            if student.code == code:
                self._students.remove(student)
                break
        else:
            print(f"\n** Student with the code {code} not found\n")

    def get_student_by_name(self, name):
        for student in self._students:
            if student.name == name:
                print("\n** Student found in student manager\n")
                print(student)
                print()
                return
        else:
            print(f"\n** Student with the name {name} not found\n")

    def update_student_by_code(self, code):
        for student in self._students:
            if student.code == code:
                print("\n** Student found in student manager ready for update\n")
                student.input()
                print()
                break