"""
Problem Set 0 - Making Faces
https://cs50.harvard.edu/python/2022/psets/0/faces/
"""

def main():
    # Prompt the user for input
    user_input = input("Enter some text: ")

    # Call the convert function
    converted_text = convert(user_input)

    # Print the converted text
    print(converted_text)


def convert(text):
    # Function to convert emoticons to emoji

    # Replace :) to 🙂
    text = text.replace(":)", "🙂")

    # Replace :( to 🙁
    text = text.replace(":(", "🙁")

    return text


main()

