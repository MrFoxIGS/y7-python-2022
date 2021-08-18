import random

again = input("press [enter] to roll the dice, type q to quit")

while again != 'q':
    print(random.randint(1,6))
    again = input()
