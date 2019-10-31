from unittest import TestCase
from cli import Command


class TestCommand(TestCase):
    def test_command(self):
        command = Command('list')
        self.assertEqual(command.command, 'list', 'Command identifier should be "list"')

    def test_description(self):
        command = Command('command')
        self.assertEqual(command.description, '', 'Default description should be empty')

    def test_variations(self):
        command = Command('command')
        self.assertEqual(command.variations, [], 'Default variations should be an empty list')

    def test_set_description(self):
        command = Command('command')
        command.set_description('This is new description')
        self.assertEqual(command.description, 'This is new description', 'The description should be the new description')

    def test_variation(self):
        self.fail()
