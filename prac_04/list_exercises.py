"""
CP1404 Practical
List exercises
"""

# 1. Numbers stuff
numbers = []

for i in range(5):
    numbers.append(int(input("Enter number: ")))

for i in range(len(numbers)):
    print(f"Number: {numbers[i]}")

print(f"The first number is {numbers[0]}")
print(f"The last number is {numbers[-1]}")
print(f"The smallest number is {min(numbers)}")
print(f"The largest number is {max(numbers)}")
print(f"The average of the numbers is {sum(numbers) / len(numbers)}")

# 2. Woefully inadequate security checker...
usernames = ['jimbo', 'giltson98', 'derekf', 'WhatSup', 'NicolEye', 'swei45', 'BaseInterpreterInterface', 'BaseStdIn',
             'Command', 'ExecState', 'InteractiveConsole', 'InterpreterInterface', 'StartServer', 'bob']

test_username = input("Username: ")
if test_username in usernames:
    print("Access granted")
else:
    print("Access denied")
