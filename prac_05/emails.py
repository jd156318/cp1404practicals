"""
CP1404 - Practical
Count how many times a word occurs
Estimate: 15 minutes
Actual: 20 minutes
"""
email_to_name = {}


def main():
    email = input("Email: ")

    while email != "":
        name = extract_name(email)
        correct = input(f"Is your name {name}? (Y/n) ")
        if correct != "" and correct.upper() != 'Y':
            name = input(f"Name: ")
        email_to_name[email] = name
        email = input("Email: ")

    [print(f"{name} ({email})") for email, name in email_to_name.items()]


def extract_name(email):
    """Extract name from user email"""
    split_name = [word.title() for word in email.split('@')[0].split('.')]
    full_name = " ".join(split_name)
    return full_name


main()
