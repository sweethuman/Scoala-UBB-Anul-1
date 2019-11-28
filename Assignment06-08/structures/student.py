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
