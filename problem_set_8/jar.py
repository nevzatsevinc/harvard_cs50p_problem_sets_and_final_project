"""
Problem Set 8 - Cookie Jar
https://cs50.harvard.edu/python/2022/psets/8/jar/
"""

class Jar:
    def __init__(self, capacity=12):
        if not isinstance(capacity, int) or capacity < 0:
            raise ValueError("ValueError")
        self._capacity = capacity
        self._size = 0

    def __str__(self):
        return "🍪" * self._size

    def deposit(self, n):
        if not isinstance(n, int) or n < 0:
            raise ValueError("ValueError")
        if self._size + n > self._capacity:
            raise ValueError("ValueError")
        self._size += n

    def withdraw(self, n):
        if not isinstance(n, int) or n < 0:
            raise ValueError("ValueError")
        if self._size < n:
            raise ValueError("ValueError")
        self._size -= n

    @property
    def capacity(self):
        return self._capacity

    @property
    def size(self):
        return self._size
