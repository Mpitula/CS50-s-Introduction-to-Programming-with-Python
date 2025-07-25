def main():
    plate = input("Plate: ").upper()
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")



def is_valid(s):
    # Length between 2 and 6
    if not (2 <= len(s) <= 6):
        return False

    # First two characters must be letters
    if not s[0].isalpha() or not s[1].isalpha():
        return False

    # Numbers must be at the end and first number can't be 0
    found_number = False
    for i in range(len(s)):
        if s[i].isdigit():
            if not found_number:
                # First digit encountered
                found_number = True
                if s[i] == '0':
                    return False  # Rule 4: First number can't be 0
            else:
                continue  # All good: still in number section
        else:
            if found_number:
                return False  # Rule 3: Letter after number

    # No punctuation or special characters
    if not s.isalnum():
        return False

    return True

main()

