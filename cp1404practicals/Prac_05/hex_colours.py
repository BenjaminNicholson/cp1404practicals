COLOURS = {'AliceBlue': '#f0f8ff', 'Aquamarine1': '#7fffd4', 'AntiqueWhite': '#faebd7', 'azure1': '#f0ffff',
           'aquamarine4': '#458b74', 'azure4': '#838b8b', 'blue1': '#0000ff', 'BlueViolet': '#8a2be2',
           'brown3': '#cd3333'}

print(COLOURS)

choice = input("Which colour do you want to pick? ")
while choice != "":
    if choice in COLOURS:
        print("{} is {}".format(choice, COLOURS[choice]))
    else:
        print("Invalid option, try again")
    choice = input("Which colour do you want to pick? ")
