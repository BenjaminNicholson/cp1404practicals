def main():
    """Create dictionary of emails and names."""

    emails_and_names = {}
    get_email = input("Email: ")
    while get_email != "":
        name = get_name_from_email(get_email)
        confirmation = input("Is this your name {}? (Y/N)".format(name))
        if confirmation.upper() != "y" and confirmation.upper() != "":
            name = input("Name: ")
        emails_and_names[get_email] = name
        get_email = input("Email: ")

    for email, name in emails_and_names.items():
        print("{} {}".format(name, email))


def get_name_from_email(get_email):
    prefix = get_email.split("@")[0]
    parts = prefix.split(".")
    name = " ".join(parts).title()
    return name


main()
