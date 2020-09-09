"""CP1404/CP5632 Practical - Client code to use the Car class."""
# Note that the import has a folder (module) in it.

from prac_06.car import Car, Limo


def main():
    """Demo test code to show how to use car class."""
    my_car = Car("Lamborghini", 319)
    my_car.drive(277)
    print("fuel =", my_car.fuel)
    print("odo =", my_car.odometer)
    print(my_car)

    print("Car {}, {}".format(my_car.fuel, my_car.odometer))
    print("Car {self.fuel}, {self.odometer}".format(self=my_car))

    limo = Limo("Limo", 100)
    limo.add_fuel(20)
    limo.drive(115)
    print(limo.odometer)
    print("fuel =", limo.fuel)
    print("odo = ", limo.odometer)


main()
