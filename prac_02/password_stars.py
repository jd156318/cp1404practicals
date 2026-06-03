def main():
    minimum_length_of_password = 5
    password = get_password(minimum_length_of_password)

    print_asterisks(password)


def print_asterisks(password: str):
    print('*' * len(password))


def get_password(minimum_length_of_password: int) -> str:
    password = input("Password: ")
    while len(password) < minimum_length_of_password:
        print("Password to short!")
        password = input("Password: ")
    return password


main()
