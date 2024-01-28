import json
import os

from .base import FileReader
from ..enums import SpecialTile, DiceStrategy


class JSONReader(FileReader):
    def __init__(self, file_name, *args, **kwargs):
        assert os.path.splitext(file_name)[1] == '.json'
        super(JSONReader).__init__(*args, **kwargs)

    def consume(self):
        contents = json.load(open(self.file, 'r'))
        # setup board
        self.board_size = contents.get('board_size', 100)
        # Should be a dict of type which contains a list of positions
        # Needs a bunch of validations
        valid_tiles = set([i.value for i in SpecialTile])
        for special_tile, *info in contents['special_tiles']:
            assert special_tile in valid_tiles
            self.special_tiles.append((special_tile, info))

        assert contents['dice_strategy'] in set([i.value for i in DiceStrategy])
        self.dice_strategy = contents['dice_strategy']
        self.dice = contents.get('dice', [6])
        self.players_start = contents['players']


