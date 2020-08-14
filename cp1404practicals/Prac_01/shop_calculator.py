"""
Benjamin Nicholson
CP1404 Shop Calculator
This calculates the total price of the number of items input and calculates the total discount as well
"""


def main():
    number_of_items = int(input("Number of items: "))
    total_price = 0
    while number_of_items <= 0:  # Determines if there are more than 0 items
        print("Invalid number of items!")
        number_of_items = int(input("Number of items: "))
    for i in range(number_of_items):
        price = float(input("Price of item: "))
        total_price += price
    print()
    if total_price >= 100:  # Determines if discount is needed and calculates the amount
        discount = 0.1 * total_price
        total_price = total_price - discount
    print(f"Total price for {3} items is {total_price:.2f}")


main()
