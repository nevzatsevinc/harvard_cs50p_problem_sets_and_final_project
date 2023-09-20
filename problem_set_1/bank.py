"""
Problem Set 1 - Home Federal Savings Bank
https://cs50.harvard.edu/python/2022/psets/1/bank/
"""

# Prompt the user for input
user_input = input("Greeting: ")

# Convert the input to lowercase and remove leading whitespace
user_input = user_input.lower().lstrip()

 # Check conditions and output
if user_input.startswith('hello'):
    print('$0')
elif user_input.startswith('h'):
    print('$20')
else:
    print('$100')