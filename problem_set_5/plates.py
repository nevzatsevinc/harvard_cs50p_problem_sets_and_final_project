def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    first_number = False

    # Check length
    if len(s) < 2 or len(s) > 6:
        return False

    # Check first two characters
    if not (s[0].isalpha() and s[1].isalpha()):
        return False

    # Check periods, spaces, or punctuation.
    for c in s:
        if not c.isalnum():
            return False

    # Check for numbers
    for c in s:
        if c.isdigit():
            if first_number:
                continue
            else:
                if c == '0':
                    return False
                first_number = True
        # A letter after numbers have started
        elif first_number:
            return False
    return True


if __name__ == "__main__":
    main()