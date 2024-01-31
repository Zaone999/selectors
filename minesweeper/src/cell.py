class Cell:
    def __init__(self) -> None:
        self._is_bomb = False
        self._is_open = False
        self._is_flag = False
        self._value = 0

    def __str__(self) -> str:
        if self.is_open:
            if self.is_bomb:
                return "B"
            elif self.is_flag:
                return "F"
            else:
                return str(self.value)
        else:
            return "X"
    @property
    def is_bomb(self):
        return self._is_bomb
    
    @is_bomb.setter
    def is_bomb(self, bool: bool):
        self._is_bomb = bool

    @property
    def is_open(self):
        return self._is_open
    
    @is_open.setter
    def is_open(self, bool: bool):
        self._is_open = bool

    @property
    def is_flag(self):
        return self._is_flag
    
    @is_flag.setter
    def is_flag(self, bool: bool):
        self._is_flag = bool

    @property
    def value(self):
        return self._value
    
    @value.setter
    def value(self, value: int):
        self._value = value