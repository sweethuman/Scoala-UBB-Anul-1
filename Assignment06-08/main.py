from controllers import UndoController
from managers import StudentManager, DisciplineManager, GradeManager, FileGradeManager, PickleGradeManager
from structures import Student, Discipline, Grade
from ui import UI
from repositories import Repository, FileRepository, PickleRepository


def add_student_test_data(student_manager: StudentManager):
    student_manager.add_student(Student(1, "Andrei"))
    student_manager.add_student(Student(2, "Alex"))
    student_manager.add_student(Student(3, "Andreea"))
    student_manager.add_student(Student(4, "Vasile"))
    student_manager.add_student(Student(5, "Ion"))
    student_manager.add_student(Student(6, "Matei"))
    student_manager.add_student(Student(7, "Paul"))
    student_manager.add_student(Student(8, "Gabriela"))
    student_manager.add_student(Student(9, "Ioana"))
    student_manager.add_student(Student(10, "Laura"))
    student_manager.add_student(Student(11, "Alexandra"))


def add_discipline_test_data(discipline_manager: DisciplineManager):
    discipline_manager.add_discipline(Discipline(1, "Analiza Matematica"))
    discipline_manager.add_discipline(Discipline(2, "Fizica Avansata"))
    discipline_manager.add_discipline(Discipline(3, "Teoria Muzicii"))
    discipline_manager.add_discipline(Discipline(4, "Fundamentele Programarii"))
    discipline_manager.add_discipline(Discipline(5, "Logica Ilogica"))
    discipline_manager.add_discipline(Discipline(6, "Filozofie"))
    discipline_manager.add_discipline(Discipline(7, "Fundamentele Psihologiei"))
    discipline_manager.add_discipline(Discipline(8, "Analiza Astrelor"))
    discipline_manager.add_discipline(Discipline(9, "Prezicerea Viitorului"))
    discipline_manager.add_discipline(Discipline(10, "Dezvoltarea tehnicilor de cunoastere persoanala"))


def add_grade_test_data(grade_manager: GradeManager):
    grade_manager.add_grade(Grade(2, 2, 2))
    grade_manager.add_grade(Grade(1, 2, 9))
    grade_manager.add_grade(Grade(2, 1, 7))
    grade_manager.add_grade(Grade(6, 4, 8))
    grade_manager.add_grade(Grade(4, 2, 4))
    grade_manager.add_grade(Grade(1, 3, 3))
    grade_manager.add_grade(Grade(2, 2, 4))
    grade_manager.add_grade(Grade(3, 1, 5))
    grade_manager.add_grade(Grade(3, 2, 1))
    grade_manager.add_grade(Grade(2, 1, 2))


def read_config():
    config = {}
    with open("settings.properties") as file:
        for line in file:
            line = line.strip()
            options = line.split("=")
            options[0] = options[0].strip()
            options[1] = options[1].strip()
            options[1] = options[1].strip('"')
            config[options[0]] = options[1]
    return config


def process_config(config: dict):
    if config["repository"] == "inmemory":
        student_repo: Repository[Student, int] = Repository(Student, int, lambda student: student.id)
        student_manager = StudentManager(student_repo)
        discipline_repo: Repository[Discipline, int] = Repository(Discipline, int, lambda discipline: discipline.id)
        discipline_manager = DisciplineManager(discipline_repo)
        grade_manager = GradeManager(student_manager, discipline_manager)
        add_student_test_data(student_manager)
        add_discipline_test_data(discipline_manager)
        add_grade_test_data(grade_manager)
    elif config["repository"] == "textfile":
        student_repo: Repository[Student, int] = FileRepository(
            Student, int, lambda student: student.id, config["students"]
        )
        student_manager = StudentManager(student_repo)
        discipline_repo: Repository[Discipline, int] = FileRepository(
            Discipline, int, lambda discipline: discipline.id, config["disciplines"]
        )
        discipline_manager = DisciplineManager(discipline_repo)
        grade_manager = FileGradeManager(student_manager, discipline_manager, config["grades"])
    elif config["repository"] == "binaryfiles":
        student_repo: Repository[Student, int] = PickleRepository(
            Student, int, lambda student: student.id, config["students"]
        )
        student_manager = StudentManager(student_repo)
        discipline_repo: Repository[Discipline, int] = PickleRepository(
            Discipline, int, lambda discipline: discipline.id, config["disciplines"]
        )
        discipline_manager = DisciplineManager(discipline_repo)
        grade_manager = PickleGradeManager(student_manager, discipline_manager, config["grades"])
    else:
        raise AttributeError("Invalid Config File!")

    return student_manager, discipline_manager, grade_manager


def main():
    config = read_config()
    student_manager, discipline_manager, grade_manager = process_config(config)
    undo_controller = UndoController()
    ui = UI(student_manager, discipline_manager, grade_manager, undo_controller)
    ui.executioner()


main()
