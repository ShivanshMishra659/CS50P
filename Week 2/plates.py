def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    numbers_used = False
    if len(s) > 6 or len(s) < 2:
        return False
    if not s.isalnum():
        return False
    if not s[0:2].isalpha():
        return False
    for c in s:
        if c.isdigit():
            if numbers_used == False:
                if c == '0':
                    return False
            numbers_used = True
        else:
            if numbers_used:
                return False
    return True


if __name__ == "__main__":
    main()