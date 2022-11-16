import numpy as np

a = np.matrix([[1, 2, 3, 4], [-2, 1, -4, 3], [3, -4, -1, 2], [4, 3, -2, -1]])

print("Визначник: {}".format(np.linalg.det(a)))