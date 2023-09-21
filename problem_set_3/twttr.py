"""
Problem Set 2 - Just setting up my twttr
https://cs50.harvard.edu/python/2022/psets/2/twttr/
"""

# Prompt the user for input
user_input = input('Input: ')

output = ''
vowels = ['A', 'E', 'I', 'O', 'U', 'a', 'e', 'i', 'o', 'u']

# Loop each character in the user input
for c in user_input:
    # if it's a vowel
    if c in vowels:
        continue
    # if not a vowel add the character to the output
    else:
        output += c

print('Output:', output)