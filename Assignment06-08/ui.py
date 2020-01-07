from typing import List, Union

from controllers import UndoController
from errors import MissingIdError
from managers.discipline_manager import DisciplineManager
from managers.grade_manager import GradeManager
from managers.student_manager import StudentManager
from structures import (
    Student,
    Discipline,
    Grade,
    CascadedOperation,
    FunctionCall,
    Operation,
)
from data_types import my_filter


class UI:
    def __init__(
        self,
        student_manager: StudentManager,
        discipline_manager: DisciplineManager,
        grade_manager: GradeManager,
        undo_controller: UndoController,
    ):
        self.student_manager = student_manager
        self.discipline_manager = discipline_manager
        self.grade_manager = grade_manager

        self.undo_controller = undo_controller

    @staticmethod
    def print_menu():
        print(
            "\n1. Add Student or Discipline\n"
            "2. Remove Student or Discipline\n"
            "3. Update Student or Discipline\n"
            "4. List Students or Disciplines\n"
            "5. Grade a Student at a Discipline\n"
            "6. Display grades for Discipline or Student\n"
            "7. Search for Disciplines or Students\n"
            "8. See Statistics \n"
            "9. Undo \n"
            "10. Redo \n"
            "11. Show Students where Id is Odd \n"
        )

    @staticmethod
    def print_submenu_8():
        print(
            "1. All students failing at one or more disciplines\n"
            "2. Students with the best school situation, sorted in descending order of their aggregated average\n"
            "3. All disciplines at which there is at least one grade, sorted in descending order of "
            "the average grade received by all students enrolled at that discipline"
        )

    @staticmethod
    def selected_option():
        while True:
            read_input = input("Select Student(1) or Discipline(2): ")
            if read_input == "1":
                return 1
            elif read_input == "2":
                return 2
            else:
                print("Sorry. Wrong value. \n")

    def executioner(self):
        while True:
            self.print_menu()
            read_input = input("Please select an option: ")
            if read_input == "1":
                if self.selected_option() == 1:
                    student = self.read_student()
                    operation = self.student_manager.add_student(student)
                    self.undo_controller.record_operation(operation)
                    print("Student Added")
                else:
                    discipline = self.read_discipline()
                    operation = self.discipline_manager.add_discipline(discipline)
                    self.undo_controller.record_operation(operation)
                    print("Discipline Added")
            elif read_input == "2":
                if self.selected_option() == 1:
                    print("List of students")
                    self.print_students_disciplines(self.student_manager.students)
                    read_id = input("Enter Student id:")
                    try:
                        read_id = int(read_id)
                        student_operation = self.student_manager.remove_student(read_id)
                        try:
                            grade_operation = self.grade_manager.remove_all_student_grades(read_id)
                        except KeyError:
                            print("There were no grades to remove for student")
                            self.undo_controller.record_operation(student_operation)
                        else:
                            self.undo_controller.record_operation(CascadedOperation(student_operation, grade_operation))
                        print("Student Removed")
                    except ValueError:
                        print("Entered value is not a valid number")
                    except MissingIdError as e:
                        print(e)
                else:
                    print("List of disciplines")
                    self.print_students_disciplines(self.discipline_manager.disciplines)
                    read_id = input("Enter Discipline id:")
                    try:
                        read_id = int(read_id)
                        discipline_operation = self.discipline_manager.remove_discipline(read_id)
                        try:
                            grade_operation = self.grade_manager.remove_all_discipline_grades(read_id)
                        except KeyError:
                            print("There were no grades to remove for discipline")
                            self.undo_controller.record_operation(discipline_operation)
                        else:
                            self.undo_controller.record_operation(
                                CascadedOperation(discipline_operation, grade_operation)
                            )
                        print("Discipline Removed")
                    except ValueError:
                        print("Entered value is not a valid number")
                    except MissingIdError as e:
                        print(e)
            elif read_input == "3":
                if self.selected_option() == 1:
                    print("List of students")
                    self.print_students_disciplines(self.student_manager.students)
                    read_id = input("Enter Student id:")
                    try:
                        read_id = int(read_id)
                        student = self.student_manager.retrieve_student(read_id)
                        read_name = input("Enter new student Name:")

                        def set_student_name(student: Student, name: str):
                            student.name = name

                        undo = FunctionCall(set_student_name, student, student.name)
                        redo = FunctionCall(set_student_name, student, read_name)
                        self.undo_controller.record_operation(Operation(undo, redo))
                        student.name = read_name
                        print("Student Updated")
                    except ValueError:
                        print("Entered value is not a valid number")
                    except MissingIdError as e:
                        print(e)
                else:
                    print("List of disciplines")
                    self.print_students_disciplines(self.discipline_manager.disciplines)
                    read_id = input("Enter Discipline id:")
                    try:
                        read_id = int(read_id)
                        discipline = self.discipline_manager.retrieve_discipline(read_id)
                        read_name = input("Enter new discipline Name:")

                        def set_discipline_name(discipline: Discipline, name: str):
                            discipline.name = name

                        undo = FunctionCall(set_discipline_name, discipline, discipline.name)
                        redo = FunctionCall(set_discipline_name, discipline, read_name)
                        self.undo_controller.record_operation(Operation(undo, redo))
                        discipline.name = read_name
                        print("Discipline Updated")
                    except ValueError:
                        print("Entered value is not a valid number")
                    except MissingIdError as e:
                        print(e)
            elif read_input == "4":
                if self.selected_option() == 1:
                    self.print_students_disciplines(self.student_manager.students)
                else:
                    self.print_students_disciplines(self.discipline_manager.disciplines)
            elif read_input == "5":
                try:
                    print("List of students:")
                    self.print_students_disciplines(self.student_manager.students)
                    read_student_id = input("Enter Student id:")
                    read_student_id = int(read_student_id)
                    print("List of disciplines:")
                    print("Help")
                    self.print_students_disciplines(self.discipline_manager.disciplines)
                    read_discipline_id = input("Enter Student id:")
                    read_discipline_id = int(read_discipline_id)
                    read_grade_value = input("Enter Student grade:")
                    read_grade_value = float(read_grade_value)
                    grade = Grade(read_discipline_id, read_student_id, read_grade_value)
                    operation = self.grade_manager.add_grade(grade)
                    self.undo_controller.record_operation(operation)
                    print("Grade added!")
                except ValueError:
                    print("Entered value is not a valid number")
                except MissingIdError as e:
                    print(e)
            elif read_input == "6":
                if self.selected_option() == 1:
                    print("List of students:")
                    self.print_students_disciplines(self.student_manager.students)
                    read_id = input("Enter Student Id: ")
                    try:
                        read_id = int(read_id)
                        self.print_grades(self.grade_manager.get_student_grades(read_id))
                    except ValueError:
                        print("Entered value is not a number!")
                    except KeyError:
                        print("Student with id is not graded yet")
                else:
                    print("List of disciplines:")
                    self.print_students_disciplines(self.discipline_manager.disciplines)
                    read_id = input("Enter Discipline Id: ")
                    try:
                        read_id = int(read_id)
                        self.print_grades(self.grade_manager.get_discipline_grades(read_id))
                    except ValueError:
                        print("Entered value is not a number!")
                    except KeyError:
                        print("Discipline with id is not graded yet")
            elif read_input == "7":
                if self.selected_option() == 1:
                    read_input = input("Enter Student term to search for: ")
                    result = self.student_manager.seElonarch(read_input)
                    self.print_students_disciplines(result)
                else:
                    read_input = input("Enter Discipline term to search for: ")
                    result = self.discipline_manager.search(read_input)
                    self.print_students_disciplines(result)
            elif read_input == "8":
                self.print_submenu_8()
                selected_statistic = input("Select a statistic: ")
                if selected_statistic == "1":
                    students = [
                        self.student_manager.retrieve_student(student_id)
                        for student_id in sorted(self.grade_manager.failing_students_ids())
                    ]
                    self.print_students_disciplines(students)
                elif selected_statistic == "2":
                    students_with_average = [
                        (self.student_manager.retrieve_student(value[0]), value[1],)
                        for value in self.grade_manager.best_students_ids()
                    ]
                    for value in students_with_average:
                        print("{}. {}: {}".format(value[0].id, value[0].name, value[1]))
                elif selected_statistic == "3":
                    disciplines_with_average = [
                        (self.discipline_manager.retrieve_discipline(value[0]), value[1],)
                        for value in self.grade_manager.best_disciplines_ids()
                    ]
                    for value in disciplines_with_average:
                        print("{}. {}: {}".format(value[0].id, value[0].name, value[1]))
            elif read_input == "9":
                try:
                    self.undo_controller.undo()
                except IndexError:
                    print("Undo History is empty!")
            elif read_input == "10":
                try:
                    self.undo_controller.redo()
                except IndexError:
                    print("Redo History is empty!")
            elif read_input == "11":

                def is_id_odd(obj: Student):
                    if obj.id % 2 == 1:
                        return True
                    return False

                self.print_students_disciplines(my_filter(self.student_manager.students, is_id_odd))

    def read_student(self):
        read_name = input("Enter student name: ")
        return Student(self.student_manager.last_student_id + 1, read_name)

    def read_discipline(self):
        read_name = input("Enter discipline name: ")
        return Discipline(self.discipline_manager.last_discipline_id + 1, read_name)

    @staticmethod
    def print_students_disciplines(elements: List[Union[Student, Discipline]]):
        for element in elements:
            print("{}. {}".format(element.id, element.name))
        print("")

    def print_grades(self, grades: List[Grade]):
        if len(grades) == 0:
            print("There are no grades")
        for grade in grades:
            student = self.student_manager.retrieve_student(grade.student_id)
            discipline = self.discipline_manager.retrieve_discipline(grade.discipline_id)
            print(
                "{}. {}, {}. {}, {}".format(
                    discipline.id, discipline.name, student.id, student.name, grade.grade_value,
                )
            )
