"""
CP1404 Prac_06
Guitars collection
Benjamin Nicholson
"""

from prac_06.guitar import Guitar


def main():
    """Guitar program testing Guitar class"""
    print("My guitars!")
    guitars = []
    get_name = input("Name: ")

    while get_name != "":
        year = int(input("Year: "))
        cost = input("Cost: ")
        add_guitar = Guitar(get_name, year, cost)
        guitars.append(add_guitar)
        print(add_guitar, "added")
        get_name = input("Name: ")

    guitars.append(Guitar("Gibson L-5 CES", 1922, 16035.40))
    guitars.append(Guitar("Line 6 JVT-59", 2010, 1512.90))

    if guitars:
        guitars.sort()
        print("These are my guitars!")
        for i, guitar in enumerate(guitars):
            vintage_status = ""
            if guitar.is_vintage():
                vintage_status = "(vintage)"
            print("Guitar {0}: {1.name:>20} ({1.year}), worth ${1.cost:<10}\
            {2}".format(i + 1, guitar, vintage_status))
    else:
        print("No guitars ")


main()
