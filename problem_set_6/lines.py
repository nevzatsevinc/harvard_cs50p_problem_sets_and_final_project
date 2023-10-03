"""
Problem Set 6 - Lines of Code
https://cs50.harvard.edu/python/2022/psets/6/lines/
"""

import sys


def main():
    # Check command-line arguments
    check_argv(sys.argv)
    # Read the file and count
    counted_lines = read_file(sys.argv[1]) 
    print(counted_lines)


def check_argv(argv):
    # Check the number of command-line arguments
    if len(argv) == 2:
        file_name = (argv[1])
        # Check is a Python file
        if file_name.endswith(".py"):
            return True
        else:
            sys.exit("Not a Python file")
    elif len(argv) < 2:
        sys.exit("Too few command-line arguments")
    elif len(argv) > 2:
        sys.exit("Too many command-line arguments")


def read_file(file_name):
    try:
        with open(file_name, "r") as file:
            line_count = 0
            # Strip leading whitespaces and check it is a comment or blank.
            for line in file:
                line = line.lstrip()
                if not line.startswith("#") and line != "":
                    line_count += 1
            return line_count
    except FileNotFoundError:
        print("File does not exist")


if __name__ == "__main__":
    main()