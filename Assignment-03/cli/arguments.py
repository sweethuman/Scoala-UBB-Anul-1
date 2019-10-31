from typing import Callable, List, TypedDict, Dict
from enum import Enum, unique
import re


class Error(Exception):
    pass


class ArgumentFormatError(Error):
    pass


@unique
class ArgumentMode(Enum):
    REQUIRED = 1
    OPTIONAL = 2
    KEYWORD = 3


class Argument(TypedDict):
    mode: ArgumentMode
    name: str
    regex: str


class Arguments:
    def __init__(self, action: Callable):
        self._arguments: List[Argument] = []
        self._action = action

    def match(self, string: str):
        """
        Matches the given string to the argument format it loaded before
        @param string: String to match
        @return: True if it matches, False if it not
        """
        strings = string.split()
        if len(self._arguments) == len(strings):
            for i in range(0, len(self._arguments)):
                if re.fullmatch(self._arguments[i]['regex'], strings[i]) is None:
                    return False
            return True
        return False

    def convert(self, string: str):
        """
        Converts the given string to a dictionary, where the key is the argument name and the value is the value from
        the given string
        @param string: The String to convert
        @return: The converted Dictionary
        """
        strings = string.split()
        params: Dict[str, str] = {}
        for i in range(0, len(self._arguments)):
            if self._arguments[i]['mode'] is not ArgumentMode.KEYWORD:
                params[self._arguments[i]['name']] = strings[i]
        return params

    @property
    def arguments(self) -> List[Argument]:
        return self._arguments

    @property
    def action(self) -> Callable:
        return self._action

    # <required:type> [optional:type] keyword; type = letters, int or (food|water|expenses) etc.
    # this function has to validate the arguments string otherwise throw an error
    # and then prepare for the tuple the arguments part already parsed
    # argument: {"mode": 'required|optional|keyword', "regex": '...', "name": 'name'}
    def load_arguments(self, arguments_text: str):
        """
        Loads the specified arguments into the class

        Argument Format:
            - B{<argument_name:type>} - a required argument, 'argument_name' is the argument name

            The available types are:
                - B{int} - accepts only numbers
                - B{letters} - accepts only letter
                - B{(option1|option2|option3)} - can have as many options as you want, separated by a '|', accepts only
                defined options
            - B{keyword} - a keyword, is used for input validation

        @param arguments_text: String to specify arguments in special format
        """
        arguments = arguments_text.split()
        for argument in arguments:
            if re.fullmatch(r'^<(([0-9]|[A-z])+_)*([0-9]|[A-z])+(:(int|letters|(\(((\w+|<|>|=)\|)+(\w+|<|>|=)\))))?>$',
                            argument):
                declaration = argument.strip('>').strip('<').split(':')
                name = declaration[0]
                if len(declaration) == 1:
                    regex = r'\w+'
                elif declaration[1] == 'int':
                    regex = r'[0-9]+'
                elif declaration[1] == 'letters':
                    regex = r'[A-z]+'
                elif re.fullmatch(r'^\(((\w+|<|>|=)\|)+(\w+|<|>|=)\)$', declaration[1]):
                    regex = declaration[1]
                else:
                    raise ArgumentFormatError('{} is in the wrong format!'.format(argument))
                argument_obj: Argument = {"mode": ArgumentMode.REQUIRED, "name": name, "regex": regex}
                self._arguments.append(argument_obj)
            elif re.fullmatch(r'^([0-9]|[A-z])+$', argument):
                argument_obj = {"mode": ArgumentMode.KEYWORD, "name": argument, "regex": argument}
                self._arguments.append(argument_obj)
            else:
                raise ArgumentFormatError('{} is in the wrong format!'.format(argument))
