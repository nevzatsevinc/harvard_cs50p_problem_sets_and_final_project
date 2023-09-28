def main():
    # Prompt the user for input
    user_input = input("Greeting: ")
    output = value(user_input)
    print(f"${output}")


def value(greeting):
    # Convert the input to lowercase and remove leading whitespace
    greeting = greeting.lower().lstrip()

    # Check conditions and output
    if greeting.startswith('hello'):
        return 0
    elif greeting.startswith('h'):
        return 20
    else:
        return 100


if __name__ == "__main__":
    main()