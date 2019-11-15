from ui import UI
from services import Services
from student import Student


def add_demo_students(students):
    students.append(Student(1, 'Gigel', 1))
    students.append(Student(2, 'Andrei', 3))
    students.append(Student(3, 'Vasile', 2))
    students.append(Student(4, 'Flaviu', 3))
    students.append(Student(5, 'Alex', 1))
    students.append(Student(6, 'Roxana', 2))
    students.append(Student(7, 'Andreea', 1))
    students.append(Student(8, 'Iulia', 2))
    students.append(Student(9, 'Ana', 1))
    students.append(Student(10, 'Ada', 3))
    students.append(Student(11, 'Raisa', 4))


def main():
    students = []
    history = []
    add_demo_students(students)
    services = Services(students, history)
    ui = UI(services)
    ui.start_menu()


main()
