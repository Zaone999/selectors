class Settings:
    def __init__(self, difficulity):
        if difficulity == "easy":
            self._width = 9
            self._height = 9
            self._num_bombs = 10
        elif difficulity == "medium":
            self._width = 16
            self._height = 16
            self._num_bombs = 40
        elif difficulity == "hard":
            self._width = 30
            self._height = 16
            self._num_bombs = 99
        else:
            raise ValueError("Invalid difficulity level")
        
    @property
    def width(self):
        return self._width
    
    @property
    def height(self):
        return self._height
    
    @property
    def num_bombs(self):
        return self._num_bombs