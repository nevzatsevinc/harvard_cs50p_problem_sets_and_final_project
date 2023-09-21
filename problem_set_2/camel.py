"""
Problem Set 2 - camelCase
https://cs50.harvard.edu/python/2022/psets/2/camel/
"""

# Prompt the user for input
camel_case = input("camelCase: ")

snake_case = ""

# convert camel case to snake case
for char in camel_case:
    # If the character is uppercase
    if char.isupper():
        snake_case += '_' + char.lower()
    else:
        snake_case += char

# Output the snake_case
print(snake_case)