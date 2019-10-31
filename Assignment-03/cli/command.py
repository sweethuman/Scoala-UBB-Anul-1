from __future__ import annotations

from typing import List, TypedDict, Callable
from cli.arguments import Arguments
import re


# TODO https://github.com/dthree/vorpal/wiki/API-%7C-vorpal.command#multi-word-commands

class OptionArgument(TypedDict):
    name: str
    required: bool


class Command:
    def __init__(self, command: str):
        self._command = command
        self._description = ""
        self._argument_variations: List[Arguments] = []

    @property
    def command(self):
        return self._command

    @property
    def description(self):
        return self._description

    @property
    def variations(self) -> List[Arguments]:
        return self._argument_variations

    def set_description(self, description: str) -> Command:
        """
        Sets the description for the command
        @param description: The Description to set
        @return: The current Command Instance
        """
        self._description = description
        return self

    def variation(self, arguments: str, function: Callable) -> Command:
        """
        Adds multiple variations to the Command. In case the command accepts more types of arguments for
        different operations

        Argument Format:
            - B{<argument_name:type>} - a required argument, 'argument_name' is the argument name that will be sent to the
            function containing the inputted value

            The available types are:
                - B{int} - accepts only numbers
                - B{letters} - accepts only letter
                - B{(option1|option2|option3)} - can have as many options as you want, separated by a '|', accepts only
                defined options
            - B{keyword} - a keyword, is required to be entered in the command and used in validation, but it does not appear
            as an argument for the function

        Example: '<pos:int> for <choice:(option1|option2)>' has a valid input as '5 to option1'

        B{THE ORDER MATTERS}
        @param arguments: Arguments entered as a string in a special format
        @param function: The function to be called when a valid argument format has been entered
        @return: The current Command Instance
        """
        initiated_arguments = Arguments(function)
        initiated_arguments.load_arguments(arguments)
        self._argument_variations.append(initiated_arguments)
        return self
