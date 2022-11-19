import numpy as np

def f(x):
    return np.sin((x**2) - 1)/(2*(x**(1/2)))

h = 0.1
x0 = 1.3

while x0 <= 2.1:
    print(round(x0, 2), round(f(x0), 4))
    x0 += h