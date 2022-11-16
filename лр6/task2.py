from turtle import color
import numpy as np
import matplotlib.pyplot as plt

x = np.array([-3.,-1.,0.5,2.5], dtype=float)
y = np.array([-16.5,-4.5,-2.6,6.7], dtype=float)
def lagranz(x,y,t):
    z = 0
    for j in range(len(y)):
        p1 = 1; p2 = 1
        for i in range(len(x)):
            if i==j:
                p1 = p1*1
                p2 = p2*1
            else:
                p1 = p1*(t-x[i])
                p2 = p2*(x[j]-x[i])
        z = z + y[j] * p1/p2
    return z

xnew = np.linspace(np.min(x), np.max(x), 100)
ynew = [lagranz(x, y, i) for i in xnew]
plt.plot(x, y, 'o', xnew, ynew, color = "blue")
plt.grid(which='major', color='#CCCCCC', linestyle='--')
plt.show()  