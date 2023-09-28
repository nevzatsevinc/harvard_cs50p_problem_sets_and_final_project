def main():
    # Prompt the user for input
    user_input = input('Input: ')
    output = shorten(user_input)
    print('Output:', output)


def shorten(word):
    output = ''
    vowels = ['A', 'E', 'I', 'O', 'U', 'a', 'e', 'i', 'o', 'u']

    # Loop each character in the user input
    for c in word:
        # if it's a vowel
        if c in vowels:
            continue
        # if not a vowel add the character to the output
        else:
            output += c
    return output


if __name__ == "__main__":
    main()