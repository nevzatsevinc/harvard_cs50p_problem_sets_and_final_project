"""
Problem Set 4 - Frank, Ian and Glen’s Letters
https://cs50.harvard.edu/python/2022/psets/4/figlet/
"""

"""
from pyfiglet import Figlet
figlet = Figlet()

You can then get a list of available fonts with code like this:
figlet.getFonts()

You can set the font with code like this, wherein f is the font’s name as a str:
figlet.setFont(font=f)

You can output text in that font with code like this, wherein s is that text as a str:
print(figlet.renderText(s))
"""

import sys
import random
from pyfiglet import Figlet


def main():
    figlet = Figlet()
    # f is the font’s name
    f = check_argv() 
    user_input = input("Input: ")
    figlet.setFont(font=f)
    print(figlet.renderText(user_input))


def check_argv():
    """
    Check argv then return the font’s name
    """
    figlet = Figlet()
    if len(sys.argv) == 1:
        return random.choice(figlet.getFonts())
    elif len(sys.argv) == 3:
        if sys.argv[1] == '-f' or sys.argv[1] == '--font':
            if sys.argv[2] in figlet.getFonts():
                return sys.argv[2]
            else:
                sys.exit("Invalid usage")
        else:
            sys.exit("Invalid usage")
    else:
        sys.exit("Invalid usage")


main()