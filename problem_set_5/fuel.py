def main():
    # Prompt the user to enter a fraction
    fraction = input("fraction x/y ")

    try:
        # Convert fraction to percentage
        percentage = convert(fraction)
        # Output the fuel gauge
        print(gauge(percentage))
    except ValueError:
        print("Value Error")
    except ZeroDivisionError:
        print("Zero Division Error")


def convert(fraction):
    # Splitting the fraction
    x, y = fraction.split('/')
    x = int(x)
    y = int(y)

    # Raise ZeroDivisionError
    if y == 0:
        raise ZeroDivisionError()
    # Raise ValueError
    elif x > y:
        raise ValueError()

    # Calculate and return the percentage
    return round((x / y) * 100)


def gauge(percentage):
    if percentage <= 1:
        return "E"
    elif percentage >= 99:
        return "F"
    else:
        return f"{percentage}%"


if __name__ == "__main__":
    main()