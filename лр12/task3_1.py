import numpy as np

def f(x):
    return 1/((1+2*x**2)**(1/2))

h = 0.045
x0 = 0.6

while x0 <= 1.5:
    print(round(x0, 3), round(f(x0), 4))
    x0 += h