a = int(input("введіть а: "))
b = int(input("введіть b: "))
e = float(input("введіть e(точність): "))

def f(x):
    return 3*x**4-4*x**3+x**2-2*x-3 

while not (float(abs(b-a)) <= e):
    if f(a) * f((a+b)/2) < 0:
        b = (a+b)/2
    else:
        a = (a+b)/2
    print("a = ", a, "b = ", b, "f(a) = ", "xn = ", (a+b)/2, "f(xn) = ", f((a+b)/2), "|a-b| = ", abs(a-b))

print("x = ", (a+b)/2)