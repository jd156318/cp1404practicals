minimum_length_of_password = 5
password = input("Password: ")
while len(password) < minimum_length_of_password:
    print("Password to short!")
    password = input("Password: ")

print('*' * len(password))
