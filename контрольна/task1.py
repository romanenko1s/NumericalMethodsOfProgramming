import numpy as np
import matplotlib.pyplot as plt
from scipy import interpolate as interp

speed = [25, 35, 45, 30, 60, 120, 100, 100, 70, 75, 80, 65]
time = np.linspace(0, 11, 12)

"""for t in time:
    print(t)"""

"""plt.plot(time, speed, scalex=(0,11), scaley=(0,130))
plt.grid()
plt.xlabel('time')
plt.ylabel('speed')
plt.show()"""

f = interp.interp1d(time, speed, kind='cubic')
time_new = np.linspace(0, 11, 10000)
speed_new = f(time_new)

plt.plot(time_new, speed_new)
plt.plot(time, speed, 'o')
plt.xlabel('Час (год)')
plt.ylabel('Швидкість (км/год)')
plt.xticks(time)
plt.yticks(np.arange(0, 140, 10))
plt.grid()
plt.show()

distance = np.trapz(speed_new, time_new)
print(f'Шлях: {distance:.3f} км')