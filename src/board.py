import logging
from typing import List, Tuple

from .special_tiles.tile import Tile, TileAction
from .player import Player

logger = logging.getLogger('Main')


class Board:
    def __init__(self, tiles=100):
        self.tiles = [Tile() for _ in range(tiles+1)]
        self.tiles[1].set_starting()
        self.tiles[-1].set_winning()

        self._player_locations = {} # Pos, player

    def is_valid_tile(self, position):
        return 0 < position <= len(self.tiles) - 1

    def add_special_tiles(self, tiles: List[Tuple[Tile, int]]):
        for tile, position in tiles:
            # verify if valid positioning outside method while building game
            assert isinstance(tile, Tile) and tile.is_special, tile
            self.tiles[position] = tile

    def set_player_location(self, player: Player, position: int):
        tile = self.tiles[position]
        if len(tile.players) and self._player_locations[list(tile.players)[0]] != 1 and not self.tiles[self._player_locations[list(tile.players)[0]]].is_winning:
            reset_player = list(tile.players)[0]
            logger.info("Player %s found at position %d, moving to starting", reset_player, self._player_locations[reset_player])
            self.set_player_location(reset_player, 1)
        tile.add_player(player)
        if player in self._player_locations:
            self.tiles[self._player_locations[player]].remove_player(player)
        self._player_locations[player] = position

    def place_player_on_board(self, player: Player, position: int):
        assert not self.is_player_on_board(player)
        assert 0 < position < len(self.tiles) - 2  # Cannot be on winning tile
        tile = self.tiles[position]
        assert not tile.is_special
        assert not tile.is_winning
        self.set_player_location(player, position)

    def move_player(self, player: Player, position_delta: int) -> bool: # Could be negative in case of snakes
        player_pos = self._player_locations[player]
        new_pos = player_pos + position_delta
        has_won = False
        if self.is_valid_tile(new_pos):
            tile = self.tiles[new_pos]
            logger.info(f"{player} has moved from {player_pos} to {new_pos}")
            self.set_player_location(player, new_pos)
            if tile.is_special:
                action, value = tile.tile_action()
                if action == TileAction.GOTO:
                    new_pos = value
                elif action == TileAction.GOTO_DELTA:
                    new_pos = new_pos - value
                logger.info("%s", str(player) + tile.action_message())
                self.set_player_location(player, new_pos)
            has_won = self.tiles[new_pos].is_winning
        else:
            logger.info("%s cannot move to %d, remains at %d", str(player), new_pos, player_pos)
        return has_won

    def is_player_on_board(self, player: Player):
        # self._player_locations.get(Player, False)
        return player in self._player_locations
