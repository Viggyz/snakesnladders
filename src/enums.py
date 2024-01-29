from enum import Enum


class SpecialTile(Enum):
    SNAKE = 'SNK'
    LADDER = 'LDR'
    CROCODILE = 'CDL'


class DiceStrategy(Enum):
    MAX = 'MAX'
    MIN = 'MIN'
    SUM = 'SUM'
