"""
Problem Set 8 - Seasons of Love
https://cs50.harvard.edu/python/2022/psets/8/seasons/
"""

import pytest
from datetime import date, timedelta
import seasons

def test_get_age_in_minutes():
    birthdate = date.today() - timedelta(days=1)  # 1 day old
    age_calculator = seasons.AgeCalculator(birthdate)
    assert age_calculator.get_age_in_minutes() == 1440  # 1 day = 1440 minutes


def test_get_age_in_words():
    birthdate = date.today() - timedelta(days=1)  # 1 day old
    age_calculator = seasons.AgeCalculator(birthdate)
    assert age_calculator.get_age_in_words() == "One thousand, four hundred forty"  # 1 day = 1440 minutes