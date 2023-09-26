"""
Problem Set 4 - Guessing Game
https://cs50.harvard.edu/python/2022/psets/4/game/
"""

import random

def main():
    # Get a level
    level = get_positive_integer("Level: ")
    # Generate a random number between 1 and level
    secret_number = random.randint(1, level)

    # Keep prompting the user to guess the secret number until it is guessed correctly
    while True:
        guess = get_positive_integer("Guess: ")
        if guess < secret_number:
            print("Too small!")
        elif guess > secret_number:
            print("Too large!")
        else:
            print("Just right!")
            break


def get_positive_integer(prompt):
    # Keep prompting the user until a positive integer is entered
    while True:
        try:
            value = int(input(prompt))
            if value > 0:
                return value
            else:
                pass
        except ValueError:
            pass


if __name__ == "__main__":
    main()