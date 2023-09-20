"""
Problem Set 1 - File Extensions
https://cs50.harvard.edu/python/2022/psets/1/extensions/
"""

# Prompt the user for input
file_name = input("File name: ")

# Convert the input to lowercase and remove whitespace
file_name = file_name.lower().strip()

# Check for known extensions and output
if file_name.endswith('.gif'):
    print('image/gif')
elif file_name.endswith('.jpg'):
    print('image/jpeg')
elif file_name.endswith('.jpeg'):
    print('image/jpeg')
elif file_name.endswith('.png'):
    print('image/png')
elif file_name.endswith('.pdf'):
    print('application/pdf')
elif file_name.endswith('.txt'):
    print('text/plain')
elif file_name.endswith('.zip'):
    print('application/zip')
else:
    print('application/octet-stream')