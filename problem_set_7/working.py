"""
Problem Set 7 - Working 9 to 5
https://cs50.harvard.edu/python/2022/psets/7/working/
"""

import re


def main():
    print(convert(input("Hours: ")))


def convert(s):
    # Test formats of  9:00 AM to 5:00 PM or 9 AM to 5 PM
    match = re.match(r"^([1-9]|1[0-2])(:[0-5][0-9])? (AM|PM) to ([1-9]|1[0-2])(:[0-5][0-9])? (AM|PM)$", s)

    if not match:
        raise ValueError("ValueError")

    start_hour = match.group(1)
    start_minute = match.group(2)
    start_meridiem = match.group(3)
    end_hour = match.group(4)
    end_minute = match.group(5)
    end_meridiem = match.group(6)

    if start_meridiem == "AM":
        if int(start_hour) < 10:
            start_hour = "0" + start_hour
        elif int(start_hour ) == 12:
            start_hour = "00"
    elif start_meridiem == "PM":
        if not int(start_hour) == 12:
            start_hour = str(int(start_hour) + 12)

    if end_meridiem =="AM":
        if int(end_hour) < 10:
            end_hour = "0" + end_hour
        elif int(end_hour ) == 12:
            end_hour = "00"
    elif end_meridiem == "PM":
        if not int(end_hour) == 12:
            end_hour = str(int(end_hour) + 12)

    if not start_minute:
        start_minute = ":00"

    if not end_minute:
        end_minute = ":00"

    return start_hour + start_minute + " to " + end_hour + end_minute


if __name__ == "__main__":
    main()