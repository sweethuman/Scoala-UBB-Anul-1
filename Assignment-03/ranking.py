from enum import Enum, unique
from typing import List, Optional

from contestant import Contestant
import copy


@unique
class Problem(Enum):
    P1 = 'P1'
    P2 = 'P2'
    P3 = 'P3'


class Ranking:
    def __init__(self, preexisting_ranking: Optional[List[Contestant]] = None):
        if preexisting_ranking is None:
            preexisting_ranking = []
        self._contestants: List[Contestant] = preexisting_ranking

    @property
    def contestants(self) -> List[Contestant]:
        return self._contestants

    @property
    def ranking(self) -> List[Contestant]:
        return sorted(self._contestants, key=lambda item: item.average, reverse=True)

    def add_contestant(self, p1: int, p2: int, p3: int):
        """
        Adds a contestant to the current ranking
        @param p1: Score for Problem 1
        @param p2: Score for Problem 2
        @param p3: Score for Problem 3
        """
        self._contestants.append(Contestant(p1, p2, p3))

    def insert_contestant(self, p1: int, p2: int, p3: int, position: int):
        """
        Inserts a contestant at the specified position
        @param p1: Score for Problem 1
        @param p2: Score for Problem 2
        @param p3: Score for Problem 3
        @param position: Position in ranking where to insert the contestant
        """
        self._contestants.insert(position, Contestant(p1, p2, p3))

    def remove_contestant(self, position: int):
        """
        Removes a contestant a the specified position by setting all the problem's scores to 0
        @param position: Contestant at this position will be removed
        @return:
        """
        self._contestants[position].p1 = 0
        self._contestants[position].p2 = 0
        self._contestants[position].p3 = 0

    def remove_contestant_start_to_end(self, start_position: int, end_position: int):
        """
        Remove all contestants from start_position to end_position by setting all the problem's scores to 0
        @param start_position: The Position at which to start removing
        @param end_position: The Position at which to stop removing
        """
        for position in range(start_position, end_position):
            self._contestants[position].p1 = 0
            self._contestants[position].p2 = 0
            self._contestants[position].p3 = 0

    def remove_contestant_positions(self, positions: List[int]):
        """
        Remove all contestant that reside at the specified positions by setting all problem's score to 0
        @param positions: The positions at which the contestants are
        """
        for position in positions:
            self._contestants[position].p1 = 0
            self._contestants[position].p2 = 0
            self._contestants[position].p3 = 0

    def replace_problem_score(self, position: int, problem: Problem, score: int):
        """
        Replaces the score of a problem for a contestant on the specified position
        @param position: Position of the contestant
        @param problem: Problem to change score of
        @param score: New score to set
        """
        if problem.P1 == problem:
            self._contestants[position].p1 = score
        elif problem.P2 == problem:
            self._contestants[position].p2 = score
        elif problem.P3 == problem:
            self._contestants[position].p3 = score


class UndoableRanking(Ranking):
    """
    The same as C{Ranking} but this version keeps a history of all the modifications
    """

    def __init__(self, preexisting_ranking: Optional[List[Contestant]] = None):
        self._oldRanking: List[List[Contestant]] = []
        super().__init__(preexisting_ranking)

    def add_contestant(self, p1: int, p2: int, p3: int):
        self._oldRanking.append(copy.deepcopy(self._contestants))
        super().add_contestant(p1, p2, p3)

    def insert_contestant(self, p1: int, p2: int, p3: int, position: int):
        self._oldRanking.append(copy.deepcopy(self._contestants))
        super().insert_contestant(p1, p2, p3, position)

    def remove_contestant(self, position: int):
        self._oldRanking.append(copy.deepcopy(self._contestants))
        super().remove_contestant(position)

    def remove_contestant_start_to_end(self, start_position: int, end_position: int):
        self._oldRanking.append(copy.deepcopy(self._contestants))
        super().remove_contestant_start_to_end(start_position, end_position)

    def remove_contestant_positions(self, positions: List[int]):
        self._oldRanking.append(copy.deepcopy(self._contestants))
        super().remove_contestant_positions(positions)

    def replace_problem_score(self, position: int, problem: Problem, score: int):
        self._oldRanking.append(copy.deepcopy(self._contestants))
        super().replace_problem_score(position, problem, score)

    def undo(self):
        """
        Undoes the last operation which modified the ranking
        """
        if len(self._oldRanking) > 0:
            self._contestants = self._oldRanking[-1]
            self._oldRanking.pop()
            return True
        return False
