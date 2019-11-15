from services import Services
from student import Student


class UI:

    def __init__(self, services: Services):
        self.__services = services

    def read_student(self):
        """
        Reads from console a student and adds it
        """
        while True:
            read_id = input('Enter Student ID: ')
            try:
                read_id = int(read_id)
            except ValueError:
                print('Student ID not a number')
                continue
            if not self.__services.check_unique_id(read_id):
                print('Student ID already exists')
                continue
            read_name = input('Enter Student Name: ')
            read_group = input('Enter Student Group: ')
            try:
                read_group = int(read_group)
            except ValueError:
                print('Student Group not a number')
                continue
            self.__services.add_to_history()
            self.__services.add_student(Student(read_id, read_name, read_group))
            break

    def list_students(self):
        """
        Prints on the console a list of students
        """
        print('List of students:')
        for student in self.__services.students:
            print(student)

    def filter_students(self):
        """
        Read from console the Group and Removes the students from the Group
        """
        while True:
            read_group = input('Enter Student Group: ')
            try:
                read_group = int(read_group)
            except ValueError:
                print('Student Group not a number')
                continue
            self.__services.add_to_history()
            self.__services.filter_students_group(read_group)
            break

    def start_menu(self):
        while True:
            print('1. Add Student\n'
                  '2. List Students\n'
                  '3. Filter Students from Group\n'
                  '4. Undo\n'
                  '5. Exit\n')
            read_value = input('Enter Menu Option: ')
            print('')
            if read_value == '1':
                self.read_student()
            elif read_value == '2':
                self.list_students()
                print('')
            elif read_value == '3':
                self.filter_students()
            elif read_value == '4':
                try:
                    self.__services.undo()
                except IndexError:
                    print("Sorry. Can't undo anymore!")
                else:
                    print('Undone!')
            elif read_value == '5':
                break
            else:
                print("Wrong Option Please try again")
