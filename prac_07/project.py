"""
Practical CP1404
Guitar class with name, start date, priority, cost estimate, and project completion percentage.
"""

from datetime import datetime


class Project:
    """Project class for storing data about a project."""

    def __init__(self, name="", start_date: date = date.min, priority=0, cost=0.0, completion_percentage=0):
        """Initialise a Project."""
        self.name = name
        self.start_date = start_date
        self.priority = priority
        self.cost = cost
        self.completion_percent = completion_percentage

    def is_after_date(self, input_date):
        """Return true if the project started after the input_date."""
        return self.start_date > input_date

    def is_complete(self):
        """Return true if the project is completed (completion_percent = 100%)."""
        return self.completion_percent == 100

    def __str__(self):
        """Format object data to print neatly."""
        return (f"{self.name}, start: {datetime.strftime(self.start_date, "%d/%m/%Y")}, priority {self.priority}, "
                f"estimate: ${self.cost:.2f}, completion: {self.completion_percent}%")

    def __lt__(self, other):
        """Self is less than other if it has an earlier start date."""
        return self.start_date < other.start_date
