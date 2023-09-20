"""
Problem Set 1 - Deep Thought
https://cs50.harvard.edu/python/2022/psets/1/deep/
"""

# Prompt the user for input
user_input = input("What is the Answer to the Great Question of Life, the Universe, and Everything? ")

# Convert the input to lowercase
user_input = user_input.lower()

# Check if the input matches any of the expected answers
if user_input == '42' or user_input == 'forty-two' or user_input == 'forty two':
    print('Yes')
else:
    print('No')