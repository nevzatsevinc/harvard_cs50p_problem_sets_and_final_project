"""
Problem Set 0 - Playback Speed
https://cs50.harvard.edu/python/2022/psets/0/playback/
"""

# Prompt the user for input
user_input = input("Enter some text: ")

# Replacing each space with ...
slow_user_input = user_input.replace(" ", "...")

# Print the replaced input
print(slow_user_input)

