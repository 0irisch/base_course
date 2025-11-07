import numpy as np
c = np.zeros((.))
a = [2, 3, 1, 4, 5, 6, 7]
b = np.array([a, np.array(a)**1])
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


