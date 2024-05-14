class Student:
    def __init__(self, code, name):
        self.code = code
        self.name = name
        self.marks = 0

    @property
    def code(self):
        return self._code
    
    @code.setter
    def code(self, value):
        if not value:
            raise ValueError('Student\'s code cannot be empty')

        # More student code validations go here
        self._code = value
    
    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, value):
        if not value:
            raise ValueError('Student\'s name cannot be empty')
        self._name = value

    @property
    def marks(self):
        return self._marks
    
    @marks.setter
    def marks(self, value: int):
        if not (0 <= value <= 10):
            raise ValueError("Marks must be between 0 and 10")
        self._marks = value

    def __str__(self):
        return f"{self.code} - {self.name} - {self.marks}"

    def input(self):
        self.name = input("Enter student\'s name: ")
        while True:
            try:
                self.marks = float(input("Enter student\'s marks: "))
                break
            except ValueError as e:
                print(e)

    def output(self):
        print(self.__str__())
