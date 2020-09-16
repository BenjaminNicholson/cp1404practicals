"""Drink class."""


# name, price, alcohol_content (%), volume

class Drink:
    MINIMUM_ALCOHOL_THRESHOLD = 0.01

    def __init__(self, name="", price=0.0, volume=0.0, alcohol_content=0.0, ):
        self.name = name
        self.price = price
        self.alcohol_content = alcohol_content
        self.volume = volume

    def __str__(self):
        return "{self.name}, ${self.price:.2f}, {self.volume}mL, ({self.alcohol_content})%".format(self=self)

    def get_alcohol_volume(self):
        return (self.alcohol_content / 100) * self.volume

    def is_alcoholic_drink(self):
        if self.alcohol_content >= self.MINIMUM_ALCOHOL_THRESHOLD:
            return True
        else:
            return False


def run_tests():
    d1 = Drink()
    print(d1)

    d2 = Drink("Pina Colada", 12.30, 450, 12.5)
    d3 = Drink("Coffee", 4.5, 280, 0)
    print(d2)
    print(d2.is_alcoholic_drink())
    total_alcohol = 0
    count_alcoholic_drinks = 0
    drinks = [d2, d2, d3]
    for drink in drinks:
        if drink.is_alcoholic_drink():
            count_alcoholic_drinks += 1
        total_alcohol += drink.get_alcohol_volume()
    print("You drank {} drinks ({} were alcoholic for a total of {} ml alcohol)".format(len(drinks),
                                                                                        count_alcoholic_drinks,
                                                                                        total_alcohol))
    print(Drink.is_alcoholic_drink(self=d2))


if __name__ == '__main__':
    run_tests()
