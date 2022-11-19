import numpy as np

h = 0.08
x0 = 0.6 + h/2

def f(x):
    return 1/((12*x+0.5)**(1/2)) + h/2

while x0 <= 1.4:
    print(round(x0, 2), round(f(x0), 4))
    x0 += h