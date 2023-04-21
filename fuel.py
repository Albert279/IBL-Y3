"""
    The function takes user input for a fuel fraction, calculates the percentage of fuel remaining, and
    prints out a corresponding message based on the percentage.
    """

def main ():
    final_fuel = get_percent()
    percent_fuel = round(final_fuel * 100)
    if percent_fuel <= 1:
        print("E")
    elif percent_fuel >= 99:
        print("F")
    else:
        print(f"{percent_fuel}%")


def get_percent():
    try:
        while True:
            fraction = input("Fuel Fraction: ")
            x, y = fraction.split('/')
            x = int(x)
            y = int(y)
            fuel = x/y
            if fuel <= 1:
                return fuel

    except (ValueError, ZeroDivisionError):
        pass

    
        main()
