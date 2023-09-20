"""
Problem Set 1 - Math Interpreter
https://cs50.harvard.edu/python/2022/psets/1/interpreter/
"""

# Prompt the user for input
expression = input("Expression x y z: ")

# Split expression using space
x, y, z = expression.split()

#Convert from string to integer
x = int(x)
z = int(z)

match y:
    case '+':
        print(f'{(x+z):.1f}')
    case '-':
        print(f'{(x-z):.1f}')
    case '*':
        print(f'{(x*z):.1f}')
    case '/':
        if z != 0:
            print(f'{(x/z):.1f}')
        else:
            print('z = 0 not allowed')