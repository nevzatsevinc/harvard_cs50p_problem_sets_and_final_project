"""
Problem Set 5 - Testing my twttr
https://cs50.harvard.edu/python/2022/psets/5/test_twttr/
"""

from twttr import shorten


def test_shorten():
    assert shorten("Hello, World") == "Hll, Wrld"
    assert shorten("Harvard University CS50") == "Hrvrd nvrsty CS50"
    assert shorten("Angaranin baglari") == "ngrnn bglr"