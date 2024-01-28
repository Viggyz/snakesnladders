from .base import BaseDiceStrategy


class MaxStrategy(BaseDiceStrategy):
    def __init__(self, *args, **kwargs):
        super(MaxStrategy).__init__(*args, **kwargs)

    def roll_dice(self):
        return max(dice.roll() for dice in self.dice)