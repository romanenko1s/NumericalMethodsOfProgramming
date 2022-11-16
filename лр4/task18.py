import numpy as np

a = np.matrix([[4, 1, 4], [1, 1, 2], [2, 1, 2]])
b = np.matrix([[-2], [-1], [0]])

print('A=',a)
print('B=',b)

a_det = np.linalg.det(a)

print('Детермінант матриці = ', a_det)
if (a_det != 0):

    print ('Розв*язуємо систему')
    x_m = np.matrix(a)
    x_m[:, 0] = b
    print('x_m=', x_m)
    y_m = np.matrix(a)
    y_m[:, 1] = b
    print('y_m=',y_m)

    z_m = np.matrix(a)
    z_m[:, 2] = b
    print('z_m=',z_m)

    x = np.linalg.det(x_m) / a_det
    y = np.linalg.det(y_m) / a_det
    z = np.linalg.det(z_m) / a_det

    print('X = ', round(x,5))
    print('Y=', round(y,5))
    print('Z=', round(z,5))

else:
    print('Розв*язків немає')