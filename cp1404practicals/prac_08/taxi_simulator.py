"""
CP1404 Practicals taxi simulator
Benjamin Nicholson
"""
from prac_08.car import Car
from prac_08.taxi import Taxi
from prac_08.silver_service_taxi import SilverServiceTaxi

MENU = "q)uit, c)hoose taxi, d)rive"


def main():
    total_bill = 0
    taxis = [Taxi("Prius", 100), SilverServiceTaxi("Limo", 100, 2), SilverServiceTaxi("Hummer", 200, 4)]

    print(MENU)
    choice = input(">>> ").lower()
    while choice != "q":
        if choice == "c":
            print("Taxis available:")
            display_taxis(taxis)
            choose_taxi = int(input("Choose taxi: "))
            current_taxi = taxis[choose_taxi]
        elif choice == "d":
            current_taxi.start_fare()
            drive_distance = float(input("Drive how far?"))
            current_taxi.drive(drive_distance)
            cost_of_trip = current_taxi.get_fare()
            print("Your {} trip cost you ${:.2f}".format(current_taxi.name, cost_of_trip))
            total_bill += cost_of_trip
        else:
            print("Invalid option")
        print("Your bill to date ${:.2f}".format(total_bill))
        print(MENU)
        choice = input(">>> ").lower()

    print("Total trip cost: ${:.2f}".format(total_bill))
    print("Taxis are now:")
    display_taxis(taxis)


def display_taxis(taxis):
    for i, taxi in enumerate(taxis):
        print("{} - {}".format(i, taxi))


main()