"""
Problem Set 8 - Cookie Jar
https://cs50.harvard.edu/python/2022/psets/8/jar/
"""

import pytest
from jar import Jar

def test_init():
    # Test with default capacity
    jar = Jar()
    assert jar.capacity == 12
    assert jar.size == 0
    
    # Test with specified capacity
    jar = Jar(10)
    assert jar.capacity == 10
    assert jar.size == 0
    
    # Test with invalid capacity
    with pytest.raises(ValueError):
        Jar(-1)
    with pytest.raises(ValueError):
        Jar("a")

def test_deposit():
    jar = Jar(10)
    
    # Test normal deposit
    jar.deposit(5)
    assert jar.size == 5
    
    # Test over deposit
    with pytest.raises(ValueError):
        jar.deposit(6)
    
    # Test invalid deposit
    with pytest.raises(ValueError):
        jar.deposit(-1)
    with pytest.raises(ValueError):
        jar.deposit("a")

def test_withdraw():
    jar = Jar(10)
    jar.deposit(5)
    
    # Test normal withdraw
    jar.withdraw(3)
    assert jar.size == 2
    
    # Test over withdraw
    with pytest.raises(ValueError):
        jar.withdraw(3)
    
    # Test invalid withdraw
    with pytest.raises(ValueError):
        jar.withdraw(-1)
    with pytest.raises(ValueError):
        jar.withdraw("a")


def test2_str():
    jar = Jar()
    assert str(jar) == ""
    jar.deposit(1)
    assert str(jar) == "🍪"
    jar.deposit(11)
    assert str(jar) == "🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪"