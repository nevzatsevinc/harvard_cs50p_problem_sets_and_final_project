"""
Problem Set 4 - Emojize
https://cs50.harvard.edu/python/2022/psets/4/emojize/
"""

import emoji

# The user can input emoji codes, or emoji aliases
# List of all emojis in the emoji python package
# https://carpedm20.github.io/emoji/all.html?enableList=enable_list_alias

user_input = input("Input: ")

#conversion of aliases to emojis
print("Output", emoji.emojize(user_input))