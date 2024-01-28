from typing import Tuple

from .tile import Tile, TileActions

class Snake(Tile):
    def __init__(self, drop_position: int):
        super(Snake).__init__(is_special=False)
        self.is_special = True
        self.drop_position = drop_position

    def action_message(self):
        return f"was bitten by a snake, will be moved to" # Figure out

    def tile_action(self) -> Tuple[TileActions, int]:
        return TileActions.GOTO, self.drop_position