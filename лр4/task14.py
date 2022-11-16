import numpy as np

a = np.matrix([[2, 3, 4], [1, 0, 6], [7, 8, 9]])

print("Визначник: {}".format(np.linalg.det(a)))