"""
Problem Set 1 - Meal Time
https://cs50.harvard.edu/python/2022/psets/1/meal/
"""

def main():
    # Prompt the user for input
    time = input("What time is it? ")

    # convert time to float
    converted_time = convert(time)

    # Check for meal time
    if 7.0 <= converted_time <= 8.0:
        print("breakfast time")
    elif 12.0 <= converted_time <= 13.0:
        print("lunch time")
    elif 18.0 <= converted_time <= 19.0:
        print("dinner time")


def convert(time):
    # Function to convert time to float
    hours, minutes = time.split(":")

    return int(hours) + int(minutes) / 60.0


if __name__ == "__main__":
    main()