import matplotlib.pyplot as plt
import numpy as np

def y(x):
    return - 1 + np.sin(x + 1)
def x(y):
    return 1 - np.cos(y)

x1 = np.arange(-2, 2, 0.1)
y1 = [y(i) for i in x1]

y2 = np.arange(-2, 2, 0.1)
x2 = [x(i) for i in y2]

plt.plot(x1, y1, 'b', x2, y2, 'r')
plt.grid(which='major', color='#CCCCCC', linestyle='--')
plt.draw()
plt.show()