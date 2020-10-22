"""
Benjamin Nicholson
CP1404 Unreliable Car Test
Completed on 15/10/2020
"""


from prac_08.car import Car
import random


class UnreliableCar(Car):

    def __init__(self, name="", fuel=0, reliability=0):
        super().__init__(name, fuel)
        self.reliability = reliability

    def __str__(self):
        return "{}, fuel = {}, odometer = {}".format(self.name, self.fuel, self.odometer)

    def drive(self, distance):
        random_number = random.randint(0, 200)
        if random_number >= self.reliability:
            distance = 0
        distance_driven = super().drive(distance)
        return distance_driven




