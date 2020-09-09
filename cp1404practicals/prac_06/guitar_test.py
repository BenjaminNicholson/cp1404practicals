"""
CP1404 Prac_06
Guitar_test
Benjamin Nicholson
"""

from prac_06.guitar import Guitar

my_guitar = Guitar("Gibson L-5 CES", 1922, 16035.40)
print(my_guitar)
print("Expected 98. Got", my_guitar.get_age())
print("Expected True. Got", my_guitar.is_vintage())
your_guitar = Guitar("Another Guitar", 2013, 1672.30)
print(your_guitar)
print("Expected 7. Got", your_guitar.get_age())
print("Expected False. Got", your_guitar.is_vintage())
