from collections import OrderedDict
from typing import Dict, List

from errors import DuplicateIdError, MissingIdError
from structures import FunctionCall, Operation
from structures.student import Student


class StudentManager:
    def __init__(self):
        self.__students: Dict[int, Student] = OrderedDict()

    def add_student(self, student: Student):
        """
        Adds a student, if id already exists throws a L{DuplicateIdError}
        @param student: The Student you want to add
        """
        if self.__students.get(student.id) is not None:
            raise DuplicateIdError("Student Id already exists")
        self.__students[student.id] = student

        self.__students = OrderedDict(sorted(self.__students.items(), key=lambda t: t[0]))
        undo = FunctionCall(self.remove_student, student.id)
        redo = FunctionCall(self.add_student, student)
        return Operation(undo, redo)

    def remove_student(self, student_id: int):
        """
        Removes a id, if id doesn't exist it throws a L{MissingIdError}
        @param student_id: The Student object with the id you want to remove
        """
        if self.__students.get(student_id) is None:
            raise MissingIdError("Student with given id does not exist")
        student = self.__students.pop(student_id)
        undo = FunctionCall(self.add_student, student)
        redo = FunctionCall(self.remove_student, student_id)
        return Operation(undo, redo)

    def retrieve_student(self, student_id: int):
        """
        Retrieves a student, if id doesn't exist it throws a L{MissingIdError}
        @param student_id: The Student with the id you want to remove
        @return: The Student Object
        """
        if self.__students.get(student_id) is None:
            raise MissingIdError("Student with given id does not exist")
        return self.__students[student_id]

    def search(self, term: str):
        """
        Search student with id or name that at least partially matches(case insensitive)
        @param term: the term to search for
        @return: All the Student Objects that match
        """
        term = term.lower()
        results: List[Student] = []
        for student in self.__students.values():
            if term in str(student.id) or term in student.name.lower():
                results.append(student)
        return results

    def student_id_exists(self, student_id):
        """
        Checks if the given student id already exists
        @param student_id: the id to check for
        @return: True or False
        """
        if self.__students.get(student_id) is None:
            return False
        return True

    @property
    def last_student_id(self):
        """
        The Last Used student id
        @return: Just the id
        """
        if len(self.__students.keys()) == 0:
            return 0
        return list(self.__students.keys())[-1]

    @property
    def students(self):
        return list(self.__students.values())
