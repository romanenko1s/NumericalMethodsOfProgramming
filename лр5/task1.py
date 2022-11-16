from scipy import optimize
import math

x = float(input("Введіть наближений х: "))
y = float(input("Введіть наближений у: "))
eps = float(input("Введіть похибку: "))

def f1(x):
    return 1 - math.cos(x) # = x

def f2(y):
    return -1 + math.sin(y + 1) # = y

xn = x
yn = y
xn1 = f2(x)
yn1 = f1(y)

while ((abs(xn1-xn)>=eps) & (abs(yn1-yn) >=eps)):
    xn = xn1
    yn = yn1
    xn1 = f2(yn)
    yn1 = f1(xn)

print ('x=', yn, '\ny=',xn)


def f3(x):
    return 1 - math.cos(x[1]) - x[0], -1 +math.sin(x[0]+1) - x[1]

s = optimize.root(f3, [0.,0.], method= "hybr")

print ("Перевірка: ",s.x)