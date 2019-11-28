from collections import OrderedDict
from typing import Dict, List

from errors import DuplicateIdError, MissingIdError
from structures.discipline import Discipline


class DisciplineManager:

    def __init__(self):
        self.__disciplines: Dict[int, Discipline] = OrderedDict()

    def add_discipline(self, discipline: Discipline):
        """
        Adds a discipline, if id already exists throws a L{DuplicateIdError}
        @param discipline: The Discipline you want to add
        """
        if self.__disciplines.get(discipline.id) is not None:
            raise DuplicateIdError('Discipline Id already exists')
        self.__disciplines[discipline.id] = discipline

    def remove_discipline(self, discipline_id: int):
        """
        Removes a discipline, if id doesn't exist it throws a L{MissingIdError}
        @param discipline_id: The Discipline with the id you want to remove
        """
        if self.__disciplines.get(discipline_id) is None:
            raise MissingIdError('Discipline with given id does not exist')
        self.__disciplines.pop(discipline_id)

    def retrieve_discipline(self, discipline_id: int):
        """
        Retrieves a discipline, if id doesn't exist it throws a L{MissingIdError}
        @param discipline_id: The Discipline object with the id you want to retrieve
        @return: The Discipline Object
        """
        if self.__disciplines.get(discipline_id) is None:
            raise MissingIdError('Discipline with given id does not exist')
        return self.__disciplines[discipline_id]

    def discipline_id_exists(self, discipline_id):
        """
        Checks if the given discipline id already exists
        @param discipline_id: the id to check for
        @return: True or False
        """
        if self.__disciplines.get(discipline_id) is None:
            return False
        return True

    def search(self, term: str) -> List[Discipline]:
        """
        Search discipline with id or name that at least partially matches(case insensitive)
        @param term: the term to search for
        @return: All the Discipline objects that match
        """
        term = term.lower()
        results: List[Discipline] = []
        for discipline in self.__disciplines.values():
            if term in str(discipline.id) or term in discipline.name.lower():
                results.append(discipline)
        return results

    @property
    def last_discipline_id(self):
        """
        The Last Used discipline id
        @return: Just the id
        """
        if len(self.__disciplines.keys()) == 0:
            return 0
        return list(self.__disciplines.keys())[-1]

    @property
    def disciplines(self):
        return list(self.__disciplines.values())
