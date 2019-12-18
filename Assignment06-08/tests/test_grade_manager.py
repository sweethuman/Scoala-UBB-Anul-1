from unittest import TestCase

from managers import StudentManager, DisciplineManager, GradeManager
from repositories import Repository
from structures import Discipline, Student, Grade


class TestGradeManager(TestCase):
    def test_get_discipline_grades(self):
        student_manager = StudentManager(Repository(Student, int, lambda value: value.id))
        discipline_manager = DisciplineManager(Repository(Discipline, int, lambda value: value.id))
        grade_manager = GradeManager(student_manager, discipline_manager)
        student_manager.add_student(Student(1, "Elon"))
        student_manager.add_student(Student(2, "Mustard"))
        student_manager.add_student(Student(3, "Dude"))
        discipline_manager.add_discipline(Discipline(1, "Maths"))
        discipline_manager.add_discipline(Discipline(2, "Fundamentals"))
        discipline_manager.add_discipline(Discipline(3, "Arhitecture"))
        grade1 = Grade(1, 1, 3.5)
        grade2 = Grade(1, 2, 4.5)
        grade3 = Grade(2, 1, 6)
        grade4 = Grade(3, 2, 7)
        grade5 = Grade(3, 3, 9)
        grade_manager.add_grade(grade1)
        grade_manager.add_grade(grade2)
        grade_manager.add_grade(grade3)
        grade_manager.add_grade(grade4)
        grade_manager.add_grade(grade5)
        self.assertEqual([grade1, grade2], grade_manager.get_discipline_grades(1))
        self.assertEqual([grade4, grade5], grade_manager.get_discipline_grades(3))

    def test_get_student_grades(self):
        student_manager = StudentManager(Repository(Student, int, lambda value: value.id))
        discipline_manager = DisciplineManager(Repository(Discipline, int, lambda value: value.id))
        grade_manager = GradeManager(student_manager, discipline_manager)
        student_manager.add_student(Student(1, "Elon"))
        student_manager.add_student(Student(2, "Mustard"))
        student_manager.add_student(Student(3, "Dude"))
        discipline_manager.add_discipline(Discipline(1, "Maths"))
        discipline_manager.add_discipline(Discipline(2, "Fundamentals"))
        discipline_manager.add_discipline(Discipline(3, "Arhitecture"))
        grade1 = Grade(1, 1, 3.5)
        grade2 = Grade(1, 2, 4.5)
        grade3 = Grade(2, 1, 6)
        grade4 = Grade(3, 2, 7)
        grade5 = Grade(3, 3, 9)
        grade_manager.add_grade(grade1)
        grade_manager.add_grade(grade2)
        grade_manager.add_grade(grade3)
        grade_manager.add_grade(grade4)
        grade_manager.add_grade(grade5)
        self.assertEqual([grade1, grade3], grade_manager.get_student_grades(1))
        self.assertEqual([grade2, grade4], grade_manager.get_student_grades(2))

    def test_add_grade(self):
        student_manager = StudentManager(Repository(Student, int, lambda value: value.id))
        discipline_manager = DisciplineManager(Repository(Discipline, int, lambda value: value.id))
        grade_manager = GradeManager(student_manager, discipline_manager)
        student_manager.add_student(Student(1, "Elon"))
        discipline_manager.add_discipline(Discipline(1, "Maths"))
        grade = Grade(1, 1, 3.5)
        grade_manager.add_grade(grade)
        self.assertEqual([grade], grade_manager.grades)

    def test_remove_all_discipline_grades(self):
        student_manager = StudentManager(Repository(Student, int, lambda value: value.id))
        discipline_manager = DisciplineManager(Repository(Discipline, int, lambda value: value.id))
        grade_manager = GradeManager(student_manager, discipline_manager)
        student_manager.add_student(Student(1, "Elon"))
        student_manager.add_student(Student(2, "Mustard"))
        student_manager.add_student(Student(3, "Dude"))
        discipline_manager.add_discipline(Discipline(1, "Maths"))
        discipline_manager.add_discipline(Discipline(2, "Fundamentals"))
        discipline_manager.add_discipline(Discipline(3, "Arhitecture"))
        grade1 = Grade(1, 1, 3.5)
        grade2 = Grade(1, 2, 4.5)
        grade3 = Grade(2, 1, 6)
        grade4 = Grade(3, 2, 7)
        grade5 = Grade(3, 3, 9)
        grade_manager.add_grade(grade1)
        grade_manager.add_grade(grade2)
        grade_manager.add_grade(grade3)
        grade_manager.add_grade(grade4)
        grade_manager.add_grade(grade5)
        grade_manager.remove_all_discipline_grades(2)
        self.assertEqual([grade1, grade2, grade4, grade5], grade_manager.grades)

    def test_remove_all_student_grades(self):
        student_manager = StudentManager(Repository(Student, int, lambda value: value.id))
        discipline_manager = DisciplineManager(Repository(Discipline, int, lambda value: value.id))
        grade_manager = GradeManager(student_manager, discipline_manager)
        student_manager.add_student(Student(1, "Elon"))
        student_manager.add_student(Student(2, "Mustard"))
        student_manager.add_student(Student(3, "Dude"))
        discipline_manager.add_discipline(Discipline(1, "Maths"))
        discipline_manager.add_discipline(Discipline(2, "Fundamentals"))
        discipline_manager.add_discipline(Discipline(3, "Arhitecture"))
        grade1 = Grade(1, 1, 3.5)
        grade2 = Grade(1, 2, 4.5)
        grade3 = Grade(2, 1, 6)
        grade4 = Grade(3, 2, 7)
        grade5 = Grade(3, 3, 9)
        grade_manager.add_grade(grade1)
        grade_manager.add_grade(grade2)
        grade_manager.add_grade(grade3)
        grade_manager.add_grade(grade4)
        grade_manager.add_grade(grade5)
        grade_manager.remove_all_student_grades(2)
        self.assertEqual([grade1, grade3, grade5], grade_manager.grades)

    # def test_failing_students_ids(self):
    #     self.fail()
    #
    # def test_best_students_ids(self):
    #     self.fail()
    #
    # def test_best_disciplines_ids(self):
    #     self.fail()
