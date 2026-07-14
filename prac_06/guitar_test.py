"""
CP1404 Practical
Import Guitar class and test it
"""

from prac_06.guitar import Guitar

gibson = Guitar("Gibson L-5 CES", 1922, 16035.40)
print(gibson)
print(gibson.get_age())
print(gibson.is_vintage())
