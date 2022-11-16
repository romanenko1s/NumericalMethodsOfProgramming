import numpy as np

a = np.matrix([[1, 2],[4, -1]])
b = np.matrix([[2, -3],[-4, 1]])

ab = a * b
ba = b * a
c = ab - ba

print(c)