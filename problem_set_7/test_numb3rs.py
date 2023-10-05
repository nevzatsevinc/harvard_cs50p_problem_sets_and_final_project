"""
Problem Set 7 - NUMB3RS
https://cs50.harvard.edu/python/2022/psets/7/numb3rs/
"""

from numb3rs import validate

def test_true_ips():
    assert validate("127.0.0.1") == True
    assert validate("255.255.255.255") == True
    assert validate("0.0.0.0") == True
    assert validate("11.1.37.218") == True

def test_false_ips():
    assert validate("145.169.11.256") == False
    assert validate("178.211.1") == False
    assert validate("192.168.1.") == False
    assert validate("192.168.1.1.1") == False
    assert validate("cat.dog.dog.cat") == False
    assert validate("") == False