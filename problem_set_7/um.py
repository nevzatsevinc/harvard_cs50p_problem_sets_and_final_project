"""
Problem Set 7 - Regular, um, Expressions
https://cs50.harvard.edu/python/2022/psets/7/um/
"""

import re


def main():
    print(count(input("Text: ")))

def count(s):
    # \bum\b for "um" as a whole word
    pattern = re.compile(r'\bum\b', re.IGNORECASE)

    # Find all occurrences of the pattern in the input string
    matches = pattern.findall(s)

    # Return the number of matches
    return len(matches)

if __name__ == "__main__":
    main()