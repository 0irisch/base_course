import matplotlib.pyplot as plt
import numpy as np

k = 0.1

phi = np.arange(0, 8*np.pi, 0.1)
r = np.e ** (k * phi)
x = r * np.cos(phi)
y = r * np.sin(phi)

plt.plot(x, y)
plt.axis('equal')
plt.savefig('task__4_1.png')
plt.close()


k = 0.1
phi = np.arange(0, 8*np.pi, 0.1)
r = k * phi
x = r * np.cos(phi)
y = r * np.sin(phi)

plt.plot(x, y)
plt.axis('equal')
plt.savefig('task__4_2.png')
plt.close()

k = 4
phi = np.arange(0, 8*np.pi, 0.1)
r = np.sin(k * phi)
x = r * np.cos(phi)
y = r * np.sin(phi)

plt.plot(x, y)
plt.axis('equal')
plt.savefig('task__4_3.png')
plt.close()

k = 0.1
phi = np.arange(0.01, 8*np.pi, 0.1)
r = k / (phi ** 0.5)
x = r * np.cos(phi)
y = r * np.sin(phi)

plt.plot(x, y)
plt.axis('equal')
plt.savefig('task__4_4.png')
plt.close()