"""
Practical CP1404
Guitar class with name, start date, priority, cost estimate, and project completion percentage.
"""


class Project:
    """Project class for storing data about a project."""

    def __init__(self, name, start_date, priority, cost, completion_percentage):
        """Initialise a Project."""
        self.name = name
        self.start_date = start_date
        self.priority = priority
        self.cost = cost
        self.completion_percent = completion_percentage
