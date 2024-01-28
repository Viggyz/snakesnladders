from .base import BaseDiceStrategy


class SumStrategy(BaseDiceStrategy):
    def __init__(self, *args, **kwargs):
        super(SumStrategy).__init__(*args, **kwargs)

    def roll_dice(self):
        return sum(dice.roll() for dice in self.dice)