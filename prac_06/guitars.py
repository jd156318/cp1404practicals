"""
CP1404 Practical
Store user's guitars and print key information.
Estimate: 20
Actual: 35
"""

from prac_06.guitar import Guitar

guitars = []
print("My guitars!")
name = input("Name: ")
while name != "":
    year = int(input("Year: "))
    cost = float(input("Cost: $"))
    guitars.append(Guitar(name=name, year=year, cost=cost))
    print(f"{guitars[-1]} added.\n")
    name = input("Name: ")

if guitars:
    max_length_name = max(len(guitar.name) for guitar in guitars)
    max_length_cost = max(len(f"{guitar.cost:,.2f}") for guitar in guitars)

    print("These are my guitars:")
    for i, guitar in enumerate(guitars, 1):
        vintage_string = " (vintage)" if guitar.is_vintage() else ""
        print(f"Guitar {i}: {guitar.name:>{max_length_name}}, worth "
              f"${guitar.cost:>{max_length_cost},.2f}{vintage_string}")
else:
    print("No guitars")
