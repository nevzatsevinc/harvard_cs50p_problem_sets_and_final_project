"""
Problem Set 7 - Regular, um, Expressions
https://cs50.harvard.edu/python/2022/psets/7/um/
"""

from um import count

def test_basic():
    assert count("hello, um, world") == 1

def test_case_insensitive():
    assert count("Hello, Um, World") == 1

def test_not_substring():
    assert count("yummy, mummy") == 0

def test_multiple_occurrences():
    assert count("um um UM um") == 4

def test_empty_string():
    assert count("") == 0