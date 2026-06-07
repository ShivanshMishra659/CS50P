def main():

    user_input = input(
        "What is the Great Question of Life, the Universe and Everything? ").lower().strip()
# .strip() cleans unwanted spaces in string

    if user_input == "42" or user_input == "forty-two" or user_input == "forty two" or user_input == " 42 ":
        print("Yes")
    else:
        print("No")


if __name__ == "__main__":
    main()