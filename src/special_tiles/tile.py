from abc import ABC, abstractmethod
from enum import Enum, auto

class TileAction(Enum):
    GOTO = auto()
    GOTO_DELTA = auto()
    FREEZE = auto()

class Tile(ABC):
    def __init__(self, is_special=False):
        self.players = set()
        self.is_starting = False
        self.is_winning = False
        self.is_special = is_special

    def set_starting(self):
        assert self.is_special is False
        self.is_starting = True

    def set_winning(self):
        assert self.is_special is False
        self.is_winning = True

    def add_player(self, player):
        assert len(self.players) <= 1 or self.is_starting or self.is_winning, self
        self.players.add(player)

    def remove_player(self, player):
        self.players.discard(player)

    def action_message(self):
        ...

    def tile_action(self):
        ...
        
    


