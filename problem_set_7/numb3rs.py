"""
Problem Set 7 - NUMB3RS
https://cs50.harvard.edu/python/2022/psets/7/numb3rs/
"""

import re

def main():
    print(validate(input("IPv4 Address: ")))


def validate(ip):
    """
    input is string
    Returns bool
    """
    if  pattern := re.search(r"^(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)$", ip):
        return True
    else:
        return False


if __name__ == "__main__":
    main()