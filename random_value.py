import random

class Dice:
    def roll():
        number1 = random.randint(1, 6)
        number2 = random.randint(1, 6)
        result = (number1, number2)
        print(result)

Dice.roll()