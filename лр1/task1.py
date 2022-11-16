x1 = float(input("Введіть x1: "))
X1 = float(input("Введіть X1: "))
x2 = float(input("Введіть x2: "))
X2 = float(input("Введіть X2: "))

dx1 = abs((x1 - X1)/x1)
dx2 = abs((x2 - X2)/x2)

if dx1 < dx2:
    print("Перша рівність точніша")
elif dx1 > dx2:
    print("Друга рівність точніша")
else:
    print("Рівності однаково точні")