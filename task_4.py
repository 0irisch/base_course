import numpy as np

M = int(input("Введите М"))
N = int(input("Введите N"))

trigonometry_array = np.zeros((M , N ))

for i in range(0,M):
    for j in range(0,N):
        trigonometry_array[i, j] = np.sin(N * i + M * j + 1)
        if trigonometry_array[i, j] < 0:
            trigonometry_array[i, j] = 0


print(trigonometry_array)

