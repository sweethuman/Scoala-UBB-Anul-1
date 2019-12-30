from console import fg, utils, fx

from enums import Chip, Direction
from game_data import GameData
from service import Service
import readchar


class UI:
    service: Service
    game_data: GameData
    horizontal_delimiter: str

    def __init__(self, service: Service, game_data: GameData):
        self.service = service
        self.game_data = game_data
        self.horizontal_delimiter = self.print_horizontal_delimiter()

    def print_board(self) -> str:
        buffer = []
        for i in range(self.game_data.height):
            buffer.append(self.horizontal_delimiter)
            buffer.append("\n")
            buffer.append("|")
            for j in range(self.game_data.width):
                buffer.append(self.print_chip(self.game_data.board[i][j]))
                buffer.append("|")
            buffer.append("\n")
        return "".join(buffer)

    def print_selector(self) -> str:
        buffer = []
        for i in range(self.game_data.width):
            if self.game_data.current_selected_column == i:
                buffer.append(" ")
                buffer.append(self.print_chip(self.game_data.currentPlayer))
                buffer.append(" ")
            else:
                buffer.append("    ")
        return "".join(buffer)

    def print_chip(self, chip: Chip) -> str:
        if chip == Chip.EMPTY:
            return "   "
        elif chip == Chip.RED:
            return fg.red + " ■ " + fg.default
        elif chip == Chip.YELLOW:
            return fg.yellow + " ■ " + fg.default

    def print_horizontal_delimiter(self) -> str:
        return "".join([fx.bold + "----" + fx.default for i in range(self.game_data.width)])

    def execute(self):
        while 1:
            buffer = [self.print_selector(), "\n", self.print_board()]
            show = "".join(buffer)
            utils.clear_screen(1)
            print(show)
            if self.game_data.ended:
                break
            while 1:
                key = readchar.readkey()
                if key == readchar.key.RIGHT:
                    self.service.move_selector(Direction.RIGHT)
                    break
                elif key == readchar.key.LEFT:
                    self.service.move_selector(Direction.LEFT)
                    break
                elif key == readchar.key.SPACE:
                    self.service.use_turn()
                    break
        print("\n\n\n")
        if self.game_data.winner == Chip.RED:
            print(fg.red + "PLAYER 1 HAS WON" + fg.default)
        elif self.game_data.winner == Chip.YELLOW:
            print(fg.yellow + "PLAYER 2 HAS WON" + fg.default)
