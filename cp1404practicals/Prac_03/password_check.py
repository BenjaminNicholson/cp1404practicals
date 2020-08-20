"""
Benjamin Nicholson CP1404
Gets a password then prints an asterisk as long as the password
"""

LENGTH = 10


def main():
    password = get_valid_password()
    print_asterisks(password)


def get_valid_password():
    password = input("Enter a password between 0 and 10: ")
    while len(password) < 0 or len(password) > 10:
        print("Sorry that is too long, try again")
        password = input("Enter a password between 0 and 10: ")
    return password


def print_asterisks(password):
    print("*" * len(password))


main()
