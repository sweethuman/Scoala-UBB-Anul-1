import os
import pickle

from errors import MissingIdError
from managers import StudentManager, GradeManager, DisciplineManager
from structures import Grade, CascadedOperation, Operation, FunctionCall


class PickleGradeManager(GradeManager):
    def __init__(self, student_manager: StudentManager, discipline_manager: DisciplineManager, file_name: str):
        super().__init__(student_manager, discipline_manager)
        self._file_name = file_name
        self._load()

    def _load(self):
        if (
            not os.path.exists(os.getcwd() + "/" + self._file_name)
            or os.path.getsize(os.getcwd() + "/" + self._file_name) == 0
        ):
            return
        with open(self._file_name, "rb") as file:
            grades = pickle.load(file)
            for grade in grades:
                super().add_grade(grade)

    def _write_to_file(self):
        with open(self._file_name, "wb") as file:
            grades = []
            for grade_list in self._disciplines.values():
                for element in grade_list:
                    grades.append(element)
            pickle.dump(grades, file)

    def add_grade(self, grade: Grade) -> Operation:
        """
        Adds a grade, if the Student Id or Discipline Id does not exist it throws a L{MissingIdError}
        @param grade: The Grade object you want to add
        """
        if not self.student_manager.student_id_exists(grade.student_id):
            raise MissingIdError("Student with given id does not exist!")
        if not self.discipline_manager.discipline_id_exists(grade.discipline_id):
            raise MissingIdError("Discipline with given id does not exist!")
        if self._disciplines.get(grade.discipline_id) is None:
            self._disciplines[grade.discipline_id] = []
        if self._students.get(grade.student_id) is None:
            self._students[grade.student_id] = []
        self._disciplines[grade.discipline_id].append(grade)
        self._students[grade.student_id].append(grade)
        undo = FunctionCall(self._remove_any_grades, grade)
        redo = FunctionCall(self.add_grade, grade)
        self._write_to_file()
        return Operation(undo, redo)

    def remove_all_discipline_grades(self, discipline_id) -> Operation:
        """
        Remove all the grades of a discipline
        @param discipline_id: The Discipline Id
        """
        grades = self._disciplines.pop(discipline_id)
        operations = []
        for grade in grades:
            undo = FunctionCall(self.add_grade, grade)
            redo = FunctionCall(self._remove_any_grades, grade)
            operations.append(Operation(undo, redo))
            self._students[grade.student_id].remove(grade)
        self._write_to_file()
        return CascadedOperation(*operations)

    def remove_all_student_grades(self, student_id) -> Operation:
        """
        Remove all the grades of a student
        @param student_id: The Student Id
        """
        grades = self._students.pop(student_id)
        operations = []
        for grade in grades:
            undo = FunctionCall(self.add_grade, grade)
            redo = FunctionCall(self._remove_any_grades, grade)
            operations.append(Operation(undo, redo))
            self._disciplines[grade.discipline_id].remove(grade)
        self._write_to_file()
        return CascadedOperation(*operations)

    def _remove_any_grades(self, *grades: Grade) -> None:
        for grade in grades:
            self._disciplines[grade.discipline_id].remove(grade)
            self._students[grade.student_id].remove(grade)
        self._write_to_file()
