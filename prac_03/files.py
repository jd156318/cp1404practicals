name = input("Your name: ")

# 1.
file_out = open("name.txt", 'w')
print(f"{name}", file=file_out)
file_out.close()

# 2.
file_in = open("name.txt")
line = (file_in.readline())
print(f"Hi {line.strip()}")
file_in.close()

# 3.
with open("numbers.txt") as file_in:
    line1 = float(file_in.readline())
    line2 = float(file_in.readline())
    print(f"Answer = {line1 + line2:.0f}")

# 4.
total = 0
with open("numbers.txt") as file_in:
    for line in file_in:
        total = total + float(line)
print(f"Total = {total:.0f}")
