"""
Problem Set 6 - Scourgify
https://cs50.harvard.edu/python/2022/psets/6/scourgify/
"""

import sys
import csv


def main():
    # Check command-line arguments
    check_argv(sys.argv)
    # Read and save file
    read_save_file(sys.argv[1])



def check_argv(argv):
    # Check the number of command-line arguments
    if len(argv) == 3:
        file_name = (argv[1])
        # Check is a csv file
        if file_name.endswith(".csv"):
            return True
        else:
            sys.exit("Not a CSV file")
    elif len(argv) < 3:
        sys.exit("Too few command-line arguments")
    elif len(argv) > 3:
        sys.exit("Too many command-line arguments")


def read_save_file(file_name):
    edited_dict = []

    try:
        # Read the input file
        with open(file_name, "r") as file:
            reader = csv.DictReader(file)
            for row in reader:
                last_name, first_name = row["name"].split(",")
                last_name = last_name.strip()
                first_name = first_name.strip()
                house = row["house"]

                edited_dict.append({"first": first_name, "last": last_name, "house": house})

        # Write to the output file
        with open(sys.argv[2], "w") as file:
            fieldnames = ["first", "last", "house"]
            writer = csv.DictWriter(file, fieldnames=fieldnames)
            writer.writeheader()

            for row in edited_dict:
                first_name = row["first"]
                last_name = row["last"]
                house = row["house"]

                writer.writerow({"first": first_name, "last": last_name, "house": house})

    except FileNotFoundError:
        sys.exit(f"Could not read {sys.argv[1]}")


if __name__ == "__main__":
    main()