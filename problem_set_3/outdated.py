"""
Problem Set 3 - Outdated
https://cs50.harvard.edu/python/2022/psets/3/outdated/
"""

month_list = [
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December"
]

while True:
    # Prompt the user to enter a date
    date_input = input("Date: ")

    try:
        # If date is MM/DD/YYYY format
        month, day, year = date_input.split('/')
        year = int(year)
        month = int(month)
        day = int(day)
        if month <= 12 and day <= 31:
            print(f"{year:04d}-{month:02d}-{day:02d}")
            break
        else:
            continue
    except ValueError:
        try:
            # If date is September 8, 1636 format
            month, day, year = date_input.split(' ')
            year = int(year)
            month = month.lower().capitalize()
            if not ',' in day:
                continue
            day = day.rstrip(',')
            day = int(day)
            if month in month_list:
                month_digit = month_list.index(month) + 1
                if month_digit <= 12 and day <= 31:
                    print(f"{year:04d}-{month_digit:02d}-{day:02d}")
                    break
                else:
                    continue
        except ValueError:
            continue