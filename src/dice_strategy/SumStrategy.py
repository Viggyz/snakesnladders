from .base import BaseDiceStrategy


class SumStrategy(BaseDiceStrategy):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
    def get_roll_value(self, rolls):
        return sum(rolls)