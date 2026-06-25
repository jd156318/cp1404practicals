"""
CP1404 - Practical
Read file, process data, and display processed information
Estimate: 35 minutes
Actual: 60 minutes
"""
from typing import Any


def main():
    """Load file from data, process and display results."""
    data = []
    read_file(data)
    champions_to_wins, countries = find_champions_and_number_of_wins(data)
    display_results(champions_to_wins, countries)


def display_results(champions_to_wins: dict[Any, Any], countries: list[Any]):
    """Display champions, number of wins, and winning countries."""
    print("Wimbledon Champions:")
    [print(f"{champion} {wins}") for champion, wins in champions_to_wins.items()]
    print(f"\nThese {len(countries)} countries have won Wimbledon:")
    print(", ".join(countries))


def find_champions_and_number_of_wins(data: list[Any]) -> tuple[dict[Any, Any], list[Any]]:
    """Process data into champions and number of wins dictionary, and list of countries."""
    champions_to_wins = {}
    countries = sorted(list(set(year[1] for year in data)))
    for line in data:
        try:
            champions_to_wins[line[2]] += 1
        except KeyError:
            champions_to_wins[line[2]] = 1
    return champions_to_wins, countries


def read_file(data: list[Any]):
    """Read data into lists of lists."""
    file_in = open("wimbledon.csv", 'r', encoding="utf-8-sig")
    raw_data = file_in.readline()
    for line in file_in.readlines():
        parts = line.strip().split(',')
        data.append(parts)
    file_in.close()


main()
