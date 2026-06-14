"""
CP1404 - Do-from-scratch Exercises
Lottery Ticket Generator
"""
from random import randint

RANDOM_NUMBERS_PER_LINE = 6
MINIMUM_RANDOM_NUMBER = 1
MAXIMUM_RANDOM_NUMBER = 45

quick_picks = int(input("How many quick picks? "))

for i in range(quick_picks):
    random_numbers = []

    for x in range(RANDOM_NUMBERS_PER_LINE):
        number = randint(MINIMUM_RANDOM_NUMBER, MAXIMUM_RANDOM_NUMBER + 1)
        while number in random_numbers:
            number = randint(MINIMUM_RANDOM_NUMBER, MAXIMUM_RANDOM_NUMBER + 1)
        random_numbers.append(number)

    str(random_numbers.sort())
    print(' '.join(f"{random_number:2}" for random_number in random_numbers))
