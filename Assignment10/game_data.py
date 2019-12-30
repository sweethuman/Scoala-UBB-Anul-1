from enums import Chip
from typing import List


class GameData:
    height: int
    width: int
    currentPlayer: Chip
    board: List[List[Chip]]
    current_selected_column: int
    ended: bool
    winner: Chip

    def __init__(self):
        self.height = 6
        self.width = 7
        self.currentPlayer = Chip.RED
        self._populate_board()
        self.current_selected_column = 0
        self.ended = False

    def _populate_board(self):
        self.board = []
        for i in range(6):
            new_row: List[Chip] = []
            for j in range(7):
                new_row.append(Chip.EMPTY)
            self.board.append(new_row)
