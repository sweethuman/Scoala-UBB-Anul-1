from unittest import TestCase

from managers import StudentManager
from repositories import Repository
from structures import Student


class TestStudentManager(TestCase):
    def test_add_student(self):
        student_manager = StudentManager(Repository(Student, int, lambda value: value.id))
        student = Student(1, "Gigiel")
        student_manager.add_student(student)
        self.assertEqual(student_manager.students, [student])

    def test_remove_student(self):
        student_manager = StudentManager(Repository(Student, int, lambda value: value.id))
        student = Student(1, "Gigiel")
        student2 = Student(2, "Gel")
        student3 = Student(3, "Andrei")
        student_manager.add_student(student)
        student_manager.add_student(student2)
        student_manager.add_student(student3)
        student_manager.remove_student(student2.id)
        self.assertListEqual(
            sorted([student, student3], key=lambda value: value.id, reverse=True), student_manager.students,
        )

    def test_retrieve_student(self):
        student_manager = StudentManager(Repository(Student, int, lambda value: value.id))
        student = Student(1, "Gigiel")
        student2 = Student(2, "Gel")
        student3 = Student(3, "Andrei")
        student_manager.add_student(student)
        student_manager.add_student(student2)
        student_manager.add_student(student3)
        self.assertEqual(student_manager.retrieve_student(2), student2)

    def test_search(self):
        student_manager = StudentManager(Repository(Student, int, lambda value: value.id))
        student = Student(1, "Gigiel")
        student2 = Student(2, "Giel")
        student3 = Student(3, "Andrei")
        student_manager.add_student(student)
        student_manager.add_student(student2)
        student_manager.add_student(student3)
        self.assertEqual(student_manager.search("gi"), [student, student2])

    def test_student_id_exists(self):
        student_manager = StudentManager(Repository(Student, int, lambda value: value.id))
        student = Student(1, "Gigiel")
        student2 = Student(2, "Giel")
        student3 = Student(3, "Andrei")
        student_manager.add_student(student)
        student_manager.add_student(student2)
        student_manager.add_student(student3)
        self.assertEqual(student_manager.student_id_exists(2), True)
        self.assertEqual(student_manager.student_id_exists(5), False)

    def test_last_student_id(self):
        student_manager = StudentManager(Repository(Student, int, lambda value: value.id))
        student = Student(1, "Gigiel")
        student2 = Student(2, "Giel")
        student3 = Student(3, "Andrei")
        student_manager.add_student(student)
        student_manager.add_student(student2)
        student_manager.add_student(student3)
        self.assertEqual(3, student_manager.last_student_id)
