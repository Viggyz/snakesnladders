from typing import Tuple

from .tile import Tile, TileAction

class Mine(Tile):
    def __init__(self, freeze_duration: int):
        super().__init__(is_special=False)
        self.is_special = True
        self.freeze_duration = freeze_duration

    def action_message(self):
        return f" has landed on a mine, cannot move for {self.freeze_duration} turns"  # Figure out

    def tile_action(self) -> Tuple[TileAction, int]:
        return TileAction.FREEZE, self.freeze_duration
