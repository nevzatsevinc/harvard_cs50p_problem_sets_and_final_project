"""
Problem Set 6 - CS50 P-Shirt
https://cs50.harvard.edu/python/2022/psets/6/shirt/
"""

import sys
from PIL import Image, ImageOps
import os

def main():
    # Check command-line arguments
    check_argv(sys.argv)
    edit_picture(sys.argv)


def check_argv(argv):
    # Check the number of command-line arguments
    if len(argv) == 3:
        file_name_1 = argv[1]
        file_name_2 = argv[2]

        file_ext_1 = os.path.splitext(file_name_1.lower())
        file_ext_2 = os.path.splitext(file_name_2.lower())
        # Check extensions are same
        if not file_ext_1[1] == file_ext_2[1]:
            sys.exit("Input and output have different extensions")
        # Check is a jpg, jpeg or png
        if file_name_1.lower().endswith(".jpg") or file_name_1.lower().endswith(".jpeg") or file_name_1.lower().endswith(".png"):
            if file_name_2.lower().endswith(".jpg") or file_name_2.lower().endswith(".jpeg") or file_name_2.lower().endswith(".png"):
                return True
            else:
                    sys.exit("Invalid input")
        else:
            sys.exit("Invalid input")
    elif len(argv) < 3:
        sys.exit("Too few command-line arguments")
    elif len(argv) > 3:
        sys.exit("Too many command-line arguments")


def edit_picture(file_name):

    try:
        # Open the images
        shirt = Image.open("shirt.png")
        photo = Image.open(sys.argv[1])
        # Resize the photo
        size = shirt.size
        photo = ImageOps.fit(photo, size)
        # Paste the shirt on the photo
        photo.paste(shirt, shirt)
        # Save the result
        photo.save(sys.argv[2])

    except FileNotFoundError:
        sys.exit(f"Could not read {sys.argv[1]}")


if __name__ == "__main__":
    main()