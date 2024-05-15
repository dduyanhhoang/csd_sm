import re


class Student:
    def __init__(self, code, name):
        self.code = code
        self.name = name
        self.marks = 0

    @property
    def code(self):
        return self._code

    @classmethod
    def validate_code(cls, value: str) -> str:
        pattern = r'^(?:SE|AI|IA|IS)(?:0[1-9]|1[0-8])\d{4}$'
        if not re.match(pattern, value):
            raise ValueError('Invalid student\'s code')
        return value

    @code.setter
    def code(self, value):
        self.validate_code(value)
        self._code = value
    
    @property
    def name(self):
        return self._name

    @classmethod
    def validate_name(cls, value: str) -> str:
        if not value:
            raise ValueError('Student\'s name cannot be empty')
        return value

    @name.setter
    def name(self, value):
        self.validate_name(value)
        self._name = value

    @property
    def marks(self):
        return self._marks

    @classmethod
    def validate_marks(cls, value: float) -> float:
        if not (0 <= value <= 10):
            raise ValueError('Student\'s marks must be between 0 and 10')
        return value

    @marks.setter
    def marks(self, value: float):
        self.validate_marks(value)
        self._marks = value

    def __str__(self):
        return f"{self.code} - {self.name} - {self.marks}"

    def input(self):
        self.name = input("Enter student\'s name modification: ")
        while True:
            try:
                self.marks = float(input("Enter student\'s new mark: "))
                break
            except ValueError as e:
                print(e)

    def output(self):
        print(self.__str__())
