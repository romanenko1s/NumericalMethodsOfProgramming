
import numpy as np
import matplotlib.pyplot as plt

alpha = 0.5
beta = 0.3
N = 1000000
S0 = 990000

t0 = 0
tf = 25
t = np.linspace(t0, tf, 25)

S = [S0]

for i in range(1, 25):
    S.append(S[-1] - alpha * S[-1])

plt.plot(t, S, 'b', marker = '^')
plt.xlabel('Час (діб)')
plt.ylabel('Вразливе населення')
plt.grid()
plt.show()