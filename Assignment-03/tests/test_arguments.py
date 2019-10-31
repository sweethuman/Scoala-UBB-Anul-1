from unittest import TestCase
from cli import Arguments
from cli.arguments import ArgumentMode, ArgumentFormatError


class TestArguments(TestCase):
    def test_match(self):
        def test_simple_action():
            pass

        arguments = Arguments(test_simple_action)
        arguments.load_arguments('<frame> <fire:int> <flank:letters> kappa')
        self.assertTrue(arguments.match('blep 55 bleeeep kappa'))
        self.assertFalse(arguments.match('blep 5a5 bleeeep kappa'))
        self.assertFalse(arguments.match('blep 55 bl5eeep kappa'))
        self.assertFalse(arguments.match('blep 55 bleeep ka8ppa'))
        self.assertFalse(arguments.match('blep 55 ka8ppa'))

    def test_convert(self):
        def test_simple_action(frame, fire, flank):
            pass

        arguments = Arguments(test_simple_action)
        arguments.load_arguments('<frame> <fire:int> <flank:letters> kappa')
        self.assertEqual(arguments.convert('blep 55 bleeeep kappa'),
                         {'frame': 'blep', 'fire': '55', 'flank': 'bleeeep'})

    def test_arguments(self):
        arguments = Arguments(lambda x: x)
        self.assertEqual(arguments.arguments, [], 'Default arguments should be an empty list')

    def test_action(self):
        def test_simple_action():
            pass

        arguments = Arguments(test_simple_action)
        self.assertEqual(arguments.action, test_simple_action, 'Action should return the action specified in the '
                                                               'constructor')

    def test_load_arguments(self):
        def test_simple_action():
            pass

        arguments = Arguments(test_simple_action)
        arguments.load_arguments('<frame>')
        self.assertEqual(arguments.arguments, [{"mode": ArgumentMode.REQUIRED, "name": 'frame', "regex": r'\w+'}])

        arguments = Arguments(test_simple_action)
        arguments.load_arguments('<frame:int>')
        self.assertEqual(arguments.arguments, [{"mode": ArgumentMode.REQUIRED, "name": 'frame', "regex": r'[0-9]+'}])

        arguments = Arguments(test_simple_action)
        arguments.load_arguments('<frame:letters>')
        self.assertEqual(arguments.arguments, [{"mode": ArgumentMode.REQUIRED, "name": 'frame', "regex": r'[A-z]+'}])

        arguments = Arguments(test_simple_action)
        arguments.load_arguments('<frame:(option1|option2|option3)>')
        self.assertEqual(arguments.arguments,
                         [{"mode": ArgumentMode.REQUIRED, "name": 'frame', "regex": r'(option1|option2|option3)'}])

        arguments = Arguments(test_simple_action)
        arguments.load_arguments('frame')
        self.assertEqual(arguments.arguments, [{"mode": ArgumentMode.KEYWORD, "name": 'frame', "regex": 'frame'}])

        with self.assertRaises(ArgumentFormatError):
            arguments = Arguments(test_simple_action)
            arguments.load_arguments('<frame')

        with self.assertRaises(ArgumentFormatError):
            arguments = Arguments(test_simple_action)
            arguments.load_arguments('<frame:water>')

        with self.assertRaises(ArgumentFormatError):
            arguments = Arguments(test_simple_action)
            arguments.load_arguments('<frame:()>')
