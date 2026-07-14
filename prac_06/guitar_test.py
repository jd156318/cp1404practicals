"""
CP1404 Practical
Import Guitar class and test it
"""

from prac_06.guitar import Guitar

gibson = Guitar("Gibson L-5 CES", 1922, 16035.40)
other = Guitar("Another Guitar", 2013, 6450.12)

print(gibson)
print(other)

print(f"{gibson.name} get_age() - Expected 104. Got {gibson.get_age()}")
print(f"{other.name} get_age() - Expected 13. Got {other.get_age()}")
print(f"{gibson.name} is_vintage - Expected True. Got {gibson.is_vintage()}")
print(f"{other.name} is_vintage - Expected False. Got {other.is_vintage()}")
