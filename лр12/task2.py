from scipy import integrate 
import numpy as np

eps = 0.001
def f1(x): 
    return np.sin((x**2) - 1)/(2*(x**(1/2)))

def simpson(a,b,n): 
    h = (b - a) / n 
    integr = f1(a) + f1(b) 
    for i in range(1,n): 
        k = a + i*h 
        if i%2 == 0: 
            integr += 2 * f1(k) 
        else: 
            integr += 4 * f1(k) 
    integr *= h/3 
    return integr 

if abs(simpson(1.3,2.1,2*8) -simpson(1.3,2.1,8))/ 15. <= eps: 
   print("Метод Сімпсона:",round (simpson(1.3,2.1,8), 5)) 

v,err = integrate.quad(f1,1.3,2.1)
print("Перевірка метода Сімпсона= ",round(v, 5)) 