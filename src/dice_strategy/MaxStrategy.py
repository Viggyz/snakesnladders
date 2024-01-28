from .base import BaseDiceStrategy


class MaxStrategy(BaseDiceStrategy):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def get_roll_value(self, rolls):
        return max(rolls)