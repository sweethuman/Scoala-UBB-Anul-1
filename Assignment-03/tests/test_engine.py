from unittest import TestCase
from cli import Engine


class TestEngine(TestCase):
    def test_delimiter(self):
        engine = Engine()
        self.assertEqual(engine.delimiter, '~$', 'Should be \'~$\'')

    def test_set_delimiter(self):
        engine = Engine()
        engine.delimiter = 'test$'
        self.assertEqual(engine.delimiter, 'test$', 'Should be \'test$\'')

    def test_command(self):
        self.fail()

    def test_show(self):
        self.fail()

    def test_exec(self):
        self.fail()
