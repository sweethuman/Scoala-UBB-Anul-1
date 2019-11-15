class Student:
    def __init__(self, stid: int, name: str, group: int):
        self.__id = stid
        self.__name = name
        self.__group = group

    @property
    def id(self):
        return self.__id

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        self.__name = value

    @property
    def group(self):
        return self.__group

    @group.setter
    def group(self, value):
        self.__group = value

    def __eq__(self, other):
        return self.__id == other.__id

    def __str__(self):
        return 'Student Id:{} Name:{} Group:{}'.format(self.__id, self.__name, self.__group)
