word_list = ["Fender Stratocaster, {}, ${}".format(2014, 765.40), "Gibson L-5 CES, {}, ${}".format(1992, 16035.40),
             "Line 6 JTV-59, {}, ${}".format(2010, 1512.90)]

out_file = open("out_file.txt", "w")
for word in word_list:
    out_file.write(word + '\n')
out_file.close()

out_file = open("out_file.txt", "r")
first_line_str = out_file.readline(0)
for line_str in out_file:
    print(line_str)
out_file.close()


import string


def count_string_letters(text):
    count = 0
    for character in text:
        if character.lower() in string.ascii_letters:
            count += 1
        return count