import matplotlib.pyplot as plt
import numpy as np

def y(x):
    return (11/15)*x**3 + 2*x**2 - 7*x + (4/15)

x1 = np.arange(-5, 4, 0.1)
y1 = [y(i) for i in x1]
plt.plot(x1, y1, 'b')
plt.grid(which='major', color='#CCCCCC', linestyle='--')
plt.draw()
plt.show()