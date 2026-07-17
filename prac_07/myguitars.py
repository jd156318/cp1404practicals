"""
CP1404 Practical

"""
import csv

from prac_07.guitar import Guitar


def main():
    guitars = read_data_into_guitar_classes()
    guitars.sort()


def read_data_into_guitar_classes():
    guitars = []
    with open("guitars.csv") as in_file:
        reader = csv.reader(in_file)
        for name, year, cost in reader:
            guitars.append(Guitar(name, int(year), float(cost)))
    return guitars


main()
