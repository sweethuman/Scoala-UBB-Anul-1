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
        """
        Places a chip in the selected column and after the turn checks if after the move there is a winner
        """
        hit_break = False
        # Checks from bottom up the first empty spot and places a chip on the board
        for i in range(self.game_data.height - 1, 0 - 1, -1):
            if self.game_data.board[i][self.game_data.current_selected_column] == Chip.EMPTY:
                self.game_data.board[i][self.game_data.current_selected_column] = self.game_data.currentPlayer
                hit_break = True
                break
        # If a valid move has been made change the player and check for a winner
        if hit_break:
            self._check_winner()
            self.game_data.currentPlayer = Chip.RED if self.game_data.currentPlayer == Chip.YELLOW else Chip.YELLOW

    def ai_turn(self):
        """
        Simulates an AI Move by selecting a random column and then doing a turn
        @return: The Random Column
        """
        column = random.randrange(0, self.game_data.width)
        self.game_data.current_selected_column = column
        self.use_turn()
        self.game_data.current_selected_column = 0
        return column

    def move_selector(self, direction: Direction):
        """
        Moves the Column Selector
        @param direction: The Direction in Which to move the selector
        """
        if direction == Direction.RIGHT:
            if self.game_data.current_selected_column + 1 < self.game_data.width:
                self.game_data.current_selected_column += 1
        elif direction == Direction.LEFT:
            if self.game_data.current_selected_column - 1 >= 0:
                self.game_data.current_selected_column -= 1

    def _check_winner(self):
        """
        Checks for a winner by checking every position and seeing
        if on any direction are at least 3 pieces of same colour placed
        """
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
