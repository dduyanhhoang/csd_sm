import os
from .student import Student
from .student_manager import StudentManager


class Menu:
    def __init__(self):
        self.students = StudentManager()

    @staticmethod
    def clear_screen():
        if os.name == 'nt':
            os.system('cls')
        else:
            os.system('clear')

    def add_student(self):
        code =