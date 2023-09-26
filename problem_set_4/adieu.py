"""
Problem Set 4 - Adieu, Adieu
https://cs50.harvard.edu/python/2022/psets/4/adieu/
"""

"""
JOIN WORDS INTO A LIST:
import inflect
p = inflect.engine()
p.join(("apple", "banana", "carrot"))
"apple, banana, and carrot"
"""

import inflect

names = []
p = inflect.engine()

while True:
    try:
        names.append(input("Name: "))
    except EOFError:
        print("")
        print("Adieu, adieu, to " + p.join(names))
        break