"""
Practical CP1404
Estimate: 1 hour
start: 19+2:56

"""
from datetime import datetime
from typing import Any

from prac_07.project import Project

DEFAULT_FILE = "projects.txt"


def main():
    print("Welcome to Pythonic Project Management")
    projects = read_file_into_projects_list(DEFAULT_FILE)
    choice = get_menu_choice()
    while choice != "Q":
        if choice == "L":
            load_filename = input("Load file: ")
            projects.append(load_filename)
        if choice == "S":
            save_project_data_to_file(projects)
        if choice == "D":
            pass
        if choice == "F":
            filter_project_objects_by_date(projects)
        if choice == "A":
            pass
        if choice == "U":
            pass
        choice = get_menu_choice()


def save_project_data_to_file(projects: list[Any]):
    """Save project data to user specified filename."""
    save_filename = input("Save to file: ")
    with open(save_filename, "w", newline="") as out_file:
        for project in projects:
            out_file.write(f"{project.name}\t{datetime.strftime(project.start_date, "%d/%m/%Y")}\t"
                           f"{project.priority}\t{project.cost}\t{project.completion_percent}\n")


def filter_project_objects_by_date(projects: list[Any]):
    """Print project objects that started after user specified date."""
    filtered_projects = []
    date_string = input("Show projects that start after date (dd/mm/yy): ")
    date = datetime.strptime(date_string, "%d/%m/%Y").date()
    for project in projects:
        if project.is_after_date(date):
            filtered_projects.append(project)
    filtered_projects.sort()
    for i in range(len(filtered_projects)):
        print(filtered_projects[i])


def get_menu_choice():
    """Print menu and get user selection."""
    print("- (L)oad projects\n- (S)ave projects\n- (D)isplay projects\n- (F)ilter projects by date\n- (A)dd new project"
          "\n- (U)pdate project\n- (Q)uit")
    return input(">>> ").upper()


def read_file_into_projects_list(filename) -> list[Any]:
    """Read specified file into Project objects and store in list."""
    projects = []
    with open(filename) as in_file:
        in_file.readline()  # Don't read header line in file
        lines = in_file.readlines()
        for line in lines:
            # Split line into parts at tab
            parts = line.strip().split("\t")
            print(parts)
            projects.append(Project(*parts))
    print(f"Loaded {len(projects)} projects from {filename}")
    return projects


main()
