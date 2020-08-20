"""
Benjamin Nicholson CP10404
Gets number of scores, calculates them then prints them to a file
"""

import random


def main():
    number_of_scores = int(input("How many scores do you want: "))
    for i in range(1, number_of_scores + 1):
        score = random.randrange(0, 101)
        s = calculate_score(score) * i
        out_file = open("results.txt", "w")
        out_file.write(s)
        out_file.close()


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

