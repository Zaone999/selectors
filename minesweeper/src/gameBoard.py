from .cell import Cell
from .settings import Settings
from random import randint


class GameBoard:
    def __init__(self, settings) -> None:
        self.settings = Settings(settings)
        self._board = [[Cell() for _ in range(self.settings.width)] for _ in range(self.settings.height)]
        self._bomb_found = False
    def __str__(self) -> str:
        header = " ".join(chr(65 + i) for i in range(self.settings.width))
        rows = "\n".join(f"{i+1} {' '.join(map(str, row))}" for i, row in enumerate(self._board))
        return f"  {header}\n{rows}"

    def _increment_value(self, x, y):
        for i in range(-1, 2):
            for j in range(-1, 2):
                if 0 <= x + i < self.settings.width and 0 <= y + j < self.settings.height:
                    self._board[y + j][x + i].value += 1

    def fill(self):
        num_bombs = self.settings.num_bombs
        while num_bombs > 0:
            x = randint(0, self.settings.width - 1)
            y = randint(0, self.settings.height - 1)
            if not self._board[y][x].is_bomb:
                self._board[y][x].is_bomb = True
                self._increment_value(x, y)
                num_bombs -= 1

    def propagate(self, x, y):
        if 0 <= x < self.settings.width and 0 <= y < self.settings.height:
            if self._board[y][x].is_open:
                return
            self._board[y][x].is_open = True
            if self._board[y][x].is_bomb:
                self._bomb_found = True
                return
            if self._board[y][x].value == 0:
                for i in range(-1, 2):
                    for j in range(-1, 2):
                        self.propagate(x + i, y + j)

    @property
    def board(self):
        return self._board
    
    @property
    def bomb_found(self):
        return self._bomb_found