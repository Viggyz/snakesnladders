from typing import Tuple

from .tile import Tile, TileAction

class Ladder(Tile):
    def __init__(self, lift_position: int):
        super(Ladder).__init__(is_special=True)
        self.lift_position = lift_position

    def action_message(self):
        return f" has reached a ladder, will climb to {self.lift_position}" # Figure out

    def tile_action(self) -> Tuple[TileAction, int]:
        return TileAction.GOTO, self.lift_position
