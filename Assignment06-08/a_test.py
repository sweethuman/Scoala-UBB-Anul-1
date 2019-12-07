from repositories.repository import Repository
from structures import Student, Discipline

student_repo: Repository[Student, int] = Repository(Student, int, lambda student: student.id)
discipline_repo: Repository[Discipline, int] = Repository(Discipline, int, lambda discipline: discipline.id)
