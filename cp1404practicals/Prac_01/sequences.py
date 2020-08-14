"""
Benjamin Nicholson
CP1404 Extension tasks
"""


def main():
    print("(E)ven\n"
          "(O)dd\n"
          "(S)quare\n"
          "(Q)uit")
    choice = input("Choose: ").upper()
    while choice != "Q":
        if choice == "E":
            number_x = int(input("Even number 1: "))
            number_y = int(input("Even number 2: "))
            for i in range(number_x, number_y, 2):
                print(i + 1, end=" ")
            print()
        elif choice == "O":
            number_x = int(input("Odd number 1: "))
            number_y = int(input("Odd number 2: "))
            for i in range(number_x, number_y, 2):
                print(i, end=" ")
            print()
        elif choice == "S":
            number_x = int(input("Number 1: "))
            number_y = int(input("Number 2: "))
            for i in range(number_x, number_y, ):
                if i ** .5 == int(i ** .5):  # calculates the square for each number in the range
                    print(i, end=" ")
            print()
        else:
            print("Invalid option")
        print("(E)ven\n"
              "(O)dd\n"
              "(S)quare\n"
              "(Q)uit")
        choice = input("Choose: ").upper()
    print("Goodbye")


main()
