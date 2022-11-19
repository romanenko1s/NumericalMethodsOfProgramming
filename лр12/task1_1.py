import numpy as np

def f(x):
    return 1/((12*x+0.5)**(1/2))

h = 0.08
x0 = 0.6

while x0 <= 1.5:
    print(round(x0, 2), round(f(x0), 4))
    x0 += h