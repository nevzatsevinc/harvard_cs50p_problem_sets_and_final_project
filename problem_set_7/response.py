"""
Problem Set 7 - Response Validation
https://cs50.harvard.edu/python/2022/psets/7/response/
"""

from validator_collection import validators, errors


email = input("What's your email address? ")

try:
    # Attempting to validate the email address. If it's invalid or empty (since allow_empty=False), an exception is raised.
    email_address = validators.email(email, allow_empty = False)
    print("Valid")
except errors.InvalidEmailError:
    print("Invalid")
except ValueError:
    print("Invalid")