from enum import Enum, auto

class MovementStatus(Enum):
    FREE = auto()
    RESTRICTED = auto()

class Player:
    def __init__(self, name):
        self.name = name
        # self._status = MovementStatus.FREE

    def __str__(self):
        return self.name
