from typing import Tuple

from .tile import Tile, TileAction

class Crocodile(Tile):
    def __init__(self, move_delta=5):
        super().__init__(is_special=False)
        self.is_special = True
        self.move_delta = move_delta

    def action_message(self):
        return f" was bitten by a crocodile, will be moving back {self.move_delta} steps" # Figure out

    def tile_action(self) -> Tuple[TileAction, int]:
        return TileAction.GOTO_DELTA, self.move_delta
