from unittest import TestCase
from game_data import GameData
from service import Service
from enums import Direction, Chip


class TestService(TestCase):
    def setUp(self) -> None:
        self.game_data = GameData()
        self.service = Service(self.game_data)

    def test_use_turn(self):
        self.service.use_turn()
        self.assertEqual(self.game_data.currentPlayer, Chip.YELLOW)
        self.assertEqual(self.game_data.board[self.game_data.height - 1][0], Chip.RED)
        self.service.use_turn()
        self.assertEqual(self.game_data.currentPlayer, Chip.RED)
        self.assertEqual(self.game_data.board[self.game_data.height - 2][0], Chip.YELLOW)
        self.game_data.current_selected_column = 1
        self.service.use_turn()
        self.assertEqual(self.game_data.currentPlayer, Chip.YELLOW)
        self.assertEqual(self.game_data.board[self.game_data.height - 1][1], Chip.RED)

    def test_ai_turn(self):
        selected_column = self.service.ai_turn()
        self.assertEqual(self.game_data.currentPlayer, Chip.YELLOW)
        self.assertEqual(self.game_data.current_selected_column, 0)
        self.assertEqual(self.game_data.board[self.game_data.height - 1][selected_column], Chip.RED)

    def test_move_selector(self):
        self.service.move_selector(Direction.RIGHT)
        self.assertEqual(self.game_data.current_selected_column, 1)
        self.assertEqual(self.game_data.currentPlayer, Chip.RED)
        for i in range(self.game_data.width + 3):
            self.service.move_selector(Direction.RIGHT)
        self.assertEqual(self.game_data.current_selected_column, self.game_data.width - 1)
        self.service.move_selector(Direction.LEFT)
        self.assertEqual(self.game_data.current_selected_column, self.game_data.width - 2)
        for i in range(self.game_data.width + 3):
            self.service.move_selector(Direction.LEFT)
        self.assertEqual(self.game_data.current_selected_column, 0)

    def test__check_winner(self):
        self.service._check_winner()
        self.assertEqual(self.game_data.ended, False)
        self.game_data.board[self.game_data.height - 2][0] = Chip.RED
        self.game_data.board[self.game_data.height - 2][1] = Chip.RED
        self.game_data.board[self.game_data.height - 2][2] = Chip.RED
        self.game_data.board[self.game_data.height - 2][3] = Chip.RED
        self.service._check_winner()
        self.assertEqual(self.game_data.ended, True)
        self.assertEqual(self.game_data.winner, Chip.RED)
