"""
CP1404 Practical
Read guitar data from a csv to Guitar objects, add user's guitars and write all Guitars back to csv
"""
import csv

from typing import Any

from prac_07.guitar import Guitar


def main():
    """Read/write guitar data from/to a csv file, with user input adding to guitar data"""
    guitars = read_data_into_guitar_classes()
    get_guitar_to_store_as_object(guitars)
    guitars.sort()
    write_guitars_to_csv(guitars)


def write_guitars_to_csv(guitars: list[Any]):
    """Write Guitar objects to csv file"""
    with open("guitars.csv", "w", newline='') as out_file:
        writer = csv.writer(out_file)
        for guitar in guitars:
            writer.writerow([guitar.name, guitar.year, guitar.cost])


def get_guitar_to_store_as_object(guitars: list[Any]):
    """Get user guitar data, create and save new Guitar object to guitar list"""
    name = input("Name: ")
    while name != "":
        year = int(input("Year: "))
        cost = float(input("Cost: $"))
        guitars.append(Guitar(name=name, year=year, cost=cost))
        print(f"{guitars[-1]} added.\n")
        name = input("Name: ")


def read_data_into_guitar_classes():
    """Open csv, read data, and save to list as a Guitar object"""
    guitars = []
    with open("guitars.csv") as in_file:
        reader = csv.reader(in_file)
        for name, year, cost in reader:
            guitars.append(Guitar(name, int(year), float(cost)))
    return guitars


main()
