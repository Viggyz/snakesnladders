from .base import BaseDiceStrategy


class MinStrategy(BaseDiceStrategy):
    def __init__(self, *args, **kwargs):
        super(MinStrategy).__init__(*args, **kwargs)

    def roll_dice(self):
        return min(dice.roll() for dice in self.dice)