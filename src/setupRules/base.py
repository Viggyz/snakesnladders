from abc import ABC, abstractmethod


class FileReader(ABC):
    def __init__(self, file_name):
        self.file = file_name
        self.board_size = 100
        self.special_tiles = {}
        self.tile_types = None
        self.dice_strategy = None
        self.dice = None
        self.players_start = []

    @abstractmethod
    def consume(self):
        ...
