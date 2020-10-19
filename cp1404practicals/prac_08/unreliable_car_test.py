"""
Benjamin Nicholson
CP1404 Unreliable Car practical
Completed on 15/10/2020
"""
from prac_08.unreliable_car import UnreliableCar


def main():
    new_car = UnreliableCar("Ford Falcon", 150, 90)
    print(new_car)
    new_car.drive(100)
    print(new_car)
    new_car.add_fuel(50)
    new_car.drive(50)
    print(new_car)


main()

