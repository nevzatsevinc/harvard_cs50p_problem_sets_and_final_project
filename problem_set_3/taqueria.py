"""
Problem Set 3 - Felipe’s Taqueria
https://cs50.harvard.edu/python/2022/psets/3/taqueria/
"""

menu = {
    "Baja Taco": 4.00,
    "Burrito": 7.50,
    "Bowl": 8.50,
    "Nachos": 11.00,
    "Quesadilla": 8.50,
    "Super Burrito": 8.50,
    "Super Quesadilla": 9.50,
    "Taco": 3.00,
    "Tortilla Salad": 8.00
}

total = 0

while True:
    try:
        # Prompt the user to 
        item = input("Item: ").lower().title()
        if item in menu:
            total += menu[item]
            print(f"Total: ${total:.2f}" )
        else:
            continue
    except EOFError:
        # Break the loop if the user inputs control-d (EOF)
        print("")
        break