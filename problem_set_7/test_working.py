"""
Problem Set 7 - Working 9 to 5
https://cs50.harvard.edu/python/2022/psets/7/working/
"""

import pytest
from working import convert

def test_convert_true_times():
    assert convert("9:00 AM to 5:00 PM") == "09:00 to 17:00"
    assert convert("9 AM to 5 PM") == "09:00 to 17:00"
    assert convert("12:00 AM to 12:00 PM") == "00:00 to 12:00"
    assert convert("12 PM to 12 AM") == "12:00 to 00:00"


def test_convert_false_times():
    with pytest.raises(ValueError):
        convert("13:00 AM to 1:00 PM")
    with pytest.raises(ValueError):
        convert("9:60 AM to 5:00 PM")


def test_convert_false_formats():
    with pytest.raises(ValueError):
        convert("9:00AM to 5:00 PM")
    with pytest.raises(ValueError):
        convert("9 to 5")
    with pytest.raises(ValueError):
        convert("9 PM 11 PM")
