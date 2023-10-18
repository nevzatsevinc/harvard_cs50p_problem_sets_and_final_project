"""
Problem Set 8 - Seasons of Love
https://cs50.harvard.edu/python/2022/psets/8/seasons/
"""

import sys
from datetime import date
import inflect


class AgeCalculator:
    def __init__(self, birthdate):
        self.birthdate = birthdate
        self.inflect_engine = inflect.engine()

    def get_age_in_minutes(self):
        age = date.today() - self.birthdate
        return age.days * 24 * 60

    def get_age_in_words(self):
        age_minutes = self.get_age_in_minutes()
        return self.inflect_engine.number_to_words(age_minutes).capitalize().replace(" and ", " ")


def main():
    date_input = input("Date of Birth (YYYY-MM-DD): ")
    
    try:
        birthdate = date.fromisoformat(date_input)
    except ValueError:
        sys.exit("Invalid date")
    
    age_calculator = AgeCalculator(birthdate)
    print(f"{age_calculator.get_age_in_words()} minutes")


if __name__ == "__main__":
    main()