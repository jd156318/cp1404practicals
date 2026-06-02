x = int(input("X: "))
y = int(input("Y: "))

print(f"1. Show the even numbers from {x} to {y}\n"
      f"2. Show the odd numbers from {x} to {y}\n"
      f"3. Show the squares of the numbers from {x} to {y}\n"
      "4. Exit the program")

choice = input("Choice: ")

while choice != '4':
    if choice == '1':
        is_x_odd = x % 2
        for i in range(x + is_x_odd, y + 1, 2):
            print(f"{i}", end=' ')
        print()

    elif choice == '2':
        is_x_odd = x % 2
        for i in range(x - is_x_odd + 1, y + 1, 2):
            print(f"{i}", end=' ')
        print()

    elif choice == '3':
        for i in range(x, y + 1):
            squared = i*i
            print(f"{squared}", end=' ')
        print()

    else:
        print("Invalid choice!")

    print(f"1. Show the even numbers from {x} to {y}\n"
          f"2. Show the odd numbers from {x} to {y}\n"
          f"3. Show the squares of the numbers from {x} to {y}\n"
          "4. Exit the program")

    choice = input("Choice: ")

print("Finished.")
