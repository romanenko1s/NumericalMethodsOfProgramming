from scipy.misc import derivative

a = int(input("введіть а: "))
b = int(input("введіть b: "))
e = float(input("введіть e(точність): "))

def f(x):
    return 3*x**4-4*x**3+x**2-2*x-3 

if (f(b)*derivative(f, b, n = 2)>0):
    xi = b
else:
    xi = a

df = derivative(f,xi, n= 1)
xi_1 = xi - f(xi)/df

while (abs(xi_1 - xi) > e):
    xi = xi_1
    xi_1 = xi - f(xi)/df

print ("x = {}".format(xi_1))