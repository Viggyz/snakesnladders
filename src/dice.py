import random


class Dice:
    def __init__(self, sides=6):
        assert sides >= 1, "Sides cannot be less than 1"
        self.sides = sides

    def roll(self):
        return random.randint(1, self.sides)
