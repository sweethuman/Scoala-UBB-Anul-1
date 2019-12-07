from collections import OrderedDict
from typing import Dict, List

from errors import DuplicateIdError, MissingIdError
from structures.discipline import Discipline
from structures import Operation, FunctionCall
from repositories import Repository


class DisciplineManager:
    def __init__(self, repository: Repository[Discipline, int]):
        self.__repository = repository

    def add_discipline(self, discipline: Discipline) -> Operation:
        """
        Adds a discipline, if id already exists throws a L{DuplicateIdError}
        @param discipline: The Discipline you want to add
        """
        if self.__repository.exists_element(discipline.id) is True:
            raise DuplicateIdError("Discipline Id already exists")
        self.__repository.add_element(discipline)
        undo = FunctionCall(self.remove_discipline, discipline.id)
        redo = FunctionCall(self.add_discipline, discipline)
        return Operation(undo, redo)

    def remove_discipline(self, discipline_id: int) -> Operation:
        """
        Removes a discipline, if id doesn't exist it throws a L{MissingIdError}
        @param discipline_id: The Discipline with the id you want to remove
        """
        if self.__repository.exists_element(discipline_id) is False:
            raise MissingIdError("Discipline with given id does not exist")
        discipline = self.__repository.remove_element(discipline_id)
        undo = FunctionCall(self.add_discipline, discipline)
        redo = FunctionCall(self.remove_discipline, discipline_id)
        return Operation(undo, redo)

    def retrieve_discipline(self, discipline_id: int) -> Discipline:
        """
        Retrieves a discipline, if id doesn't exist it throws a L{MissingIdError}
        @param discipline_id: The Discipline object with the id you want to retrieve
        @return: The Discipline Object
        """
        if self.__repository.exists_element(discipline_id) is False:
            raise MissingIdError("Discipline with given id does not exist")
        return self.__repository.get_element(discipline_id)

    def discipline_id_exists(self, discipline_id) -> bool:
        """
        Checks if the given discipline id already exists
        @param discipline_id: the id to check for
        @return: True or False
        """
        return self.__repository.exists_element(discipline_id)

    def search(self, term: str) -> List[Discipline]:
        """
        Search discipline with id or name that at least partially matches(case insensitive)
        @param term: the term to search for
        @return: All the Discipline objects that match
        """
        term = term.lower()
        results: List[Discipline] = []
        for discipline in self.__repository.get_all:
            if term in str(discipline.id) or term in discipline.name.lower():
                results.append(discipline)
        return results

    @property
    def last_discipline_id(self):
        """
        The Last Used discipline id
        @return: Just the id
        """
        if len(self.__repository.get_all) == 0:
            return 0
        return sorted(self.__repository.get_all, key=lambda discipline: discipline.id)[-1].id

    @property
    def disciplines(self):
        return sorted(self.__repository.get_all, key=lambda discipline: discipline.id, reverse=True)
