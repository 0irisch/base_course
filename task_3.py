import numpy as np

a = int(input())
b = int(input())
c = int(input())

d = [0, 1, 2, 3, 4, 5]
t = np.array(d)

x = a + b * t
y = c + b * t - ((10 * t**2)/2)

print(x, y)




