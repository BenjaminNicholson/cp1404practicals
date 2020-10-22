"""
CP1404 Practical sort_files_2
Benjamin Nicholson
Completed 22/10/2020
"""

import os


def main():
    categories = {}
    os.chdir("FilesToSort")
    os.chdir("FilesToSort")
    for filename in os.listdir("."):
        if os.path.isdir(filename):
            continue

        file_extension = filename.split(".")[-1]
        if file_extension not in categories:
            category = input("What category would you like to sort {} files into?".format(file_extension))
            categories[file_extension] = category
            try:
                os.mkdir(category)
            except FileExistsError:
                pass

        os.rename(filename, "{}/{}".format(categories[file_extension], filename))


main()