import random

N = int(input("ВВедіть N рядків: "))
M = int(input("ВВедіть M стовпців: "))

matrix = []

for i in range(N):
    row = []
    for j in range(M):
        num = random.randint(0, 99)
        row.append(num)
    matrix.append(row)

for row in matrix:
    print(row)

sumMain = 0
sumSecondary = 0

for i in range(N):
    sumMain += matrix[i][i]
    sumSecondary += matrix[i][N-i-1]

print(sumMain)
print(sumSecondary)