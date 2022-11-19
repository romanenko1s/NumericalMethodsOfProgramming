from scipy import integrate 
import numpy as np

eps = 0.001
def f1(x): 
    return 1/((1+2*x**2)**(1/2)) 

def trap(f1,a,b,n): 
    h=(b-a)/n 
    sum=0.5*(f1(a)+f1(b)) 
    for i in range(1,n): 
        sum+=f1(a+i*h)
    return sum*h

v,err = integrate.quad(f1,0.6, 1.5)

if abs (trap(f1, 0.6, 1.5, 2*20) -trap(f1, 0.6, 1.5, 20))/3. <= eps: 
    print("Метод трапеції:",round (trap(f1, 0.6, 1.5, 20), 5)) 

print("Перевірка методу трапеції= ",round(v, 5))