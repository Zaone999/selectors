import unittest
from src.gameBoard import GameBoard

class TestGameBoard(unittest.TestCase):
    def setUp(self):
        self.board = GameBoard()
        self.board.fill()

    def test_propagate_in_bounds(self):
        self.board.propagate(5, 5)
        self.assertTrue(self.board._board[5][5].is_open)
    
    def test_propagate_out_of_bounds(self):
        self.board.propagate(-1, -1)
        self.assertFalse(self.board._board[0][0].is_open)

    def test_propagate_bomb(self):
        self.board._board[5][5].is_bomb = True
        self.board.propagate(5, 5)
        self.assertTrue(self.board._bomb_found)

    def test_propagate_value(self):
        self.board._board[5][5].value = 0
        self.board.propagate(5, 5)
        for i in range(-1, 2):
            for j in range(-1, 2):
                self.assertTrue(self.board._board[5 + j][5 + i].is_open)