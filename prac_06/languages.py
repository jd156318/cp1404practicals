"""
Practical 06
Use ProgrammingLanguage class to store and get key data about programming languages.
"""

from prac_06 import programming_language
from prac_06.programming_language import ProgrammingLanguage

python = ProgrammingLanguage("Python", "Dynamic", True, 1991)
ruby = ProgrammingLanguage("Ruby", "Dynamic", True, 1995)
visual_basic = ProgrammingLanguage("Visual Basic", "Static", False, 1991)
print(python)

language_objects = [python, ruby, visual_basic]

print(f"The dynamically typed languages are:")
for language_object in language_objects:
    if language_object.is_dynamic():
        print(language_object.language)
