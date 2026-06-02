"""
Practical for CP1404
Program for shop calculator
"""
from loops import number_of_stars

total_price = 0
number_of_items = int(input("Number of items: "))

while number_of_items < 0:
    print("Invalid number of items!")
    number_of_items = int(input("Number of items: "))

for item in range(number_of_items):
    price = float(input("Price of item: "))
    total_price = total_price + price

print(f"Total price for {number_of_items} items is ${total_price:.2f}")
