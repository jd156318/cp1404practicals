"""
CP1404/CP5632 - Practical
Program to determine score status
"""
from random import randint


def main():
    # Determine and print score status for user input
    score = float(input("Enter score: "))
    status = determine_score_status(score)
    print(f"User status {score} is {status}")
    if 100 >= score >= 90:
        print("You get a prize!")

    # Determine and print score status for random input
    score = randint(0, 100)
    status = determine_score_status(score)
    print(f"Random: {score} = {status}")


def determine_score_status(score):
    if score < 0 or score > 100:
        return "Invalid score"
    elif score >= 90:
        return "Excellent"
    elif score >= 50:
        return "Passable"
    else:
        return "Bad"


main()
