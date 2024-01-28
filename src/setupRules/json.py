import json
import os
import logging

from .base import FileReader
from ..enums import SpecialTile, DiceStrategy

logger = logging.getLogger('Main')


class JSONReader(FileReader):
    def __init__(self, file_name, *args, **kwargs):
        assert os.path.splitext(file_name)[1] == '.json', os.path.splitext(file_name)
        super().__init__(file_name)

    def consume(self):
        logger.debug("Attempting to read file")
        contents = json.load(open(self.file, 'r'))

        # setup board
        self.board_size = contents.get('board_size', 100)
        logger.debug('Set board size to %d', self.board_size)
        # Should be a dict of type which contains a list of positions
        # Needs a bunch of validations
        valid_tiles = set([i.value for i in SpecialTile])
        for special_tile, *info in contents['special_tiles']:
            assert special_tile in valid_tiles
            self.special_tiles.append((special_tile, info))
        logger.debug('Added %d special tiles', len(self.special_tiles))

        assert contents['dice_strategy'] in set([i.value for i in DiceStrategy])
        self.dice_strategy = contents['dice_strategy']
        logger.debug('Set dice strategy to %s', self.dice_strategy)
        self.dice = contents.get('dice', [6])
        logger.debug('%d dice found', len(self.dice))
        self.players_start = contents['players']
        logger.debug('%d players added...', len(self.players_start))


