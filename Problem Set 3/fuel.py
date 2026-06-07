while True:
    fuel_fraction = input("Fraction: ")
    try:
        x, y = fuel_fraction.split("/")
        x = int(x)
        y = int(y)
        if x < 0 or y < 0:
            raise ValueError
        fuel_result = int(round((x/y), ndigits=2) * 100)
        if fuel_result > 100:
            raise ValueError
        break
    except (ValueError, ZeroDivisionError):
        pass

if fuel_result <= 1:
    print("E")
elif fuel_result >= 99:
    print("F")
else:
    print(fuel_result, "%", sep="")
