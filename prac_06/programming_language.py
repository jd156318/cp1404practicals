"""
Practical 06 - Programming language class.
Estimated: 30
Actual: 18
"""


class ProgrammingLanguage:
    def __init__(self, language, typing, reflection, year):
        self.language = language
        self.typing = typing
        self.reflection = reflection
        self.year = year

    def is_dynamic(self):
        """Returns true if the language is dynamically typed, else returns false"""
        if self.typing == "Dynamic":
            return True
        return False

    def __str__(self):
        return f"{self.language}, {self.typing} typing, Reflection={self.reflection}, First appeared in {self.year}"
