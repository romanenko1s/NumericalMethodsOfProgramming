import numpy as np
import math
from scipy.misc import derivative

a = int(input("введіть а: "))
b = int(input("введіть b: "))
e = float(input("введіть e(точність): "))

def f(x):
    return 3*x**4-4*x**3+x**2-2*x-3 


if (f(a)*derivative(f, a, n = 2)>0):
    x0 = a
    xi = b
else:
    x0 = b
    xi = a
xi_1 = xi-(xi - x0) * f(xi)/(f(xi) - f(x0))

while (abs(xi_1 - xi) > e):
    xi = xi_1
    xi_1 = xi-(xi - x0) * f(xi)/(f(xi) - f(x0))

print("x = {}".format(xi_1))