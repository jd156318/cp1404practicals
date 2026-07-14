"""
CP1404 Practical
Define Guitar class with name, year made, and cost.
Estimate: 15
Actual: 16
"""
from datetime import datetime


class Guitar:
    """Guitar class for storing data about a guitar."""

    def __init__(self, name="", year=0, cost=0.0):
        """Initialise a Guitar."""
        self.name = name
        self.year = year
        self.cost = cost

    def __str__(self):
        """Return data of a Guitar in a string."""
        return f"{self.name} ({self.year}) : ${self.cost:,.2f}"

    def get_age(self):
        """Return current age of guitar."""
        return datetime.now().year - self.year

    def is_vintage(self):
        """Return true/false for whether a guitar is vintage or not."""
        return Guitar.get_age(self) >= 50
