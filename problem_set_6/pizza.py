"""
Problem Set 6 - Pizza Py
https://cs50.harvard.edu/python/2022/psets/6/pizza/
"""

import sys
import csv
from tabulate import tabulate


def main():
    # Check command-line arguments
    check_argv(sys.argv)
    # Read the file and print
    formated_text = read_file(sys.argv[1]) 
    print(formated_text)


def check_argv(argv):
    # Check the number of command-line arguments
    if len(argv) == 2:
        file_name = (argv[1])
        # Check is a csv file
        if file_name.endswith(".csv"):
            return True
        else:
            sys.exit("Not a CSV file")
    elif len(argv) < 2:
        sys.exit("Too few command-line arguments")
    elif len(argv) > 2:
        sys.exit("Too many command-line arguments")


def read_file(file_name):
    headers = []
    table = []

    try:
        with open(file_name, "r") as file:
            reader = csv.reader(file)
            # Get the header row
            headers = next(reader)
            # Get the remaining data
            table = list(reader)
            
        return tabulate(table, headers, tablefmt="grid")

    except FileNotFoundError:
        sys.exit("File does not exist")


if __name__ == "__main__":
    main()