"""
Problem Set 5 - Back to the Bank
https://cs50.harvard.edu/python/2022/psets/5/test_bank/
"""

from bank import value


def test_value():
    assert value("Hello, Newman") == 0
    assert value("How you doing?") == 20
    assert value("What's happening?") == 100