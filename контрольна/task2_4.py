
import numpy as np
import matplotlib.pyplot as plt
from scipy import interpolate as interp

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

f_S = interp.interp1d(t, S, kind='cubic')
f_I = interp.interp1d(t, I, kind='cubic')
f_R = interp.interp1d(t, R, kind='cubic')

t_new = np.linspace(t0, tf, 100000)
S_new = f_S(t_new)
I_new = f_I(t_new)
R_new = f_R(t_new)


plt.plot(t_new, S_new, 'b', label = 'Вразливі')
plt.plot(t_new, I_new, 'r', label = 'Інфіковані')
plt.plot(t_new, R_new, 'g', label = 'Одужавші')
plt.xlabel('Час (діб)')
plt.ylabel('Населення')
plt.yticks(np.arange(0, 1100000, 100000))
plt.grid()
plt.legend()
plt.show()
