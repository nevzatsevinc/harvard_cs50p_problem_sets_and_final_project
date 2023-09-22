"""
Problem Set 3 - Fuel Gauge
https://cs50.harvard.edu/python/2022/psets/3/fuel/#fuel-gauge
"""

def main():
    fraction = fuel("fraction x/y ")

    # Check the value
    if fraction <= 1:
        print("E")
    elif fraction >= 99:
        print("F")
    else:
        print(f"{fraction}%")


def fuel(s):
    # Continue prompting the user until a valid fraction is entered
    while True:
        try:
            x, y = input(s).split('/')
            frac = round((int(x) / int(y))*100)
            if frac > 100:
                continue
            else:
                # Return the calculated fraction
                return frac
        except ValueError:
            pass
        except ZeroDivisionError:
            pass
        else:
            break


main()