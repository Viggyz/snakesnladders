from .board import Board
from .dice import Dice
from .dice_strategy import MaxStrategy, MinStrategy, SumStrategy
from .enums import SpecialTile, DiceStrategy
from .game import Game
from .player import Player
from .setupRules.base import FileReader
from .special_tiles import Snake, Ladder


class GameBuilder:
    def __init__(self, setup_reader: FileReader):
        self.reader = setup_reader

    def setup(self):
        # Read from file and setup values
        self.reader.consume()

        # Setup base board
        board = Board(self.reader.board_size)

        # Tile setup
        special_tiles = []
        for tile_type, info in self.reader.special_tiles:
            if tile_type == SpecialTile.SNAKE:
                pos, drop_pos = info
                special_tiles.append((Snake(drop_pos), pos))
            elif tile_type == SpecialTile.LADDER:
                pos, lift_pos = info
                special_tiles.append((Ladder(lift_pos), pos))
        board.add_special_tiles(special_tiles)

        players = []
        # Player setup
        for name, pos in self.reader.players_start:
            # Potentiall check if same name is used twice
            player = Player(name)
            players.append(player)
            board.set_player_location(player, pos)

        #  Dice setup
        dices = [Dice(sides=sides) for sides in self.reader.dice]
        dice_strat = SumStrategy(dices)
        if self.reader.dice_strategy == DiceStrategy.MAX:
            dice_strat = MaxStrategy(dices)
        elif self.reader.dice_strategy == DiceStrategy.MIN:
            dice_strat = MinStrategy(dices)

        game = Game(board, dice_strat, players)
        return game

