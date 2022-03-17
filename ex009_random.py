import random


class Dice:
    def roll(self):
        result = (random.randint(1, 6), random.randint(1, 6))
        return result


dice = Dice()
print(dice.roll())
