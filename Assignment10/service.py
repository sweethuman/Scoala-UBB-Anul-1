from enums import Chip, Direction
from typing import List
from game_data import GameData
import random


class Service:
    game_data: GameData
    directions = [(0, 1), (1, 0), (1, 1), (1, -1)]

    def __init__(self, game_data: GameData):
        self.game_data = game_data

    def use_turn(self):
        hit_break = False
        for i in range(self.game_data.height - 1, 0 - 1, -1):
            if self.game_data.board[i][self.game_data.current_selected_column] == Chip.EMPTY:
                self.game_data.board[i][self.game_data.current_selected_column] = self.game_data.currentPlayer
                hit_break = True
                break
        if hit_break:
            self._check_winner()
            self.game_data.currentPlayer = Chip.RED if self.game_data.currentPlayer == Chip.YELLOW else Chip.YELLOW

    def ai_turn(self):
        self.game_data.current_selected_column = random.randrange(0, self.game_data.width)
        self.use_turn()
        self.game_data.current_selected_column = 0

    def move_selector(self, direction: Direction):
        if direction == Direction.RIGHT:
            if self.game_data.current_selected_column + 1 < self.game_data.width:
                self.game_data.current_selected_column += 1
        elif direction == Direction.LEFT:
            if self.game_data.current_selected_column - 1 >= 0:
                self.game_data.current_selected_column -= 1

    def _check_winner(self):
        for i in range(self.game_data.height):
            for j in range(self.game_data.width):
                if self.game_data.board[i][j] != Chip.EMPTY:
                    current_chip = self.game_data.board[i][j]
                    for direction in self.directions:
                        count = 1
                        current_row = i
                        current_column = j
                        for pos in range(3):
                            current_row += direction[0]
                            current_column += direction[1]
                            if self.game_data.height > current_row >= 0 and self.game_data.width > current_column >= 0:
                                if self.game_data.board[current_row][current_column] == current_chip:
                                    count += 1
                                else:
                                    break
                        if count == 4:
                            self.game_data.ended = True
                            self.game_data.winner = current_chip
                            return
