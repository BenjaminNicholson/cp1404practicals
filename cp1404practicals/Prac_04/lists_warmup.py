# numbers[0] = [3]
# numbers[-1] = [2]
# numbers[3] = [1]
# numbers[:-1] = [3, 1, 4, 1, 5, 9]
# numbers[3:4] = [1]
# 5 in numbers = True
# 7 in numbers = False
# "3" in numbers = False
# numbers + [6, 5, 3] = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3]


# numbers = [3, 1, 4, 1, 5, 9, 2]
# for n, i in enumerate(numbers):
#     if i == 3:
#         numbers[n] = "10"
# print(numbers)
#
# numbers += [1]
# print(numbers)
#
# print(numbers[2:])
#
# for j in enumerate(numbers):
#     if 9 in j:
#         print("Yes 9 is in list")

scores = []
score = int(input("Score: "))
if not scores:
    print("Sorry first input can't be negative")
    score = int(input("Score: "))
    scores.append(score)
    while score >= 0:
        scores.append(score)
        score = int(input("Score: "))
print("You highest score is {}".format(max(scores)))
