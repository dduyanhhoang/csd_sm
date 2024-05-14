from typing import Optional
from .student import Student


class StudentManager(list):
    def __str__(self) -> str:
        if not self:
            return f"\n** No students currently in the list\n"

        students = "\n** Students list\n** Format: Code - Name - Marks\n"
        for student in self:
            students += str(student) + "\n"

        return students

    def add_student(self, student: Student) -> None:
        if not isinstance(student, Student):
            raise ValueError("\n** You can only add Student to StudentManager\n")

        if any(s.code == student.code for s in self):
            raise ValueError(f"\n**Student with code {student.code} already exists\n")

        self.append(student)
        print(f"\n** Student {student.code} added successfully\n")

    def remove_student_by_code(self, code: str) -> bool:
        if not self:
            print(f"\n** No students currently in the list\n")
            return False
        
        for student in self:
            if student.code == code:
                self.remove(student)
                print(f"\n** Student with code {code} removed successfully\n")
                return True

        print(f"\n** Student with code {code} not found\n")
        return False

    def get_student_by_name(self, name: str) -> Optional[Student]:
        if not self:
            print(f"\n** No students currently in the list\n")
            return None

        for student in self:
            if student.name == name:
                print("\n** Student found:")
                print(student)
                return student

        print(f"\n** Student with the name {name} not found\n")
        return None

    def update_student_by_code(self, code: str) -> bool:
        if not self:
            print(f"\n** No students currently in the list\n")
            return False

        for student in self:
            if student.code == code:
                print(f"\n**Student with code {code} found and ready for update:")
                student.input()
                return True

        print(f"\n** Student with code {code} not found\n")
        return False
