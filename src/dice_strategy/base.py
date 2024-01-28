from abc import ABC, abstractmethod
from typing import List

from ..dice import Dice


class BaseDiceStrategy(ABC):
    def __init__(self, dices: List[Dice]):
        self.dice: List[Dice] = dices

    @abstractmethod
    def roll_dice(self):
        ...
        