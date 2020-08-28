import random

NUMBER_PER_LINE = 5
MINIMUM = 1
MAXIMUM = 45


def main():
    number_of_quick_picks = int(input("How many quick picks do you want? "))
    while number_of_quick_picks <= 0:
        print("That's not right, try again")
        number_of_quick_picks = int(input("How many quick picks do you want? "))

    for i in range(number_of_quick_picks):
        quick_picks = []
        for j in range(NUMBER_PER_LINE):
            number = random.randrange(MINIMUM, MAXIMUM)
            while number in quick_picks:
                number = random.randrange(MINIMUM, MAXIMUM)
            quick_picks.append(number)
        quick_picks.sort()
        print(" ".join("{:2}".format(number) for number in quick_picks))

main()
