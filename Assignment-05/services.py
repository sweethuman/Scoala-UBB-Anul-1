import copy


class Services:
    def __init__(self, students: list, history: list):
        self.__students = students
        self.__history = history

    @property
    def students(self):
        return self.__students

    @property
    def history(self):
        return self.__history

    def add_to_history(self):
        """
        Saves inside history the current state
        """
        self.__history.append(copy.deepcopy(self.__students))

    def add_student(self, student):
        """
        Adds a Student to the list
        @param student: Student to add
        @return:
        """
        self.__students.append(student)

    def undo(self):
        """
        Undoes the last operation by restoring the saved state in history
        """
        self.__students[:] = self.__history.pop()

    def check_unique_id(self, stid):
        """
        Checks if a gived Id is unique between the students
        @param stid: Id to Check
        """
        for student in self.__students:
            if student.id == stid:
                return False
        return True

    def delete_student_by_index(self, index):
        self.__students.pop(index)

    def filter_students_group(self, group: int):
        """
        Removes the Students in the Specified Group
        @param group: Group of Students to Remove from the List
        """
        length = len(self.__students)
        index = 0
        while index < length:
            if self.__students[index].group == group:
                self.delete_student_by_index(index)
                index -= 1
                length -= 1
            index += 1
