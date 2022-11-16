from scipy.misc import derivative

a = int(input("введіть а: "))
b = int(input("введіть b: "))
e = float(input("введіть e(точність): "))

def f(x):
    return 3*x**4-4*x**3+x**2-2*x-3 

if (derivative(f, a, n = 1)*derivative(f, a, n = 2)>0):
    a0 = a
    b0 = b
else:
    a0 = b
    b0 = a
ai = a0
bi = b0
while abs(ai-bi)>e:
    ai_1 = ai -f(ai)*(bi - ai)/(f(bi) - f(ai))
    bi_1 = bi - f(bi)/derivative(f,bi, n= 1)
    ai = ai_1
    bi = bi_1
x = (ai_1+bi_1)/2

print("x = {}".format(x))