from typing import List, Dict, Tuple

from errors import MissingIdError
from managers.discipline_manager import DisciplineManager
from managers.student_manager import StudentManager
from structures.grade import Grade


class GradeManager:

    def __init__(self, student_manager: StudentManager, discipline_manager: DisciplineManager):
        self.student_manager = student_manager
        self.discipline_manager = discipline_manager
        self.__disciplines: Dict[int, List[Grade]] = {}
        self.__students: Dict[int, List[Grade]] = {}

    @property
    def grades(self):
        return [item for sublist in self.__disciplines.values() for item in sublist]

    # Raises KeyError if key doesn't exist
    def get_discipline_grades(self, discipline_id):
        """
        All the grades of a discipline
        @param discipline_id: The Id of the discipline
        @return: A List of Grades
        """
        return self.__disciplines[discipline_id]

    # Raises KeyError if key doesn't exist
    def get_student_grades(self, student_id):
        """
        All the grades of a student
        @param student_id: The Id of the student
        @return: A List of Grades
        """
        return self.__students[student_id]

    def add_grade(self, grade: Grade):
        """
        Adds a grade, if the Student Id or Discipline Id does not exist it throws a L{MissingIdError}
        @param grade: The Grade object you want to add
        """
        if not self.student_manager.student_id_exists(grade.student_id):
            raise MissingIdError('Student with given id does not exist!')
        if not self.discipline_manager.discipline_id_exists(grade.discipline_id):
            raise MissingIdError('Discipline with given id does not exist!')
        if self.__disciplines.get(grade.discipline_id) is None:
            self.__disciplines[grade.discipline_id] = []
        if self.__students.get(grade.student_id) is None:
            self.__students[grade.student_id] = []
        self.__disciplines[grade.discipline_id].append(grade)
        self.__students[grade.student_id].append(grade)

    def remove_all_discipline_grades(self, discipline_id):
        """
        Remove all the grades of a discipline
        @param discipline_id: The Discipline Id
        """
        grades = self.__disciplines.pop(discipline_id)
        for x in grades:
            self.__students[x.student_id].remove(x)

    def remove_all_student_grades(self, student_id):
        """
        Remove all the grades of a student
        @param student_id: The Student Id
        """
        grades = self.__students.pop(student_id)
        for x in grades:
            self.__disciplines[x.discipline_id].remove(x)

    def failing_students_ids(self):
        """
        Return the student ids of the students with an average of < 5 at at least one discipline
        @return: A List of Ids
        """
        failing_student_ids: List[int] = []
        for student_id in self.__students:
            discipline_values: Dict[int, List[int]] = {}
            for grade in self.__students[student_id]:
                stored_grades = discipline_values.get(grade.discipline_id)
                if stored_grades is None:
                    discipline_values[grade.discipline_id] = []
                    stored_grades = discipline_values.get(grade.discipline_id)
                stored_grades.append(grade.grade_value)
            for discipline_id in discipline_values:
                sumx = 0
                nr_of_grades = len(discipline_values[discipline_id])
                for grade_value in discipline_values[discipline_id]:
                    sumx += grade_value
                sumx = sumx / nr_of_grades
                if sumx < 5:
                    failing_student_ids.append(student_id)
                    break
        return failing_student_ids

    def best_students_ids(self):
        """
        The best students arranged in descending order
        @return: A List of Tuples with the student id and their average grade
        """
        best_students_ids: List[Tuple[int, float]] = []
        for student_id in self.__students:
            discipline_values: Dict[int, List[int]] = {}
            for grade in self.__students[student_id]:
                stored_grades = discipline_values.get(grade.discipline_id)
                if stored_grades is None:
                    discipline_values[grade.discipline_id] = []
                    stored_grades = discipline_values.get(grade.discipline_id)
                stored_grades.append(grade.grade_value)
            average_grades: List[float] = []
            for discipline_id in discipline_values:
                sumx = 0
                nr_of_grades = len(discipline_values[discipline_id])
                for grade_value in discipline_values[discipline_id]:
                    sumx += grade_value
                sumx = sumx / nr_of_grades
                average_grades.append(sumx)
            sumx = 0
            for average in average_grades:
                sumx += average
            sumx = sumx / len(average_grades)
            best_students_ids.append((student_id, sumx))
        best_students_ids.sort(key=lambda value: value[1], reverse=True)
        return best_students_ids

    def best_disciplines_ids(self):
        """
        The Best Disciplines ordered in descending order
        @return: A List of Tuples with the discipline id and it's average grade
        """
        best_discipline_ids: List[Tuple[int, float]] = []
        for discipline_id in self.__disciplines:
            discipline_values: List[float] = [grade.grade_value for grade in self.__disciplines[discipline_id]]
            sumx = 0
            for grade_value in discipline_values:
                sumx += grade_value
            sumx = sumx / len(discipline_values)
            best_discipline_ids.append((discipline_id, sumx))
        best_discipline_ids.sort(key=lambda value: value[1], reverse=True)
        return best_discipline_ids
