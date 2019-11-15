from unittest import TestCase
from student import Student
from services import Services
import copy


class TestServices(TestCase):
    def test_students(self):
        students = [Student(3, 'Malignen', 4)]
        history = []
        services = Services(students, history)
        self.assertEqual(students, services.students)

    def test_history(self):
        students = [Student(3, 'Malignen', 4)]
        history = [[Student(3, 'Malignen', 4)]]
        services = Services(students, history)
        self.assertEqual(history, services.history)

    def test_add_to_history(self):
        students = [Student(3, 'Malignen', 4)]
        history = []
        history = [students]
        services = Services(students, history)
        services.add_to_history()
        self.assertEqual(history, services.history)

    def test_add_student(self):
        students = [Student(3, 'Malignen', 4)]
        history = []
        services = Services(copy.deepcopy(students), history)
        test_student = Student(4, 'Maca', 6)
        services.add_student(test_student)
        students.append(test_student)
        self.assertEqual(students, services.students)

    def test_undo(self):
        students = [Student(3, 'Malignen', 4), Student(4, 'Macha', 6)]
        previous_state = [Student(3, 'Malignen', 4)]
        history = [previous_state]
        services = Services(students, history)
        services.undo()
        self.assertEqual(previous_state, services.students)

    def test_check_unique_id(self):
        students = [Student(3, 'Malignen', 4), Student(9, 'Albastru', 2)]
        history = []
        services = Services(students, history)
        self.assertEqual(True, services.check_unique_id(5))
        self.assertEqual(True, services.check_unique_id(1))
        self.assertEqual(False, services.check_unique_id(3))
        self.assertEqual(False, services.check_unique_id(9))

    def test_delete_student_by_index(self):
        students = [Student(3, 'Malignen', 4), Student(9, 'Albastru', 2), Student(6, 'Albastru', 2)]
        history = []
        services = Services(students, history)
        services.delete_student_by_index(1)
        self.assertEqual([Student(3, 'Malignen', 4), Student(6, 'Albastru', 2)], services.students)

    def test_filter_students_group(self):
        students = [Student(1, 'Gigel', 1), Student(2, 'Andrei', 3), Student(3, 'Vasile', 2), Student(4, 'Flaviu', 3),
                    Student(5, 'Alex', 1), Student(6, 'Roxana', 2), Student(7, 'Andreea', 1), Student(8, 'Iulia', 2),
                    Student(9, 'Ana', 1), Student(10, 'Ada', 3), Student(11, 'Raisa', 4)]
        services = Services(students, [])
        students = [Student(1, 'Gigel', 1), Student(3, 'Vasile', 2), Student(5, 'Alex', 1), Student(6, 'Roxana', 2),
                    Student(7, 'Andreea', 1), Student(8, 'Iulia', 2), Student(9, 'Ana', 1), Student(11, 'Raisa', 4)]
        services.filter_students_group(3)
        self.assertEqual(students, services.students)
