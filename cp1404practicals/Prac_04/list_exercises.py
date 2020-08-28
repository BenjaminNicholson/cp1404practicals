# numbers = []
# while len(numbers) < 5:
#     number = int(input("Numbers: "))
#     numbers.append(number)
# average = sum(numbers) / len(numbers)
# print("The first number is {}".format(numbers[0]))
# print("The last number is {}".format(numbers[-1]))
# print("The smallest number is {}".format(min(numbers)))
# print("The largest number is {}".format(max(numbers)))
# print("The average of the numbers is {}".format(average))

usernames = ['jimbo', 'giltson98', 'derekf', 'WhatSup', 'NicolEye', 'swei45', 'BaseInterpreterInterface', 'BaseStdIn', 'Command', 'ExecState', 'InteractiveConsole', 'InterpreterInterface', 'StartServer', 'bob']

name = input("What is your username? ")
if name in usernames:
    print("Access granted")
else:
    print("Access denied")
