"""
Problem Set 3 - Grocery List
https://cs50.harvard.edu/python/2022/psets/3/grocery/
"""

grocery_list = {}

while True:
    try:
        # Prompt the user to
        item = input().lower()
        if item in grocery_list:
            grocery_list[item] += 1
        else:
            grocery_list[item] = 1

    except EOFError:
        # Break the loop if the user inputs control-d (EOF)
        break

# Sort items alphabetically and print them in uppercase
for item, how_many in sorted(grocery_list.items()):
    print(how_many, item.upper())