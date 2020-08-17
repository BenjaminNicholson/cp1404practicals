"""
CP1404/CP5632 - Practical
files
"""

get_name = input("What is your name: ")
out_file = open("names.txt", "w")
out_file.write(get_name)
out_file.close()

out_file = open("names.txt", "r")
file_contents = out_file.read().strip()
out_file.close()
print("Your name is: ", file_contents)

in_file = open("numbers.txt", "r")
number1 = int(in_file.readline())
number2 = int(in_file.readline())
in_file.close()
print(number1 + number2)

in_file = open("numbers.txt", "r")
total = 0
for line in in_file:
    number = int(line)
    total += number
in_file.close()
print(total)
