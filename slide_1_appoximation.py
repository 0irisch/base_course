import matplotlib.pyplot as plt
import numpy as np

fig, ax = plt.subplots()

xw = [0, 10, 10, 0, 0]
yw = [0, 0, 8, 8, 0]
ax.plot(xw, yw, '-', linewidth=2, color='k')


xr = [0, 5, 10, 0]
yr = [8, 11, 8, 8]
ax.plot(xr, yr, '-', linewidth=2, color='k')

xd = [4, 4, 6, 6, 4]
yd = [0, 5, 5, 0, 0]
ax.plot(xd, yd, '-', linewidth=2, color='k')

t = np.linspace(0, 2*np.pi, 20)
xwi1 = 2 + 1 * np.cos(t)
ywi1 = 4 + 1 * np.sin(t)
ax.plot(xwi1, ywi1, '-', linewidth=2, color='k')

t = np.linspace(0, 2*np.pi, 20)
xwi1 = 8 + 1 * np.cos(t)
ywi1 = 4 + 1 * np.sin(t)
ax.plot(xwi1, ywi1, '-', linewidth=2, color='k')


plt.axis('equal')
plt.savefig('slide_1_appoximation_paint.png')