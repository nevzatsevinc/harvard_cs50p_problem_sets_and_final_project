"""
Problem Set 4 - Little Professor
https://cs50.harvard.edu/python/2022/psets/4/professor/
"""

import random

def main():
    # Get the level of difficulty
    level = get_level()
    # Keep track of correct answers
    score = 0
    # Ask 10 questions
    for _ in range(10):
        x , y = generate_integer(level)
        # Check if the answer is correct
        for i in range(3):
            try:
                z = int(input(f"{x} + {y} = "))
                if z == (x + y):
                    score += 1
                    break
                else:
                    print("EEE")
            except ValueError:
                print("EEE")
            # After 3 attempts, display the correct answer.
            print(f"{x} + {y} = {x+y}")
    print(f"Score: {score}")
     

def get_level():
    # A valid level is chosen
    while True:
        level = input("Level: ")

        if level == '1':
            return 1
        elif level == '2':
            return 2
        elif level == '3':
            return 3
        else:
            pass


def generate_integer(level):
    # Based on the level, generate two random integers
    if level == 1:
        x = random.randint(0,9)
        y = random.randint(0,9)
        return x, y
    elif level == 2:
        x = random.randint(10,99)
        y = random.randint(10,99)
        return x, y
    elif level == 3:
        x = random.randint(100,999)
        y = random.randint(100,999)
        return x, y


if __name__ == "__main__":
    main()