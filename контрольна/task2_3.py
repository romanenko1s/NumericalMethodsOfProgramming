
import numpy as np
import matplotlib.pyplot as plt

alpha = 0.5
beta = 0.3
N = 1000000
S0 = 990000
I0 = 7000
R0 = 3000

t0 = 0
tf = 25
t = np.linspace(t0, tf, 25)

S = [S0]
I = [I0]
R = [R0]

for i in range(1, 25):
    S.append(S[-1] - alpha * S[-1])
    I.append(I[-1] + alpha * S[-1] - beta * I[-1])
    R.append(R[-1] + beta * I[-1])

plt.plot(t, R, 'g', marker = 's')
plt.xlabel('Час (діб)')
plt.ylabel('Одужавше населення')
plt.grid()
plt.show()