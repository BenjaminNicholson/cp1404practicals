"""
CP1404/CP5632 - Practical
Broken program to determine score status
"""
import random


def main():
    score = int(input("Enter score: "))
    result = calculate_score(score)
    print(result)
    score = random.randint(0, 100)
    print(score)
    print(calculate_score(score))


def calculate_score(score):
    if score < 0 or score > 100:
        return "Invalid score"
    elif score >= 90:
        return "Excellent"
    elif score >= 50:
        return "Passable"
    else:
        return "Bad"


main()
