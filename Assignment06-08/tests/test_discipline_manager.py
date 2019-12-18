from unittest import TestCase

from managers import DisciplineManager
from repositories import Repository
from structures import Discipline


class TestDisciplineManager(TestCase):
    def test_add_discipline(self):
        discipline_manager = DisciplineManager(Repository(Discipline, int, lambda value: value.id))
        discipline = Discipline(1, "Matematica")
        discipline_manager.add_discipline(discipline)
        self.assertEqual([discipline], discipline_manager.disciplines)

    def test_remove_discipline(self):
        discipline_manager = DisciplineManager(Repository(Discipline, int, lambda value: value.id))
        discipline = Discipline(1, "Matematica")
        discipline2 = Discipline(2, "Fundmae")
        discipline3 = Discipline(3, "Matematica")
        discipline_manager.add_discipline(discipline)
        discipline_manager.add_discipline(discipline2)
        discipline_manager.add_discipline(discipline3)
        discipline_manager.remove_discipline(2)
        self.assertListEqual(
            sorted([discipline, discipline3], key=lambda value: value.id, reverse=True), discipline_manager.disciplines,
        )

    def test_retrieve_discipline(self):
        discipline_manager = DisciplineManager(Repository(Discipline, int, lambda value: value.id))
        discipline = Discipline(1, "Matematica")
        discipline2 = Discipline(2, "Fundmae")
        discipline3 = Discipline(3, "Matematica")
        discipline_manager.add_discipline(discipline)
        discipline_manager.add_discipline(discipline2)
        discipline_manager.add_discipline(discipline3)
        self.assertEqual(discipline2, discipline_manager.retrieve_discipline(2))

    def test_discipline_id_exists(self):
        discipline_manager = DisciplineManager(Repository(Discipline, int, lambda value: value.id))
        discipline = Discipline(1, "Matematica")
        discipline2 = Discipline(2, "Fundmae")
        discipline3 = Discipline(3, "Matematica")
        discipline_manager.add_discipline(discipline)
        discipline_manager.add_discipline(discipline2)
        discipline_manager.add_discipline(discipline3)
        self.assertEqual(True, discipline_manager.discipline_id_exists(2))
        self.assertEqual(False, discipline_manager.discipline_id_exists(4))

    def test_search(self):
        discipline_manager = DisciplineManager(Repository(Discipline, int, lambda value: value.id))
        discipline = Discipline(1, "Matematica")
        discipline2 = Discipline(2, "Fundmae")
        discipline3 = Discipline(3, "Logica")
        discipline_manager.add_discipline(discipline)
        discipline_manager.add_discipline(discipline2)
        discipline_manager.add_discipline(discipline3)
        self.assertEqual([discipline, discipline2], discipline_manager.search("ma"))

    def test_last_discipline_id(self):
        discipline_manager = DisciplineManager(Repository(Discipline, int, lambda value: value.id))
        discipline = Discipline(1, "Matematica")
        discipline2 = Discipline(2, "Fundmae")
        discipline3 = Discipline(3, "Logica")
        discipline_manager.add_discipline(discipline)
        discipline_manager.add_discipline(discipline2)
        discipline_manager.add_discipline(discipline3)
        self.assertEqual(3, discipline_manager.last_discipline_id)
