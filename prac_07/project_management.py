"""
Practical CP1404
Estimate: 1 hour
start: 19+2:56

"""
from typing import Any

from prac_07.project import Project

DEFAULT_FILE = "projects.txt"


def main():
    print("Welcome to Pythonic Project Management")
    projects = read_file_into_projects_list(DEFAULT_FILE)
    choice = get_menu_choice()


def get_menu_choice():
    """Print menu and get user selection."""
    print("- (L)oad projects\n- (S)ave projects\n- (D)isplay projects\n- (F)ilter projects by date\n- (A)dd new project"
          "\n- (U)pdate project\n- (Q)uit")
    return input(">>> ")


def read_file_into_projects_list(filename) -> list[Any]:
    """Read specified file into Project objects and store in list."""
    projects = []
    with open(filename) as in_file:
        in_file.readline()  # Don't read header line in file
        lines = in_file.readlines()
        for line in lines:
            parts = line.split()
            # Format name into one string
            edited_parts = parts[-5:]
            edited_parts[0] = " ".join(parts[0:-4])
            print(edited_parts)
            projects.append(Project(*edited_parts))
    print(f"Loaded {len(projects)} projects from {filename}")
    return projects


main()
