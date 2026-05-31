expression = input("expression: ")

x, y, z = expression.split()
x = float(x)
z = float(z)

if y == '+':
    print(round(x + z, 1))
elif y == '-':
    print(round(x - z, 1))
elif y == '*':
    print(round(x * z, 1))
elif y == '/':
    print(round(x / z, 1))
else:
    print("Invalid operation")