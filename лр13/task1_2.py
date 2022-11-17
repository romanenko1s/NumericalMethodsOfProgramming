
import numpy as np
import matplotlib.pyplot as plt

x0 = 1.2
y0 = 1.8
x = [x0]
y = [y0]
i = 0

while i < 10:
    x.append(round(x[i] + 0.1, 4))
    y.append(round((y[i] + 0.1*(x[i] + np.cos(y[i]/(1/3)**1/2))), 4))
    i+=1

print(x)
print(y)

plt.plot(x, y)
plt.grid()
plt.show()