import random


class Dice:
    def roll():
        result = (random.randint(1, 6), random.randint(1, 6))
        return result


result = Dice.roll()
print(result)
