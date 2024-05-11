class Student:
    def __init__(self, code, name):
        self._code = code
        self._name = name
        self._marks = 0

    @property
    def code(self):
        return self._code
    
    @code.setter
    def code(self, value):
        self._code = value
    
    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, value):
        self._name = value

    @property
    def marks(self):
        return self._marks
    
    @marks.setter
    def marks(self, value: int):
        if value > 10 or value < 0:
            raise ValueError("Marks must be between 0 and 10")
        self._marks = value

    def __str__(self):
        return f"{self._code} - {self._name} - {self._marks}"
    
    def input(self):
        self._name = input("Enter student new name: ")
        self._marks = float(input("Enter student new mark: "))

    def output(self):
        print(self.__str__() + "\n")