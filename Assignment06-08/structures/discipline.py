from typing import List


class Discipline:
    def __init__(self, discipline_id: int, name: str):
        self.__id = discipline_id
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
    def write_to_file(element: "Discipline") -> List[str]:
        text = [str(element.id), str(element.name)]
        return text

    @staticmethod
    def read_from_file(*args: str) -> "Discipline":
        return Discipline(int(args[0]), args[1])
