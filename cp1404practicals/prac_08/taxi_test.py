"""
Benjamin Nicholson
CP1404 taxi practical
Completed on 15/10/2020
"""

from prac_08 import taxi


def main():
    new_taxi = taxi.Taxi("Prius 1", 100)
    new_taxi.drive(40)
    print(new_taxi)
    new_taxi.start_fare()
    new_taxi.drive(100)
    print(new_taxi, new_taxi.current_fare_distance)


main()
