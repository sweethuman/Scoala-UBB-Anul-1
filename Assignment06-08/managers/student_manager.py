from collections import OrderedDict
from typing import Dict, List

from errors import DuplicateIdError, MissingIdError
from structures import FunctionCall, Operation
from structures.student import Student
from repositories import Repository


class StudentManager:
    def __init__(self, repository: Repository[Student, int]):
        self.__repository = repository

    def add_student(self, student: Student) -> Operation:
        """
        Adds a student, if id already exists throws a L{DuplicateIdError}
        @param student: The Student you want to add
        """
        if self.__repository.exists_element(student.id) is True:
            raise DuplicateIdError("Student Id already exists")
        self.__repository.add_element(student)
        undo = FunctionCall(self.remove_student, student.id)
        redo = FunctionCall(self.add_student, student)
        return Operation(undo, redo)

    def remove_student(self, student_id: int) -> Operation:
        """
        Removes a id, if id doesn't exist it throws a L{MissingIdError}
        @param student_id: The Student object with the id you want to remove
        """
        if self.__repository.exists_element(student_id) is False:
            raise MissingIdError("Student with given id does not exist")
        student = self.__repository.remove_element(student_id)
        undo = FunctionCall(self.add_student, student)
        redo = FunctionCall(self.remove_student, student_id)
        return Operation(undo, redo)

    def retrieve_student(self, student_id: int):
        """
        Retrieves a student, if id doesn't exist it throws a L{MissingIdError}
        @param student_id: The Student with the id you want to remove
        @return: The Student Object
        """
        if self.__repository.exists_element(student_id) is False:
            raise MissingIdError("Student with given id does not exist")
        return self.__repository.get_element(student_id)

    def student_id_exists(self, student_id):
        """
        Checks if the given student id already exists
        @param student_id: the id to check for
        @return: True or False
        """
        return self.__repository.exists_element(student_id)

    def search(self, term: str):
        """
        Search student with id or name that at least partially matches(case insensitive)
        @param term: the term to search for
        @return: All the Student Objects that match
        """
        term = term.lower()
        results: List[Student] = []
        for student in self.__repository.get_all:
            if term in str(student.id) or term in student.name.lower():
                results.append(student)
        return results

    @property
    def last_student_id(self):
        """
        The Last Used student id
        @return: Just the id
        """
        if len(self.__repository.get_all) == 0:
            return 0
        return sorted(self.__repository.get_all, key=lambda student: student.id)[-1].id

    @property
    def students(self):
        return sorted(self.__repository.get_all, key=lambda student: student.id, reverse=True)
