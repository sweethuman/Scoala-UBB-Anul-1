from typing import List
from protocols import FileStorable


class Student:
    def __init__(self, student_id: int, name: str):
        self.__id = student_id
        self.__name = name

    @property
    def id(self):
        return self.__id

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value: str):
        self.__name = value

    @staticmethod
    def write_to_file(element: "Student") -> List[str]:
        text = [str(element.id), str(element.name)]
        return text

    @staticmethod
    def read_from_file(*args: str) -> "Student":
        return Student(int(args[0]), args[1])
