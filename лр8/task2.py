import numpy as np
from math import factorial
import matplotlib.pyplot as plt

x=[1.415,1.42,1.425,1.43,1.435,1.44,1.445,1.45,1.455,1.46,1.465]
y=[0.8885,0.8895,0.8906,0.8916,0.8926,0.8936,0.8947,0.8956,0.8966,0.8976,0.8986]

x1 = 1.422
x2 = 1.451

h = x[1] - x[0]
q=(x1 - x[0])/h
q1 = (x2-x[-1])/h
def n(y,j):
    mas=[]
    for i in range(len(y)):
        mas.append(y[i] - y[i-1])
    mas.pop(0)  
    if j == 1:
        return mas
    else:
        j-=1
        return n(mas, j)

s_1 = y[0]+q*n(y,1)[0]+q*(q-1)*n(y,2)[0]/factorial(2)
s_2 = q*(q-1)*(q-2)*n(y,3)[0]/factorial(3)
s_3 = q*(q-1)*(q-2)*(q-3)*n(y,4)[0]/factorial(4)
s_4 = q*(q-1)*(q-2)*(q-3)*(q-4)*n(y,5)[0]/factorial(5)
n_1 = s_1 + s_2 + s_3 + s_4

d_1 = y[0]+q1*n(y,1)[0]+q1*(q1-1)*n(y,2)[0]/factorial(2)
d_2 = q1*(q1-1)*(q1-2)*n(y,3)[0]/factorial(3)
d_3 = q1*(q1-1)*(q1-2)*(q1-3)*n(y,4)[0]/factorial(4)
d_4 = q1*(q1-1)*(q1-2)*(q1-3)*(q1-4)*n(y,5)[0]/factorial(5)
n_2 = d_1 + d_2 + d_3 + d_4

print ("значення функції в точці x1 = ", x1, " дорівнює ", round(n_1,5))
print ("значення функції в точці x2 = ", x2, " дорівнює ", round(n_2,5))

x_1 = np.linspace(np.min(x), np.max(x))
y_1 = np.linspace(np.min(y), np.max(y))

plt.plot(x,y, 'ro', x_1, y_1)
plt.plot(x1, n_1, 'bo')
plt.plot(x2, n_2, 'bo')
plt.title('Graph of the interpolation function')
plt.xlabel('x')
plt.ylabel('y')
plt.grid()
plt.show()