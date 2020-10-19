from prac_08.silver_service_taxi import SilverServiceTaxi


def main():
    new_taxi = SilverServiceTaxi("Silver Star", 100, 2)
    new_taxi.start_fare()
    new_taxi.drive(100)
    print(new_taxi)
    print(new_taxi.get_fare())


main()
