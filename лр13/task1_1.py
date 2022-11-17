import numpy as np
import matplotlib.pyplot as plt

x0 = 0.5
y0 = 1.8
x = [x0]
y = [y0]
i = 0

while i < 10:
    x.append(round(x[i] + 0.1, 4))
    y.append(round((y[i] + 0.1*(x[i] + np.sin(y[i]/1.25))), 4))
    i+=1

print(x)
print(y)

plt.plot(x, y)
plt.grid()
plt.show()