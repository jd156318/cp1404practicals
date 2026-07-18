"""
Practical CP1404
Guitar class with name, start date, priority, cost estimate, and project completion percentage.
"""

from datetime import datetime


class Project:
    """Project class for storing data about a project."""

    def __init__(self, name="", start_date="00/00/0000", priority=0, cost=0.0, completion_percentage=0):
        """Initialise a Project."""
        self.name = name
        self.start_date = datetime.strptime(start_date, "%d/%m/%Y").date()
        self.priority = priority
        self.cost = cost
        self.completion_percent = completion_percentage

    def is_after_date(self, input_date):
        """Return true if the project started after the input_date."""
        return self.start_date > input_date

    def __str__(self):
        """Format object data to print neatly."""
        return (f"{self.name}, start: {datetime.strftime(self.start_date, "%d/%m/%Y")}, priority {self.priority}, "
                f"estimate: ${self.cost}, completion: {self.completion_percent}%")

    def __lt__(self, other):
        """Self is less than other if it has an earlier start date."""
        return self.start_date < other.start_date
