for i in range(1, 21, 2):
    print(i, end=' ')
print()

# a
for i in range(0, 101, 10):
    print(i, end=' ')
print()

# b
for i in range(20, -1, -1):
    print(i, end=' ')
print()

# c
number_of_stars = int(input("Number of stars: "))
for star in range(number_of_stars):
    print("*", end='')
print()

# d
number_of_lines = int(input("Number of lines: "))
for line in range(number_of_lines):
    for star_per_line in range(line + 1):
        print("*", end='')
    print()
print()
