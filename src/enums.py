from enum import Enum


class SpecialTile(Enum):
    SNAKE = 'SNK'
    LADDER = 'LDR'


class DiceStrategy(Enum):
    MAX = 'MAX'
    MIN = 'MIN'
    SUM = 'SUM'
