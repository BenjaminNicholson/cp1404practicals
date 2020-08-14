"""
Benjamin Nicholson
CP1404 Menus
This program has a menu structure that says hello, goodbye and determines invalid input
"""

name = input("Enter name: ")
print("(H)ello\n", "(G)oodbye\n", "(Q)uit")
choice = input("Choice: ").upper()
while choice != "Q":
    if choice == "H":
        print(f"Hello {name}")
    elif choice == "G":
        print(f"Goodbye {name}")
    else:
        print("Invalid choice")
    print("(H)ello\n", "(G)oodbye\n", "(Q)uit")
    choice = input("Choice: ").upper()
print("Goodbye")
