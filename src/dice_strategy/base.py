from abc import ABC, abstractmethod
from typing import List

from ..dice import Dice


class BaseDiceStrategy(ABC):
    def __init__(self, dices: List[Dice]):
        self.dice: List[Dice] = dices

    @abstractmethod
    def get_roll_value(self, rolls):
        ...

    def roll_dice(self):
        rolls = [dice.roll() for dice in self.dice]
        selected = self.get_roll_value(rolls)
        return selected, self.gen_msg(rolls, selected)

    def gen_msg(self, rolls, selected):
        return f' has rolled {" ".join(map(str, rolls))}, final roll is {selected}'
        