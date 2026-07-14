"""
CP1404/CP5632 Practical - Client code to use the Car class.
Code updated to work with updated Car class.
"""

from prac_06.car import Car


def main():
    """Demo test code to show how to use car class."""
    my_car = Car("Car", 180)
    limo = Car("Limo", 100)
    limo.add_fuel(20)
    print(f"{limo}")
    limo.drive(115)
    print(f"{limo}")
    my_car.drive(30)
    print(f"{my_car}")
    patrol = Car(fuel=500)
    print(patrol)


main()
