def main():
    time = convert(input("What time is it? "))
    if 8 >= time >= 7:
        print("Breakfast time")
    elif 13 >= time >= 12:
        print("Lunch time")
    elif 19 >= time >= 18:
        print("Dinner time")


def convert(time):
    h , m = time.split(":")
    return float(h) + (float(m)/60)



if __name__ == "__main__":
    main()