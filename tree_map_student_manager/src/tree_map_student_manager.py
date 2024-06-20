from tree_map import TreeMap
from student import Student


class TreeMapStudentManager(TreeMap):
    def __init__(self):
        super().__init__()

    def add_student(self, student):
        if not isinstance(student, Student):
            raise ValueError("Value must be a Student instance")
        self[student.sid] = student

    def get_student(self, sid):
        return self[sid]

    def update_student(self, student):
        if not isinstance(student, Student):
            raise ValueError("Value must be a Student instance")
        self[student.sid] = student

    def remove_student(self, sid):
        del self[sid]

    def get_first_student(self):
        position = self.first()
        return position.element() if position else None

    def get_last_student(self):
        position = self.last()
        return position.element() if position else None

    def find_students_in_range(self, start_sid, end_sid):
        for key, student in self.find_range(start_sid, end_sid):
            yield student

    def list_all_students(self):
        for sid in self:
            yield self[sid]

if __name__ == "__main__":
    manager = TreeMapStudentManager()

    # Create 10 student objects
    students = [
        Student("IB012345", "John Doe", "123456789", 2000),
        Student("IB012346", "Jane Smith", "987654321", 2001),
        Student("IB012347", "Alice Johnson", "234567890", 2002),
        Student("IB012348", "Bob Brown", "345678901", 2003),
        Student("IB012349", "Charlie Davis", "456789012", 2004),
        Student("IB012350", "Diana Evans", "567890123", 2005),
        Student("IB012351", "Ethan Harris", "678901234", 2006),
        Student("IB012352", "Fiona Clark", "789012345", 2007),
        Student("IB012353", "George Lewis", "890123456", 2008),
        Student("IB012354", "Hannah Walker", "901234567", 2009),
    ]

    # Add students to the manager
    for student in students:
        manager.add_student(student)

    # Display all students
    print("All students:")
    for student in manager.list_all_students():
        print(f"{student.sid}: {student.name}, {student.number}, {student.yob}")

    # Get and display a specific student
    print("\nGet student with sid 'IB012345':")
    student = manager.get_student("IB012345")
    print(f"{student.sid}: {student.name}, {student.number}, {student.yob}")

    # Update a student
    print("\nUpdate student with sid 'IB012345':")
    updated_student = Student("IB012345", "John Updated", "123456789", 2000)
    manager.update_student(updated_student)
    student = manager.get_student("IB012345")
    print(f"{student.sid}: {student.name}, {student.number}, {student.yob}")

    # Remove a student
    print("\nRemove student with sid 'IB012350':")
    manager.remove_student("IB012350")
    print("All students after removal:")
    for student in manager.list_all_students():
        print(f"{student.sid}: {student.name}, {student.number}, {student.yob}")

    # Get the first student
    print("\nFirst student:")
    first_position = manager.first()
    if first_position is not None:
        first_student = first_position.element()
        print(f"{first_student._key}: {first_student._value.name}, {first_student._value.number}, {first_student._value.yob}")

    # Get the last student
    print("\nLast student:")
    last_position = manager.last()
    if last_position is not None:
        last_student = last_position.element()
        print(f"{last_student._key}: {last_student._value.name}, {last_student._value.number}, {last_student._value.yob}")

    # Find students in a range
    print("\nStudents in range 'IB012346' to 'IB012352':")
    for student in manager.find_students_in_range("IB012346", "IB012352"):
        print(f"{student.sid}: {student.name}, {student.number}, {student.yob}")
