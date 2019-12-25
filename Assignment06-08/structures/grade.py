from typing import List


class Grade:
    def __init__(self, discipline_id: int, student_id: int, grade_value: float):
        self.__discipline_id = discipline_id
        self.__student_id = student_id
        self.__grade_value = grade_value

    @property
    def discipline_id(self):
        return self.__discipline_id

    @property
    def student_id(self):
        return self.__student_id

    @property
    def grade_value(self):
        return self.__grade_value

    @grade_value.setter
    def grade_value(self, value: float):
        self.__grade_value = value

    @staticmethod
    def write_to_file(element: "Grade") -> List[str]:
        text = [str(element.discipline_id), str(element.student_id), str(element.grade_value)]
        return text

    @staticmethod
    def read_from_file(*args: str) -> "Grade":
        return Grade(int(args[0]), int(args[1]), float(args[2]))
