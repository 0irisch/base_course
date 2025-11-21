import numpy as np

b = [2, 3, 1, 4, 5, 6, 7 ], [8, 1, 3, 2, 2, 6, 8], [1, 4, 3, 1, 0, 2, 5], [4, 5, 0, 1, 3, 2 , 1], [8, 7, 9, 1, 0, 2, 3]
b = np.array(b)
print(b)

slice = b[0:3:1, 0:2:1]
print(slice)

slice = b[4::1, 0:1:1]
print(slice)

slice = b[3::1, 2:4:1]
print(slice)

slice = b[1:3:1, 3:5:1]
print(slice)

slice = b[0:3:1, 5]
print(slice)

slice = b[3:4:1, 5::1]
print(slice)


