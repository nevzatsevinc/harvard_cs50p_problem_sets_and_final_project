"""
Problem Set 5 - Refueling
https://cs50.harvard.edu/python/2022/psets/5/test_fuel/
"""

import pytest
from fuel import convert, gauge

def test_convert():
    assert convert("1/4") == 25
    assert convert("2/4") == 50
    assert convert("3/4") == 75

    with pytest.raises(ZeroDivisionError):
        convert('1/0')
    with pytest.raises(ValueError):
        convert('5/3')
    with pytest.raises(ValueError):
        convert('abc/3')


def test_gauge():
    assert gauge(1) == "E"
    assert gauge(99) == "F"
    assert gauge(50) == "50%"