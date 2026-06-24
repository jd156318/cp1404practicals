"""
CP1404 Practical
Colour hex codes in a dictionary
"""
# Available program colours
NAME_TO_CODE = {"absolute zero": "#0048ba", "amethyst": "#9966cc", "aqua": "#00ffff", "rust": "#b7410e",
                "blue green": "#0d98ba", "red1": "#ff0000", "rose": "#ff007f", "salmon": "#fa8072",
                "scarlet": "#ff2400"}

# Display available colours
print("Colours in program are:")
for name in NAME_TO_CODE:
    print(name)

colour = input("Enter colour: ").lower()

# Display hex code if user colour is in dictionary
while colour != "":
    try:
        print(f"{colour} has hex code {NAME_TO_CODE[colour]}")
    except KeyError:
        print(f"{colour} is not in program")
    colour = input("Enter colour: ").lower()
