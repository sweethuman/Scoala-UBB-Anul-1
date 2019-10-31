from cli.command import Command
from output.output_colors import OutputColors
from typing import List, Tuple, Dict, Union, TypedDict


class Error(Exception):
    pass


class TooManyCommandIdentifiers(Error):
    pass


class Engine:

    def __init__(self):
        self._commands: Dict[str, Command] = {}
        self._delimiter = '~$'
        self._active = False

    @property
    def delimiter(self) -> str:
        return self._delimiter

    @delimiter.setter
    def delimiter(self, delimiter: str):
        self._delimiter = delimiter

    def command(self, command: str, description: str) -> Command:
        """
        Initializes a command
        @param command: String Identifier for command
        @param description: The description of the command to be shown on the help menu
        @return: Created Command Object
        """
        if len(command.split(' ')) > 1:
            raise TooManyCommandIdentifiers('Command should only have one identifier. Additional words can be entered '
                                            'as keywords using variation.')
        created_command = Command(command)
        created_command.set_description(description)
        self._commands[command] = created_command
        if self._active:
            self.__generate_help()
        return created_command

    # should start the help generator for help command
    # show the delimiter and input and start processing the commands
    # after the input when command is entered we check for fitting command
    # parser should support double quotes to enter arguments and ignore them of any other functionality
    # number arguments should be converted automatically to numbers
    def show(self):
        """
        Starts the Input on the console and runs the engine and waits for commands
        """
        self._active = True
        self.__generate_help()
        while True:
            execute_command = input(self._delimiter + ' ')
            self.exec(execute_command)

    def exec(self, command_text: str):
        """
        Executes the given command with arguments
        @param command_text: Command String received in the same format as typed normally in the console
        @return: None
        """
        command_text, rest = (list(command_text.split(' ', 1)) + [''])[:2]
        if command_text in self._commands:
            command = self._commands[command_text]
            passed = False
            for arguments_variant in command.variations:
                if arguments_variant.match(rest):
                    arguments_variant.action(**arguments_variant.convert(rest))
                    passed = True
                    break
            if not passed:
                print(OutputColors.FAIL + "The arguments provided don't match the command" + OutputColors.ENDC)
        else:
            print(OutputColors.FAIL + 'Command not found!' + OutputColors.ENDC)

    def __generate_help(self):
        pass
