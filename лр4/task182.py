import numpy as np

a = np.matrix([[4, 1, 4], [1, 1, 2], [2, 1, 2]])
b = np.matrix([[-2], [-1], [0]])

x = np.linalg.solve(a, b)

print(x)