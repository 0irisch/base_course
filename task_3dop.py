import matplotlib.pyplot as plt
import numpy as np

def lesenka_plotter(N=5):
    x = np.arange(N, N+1, 0.1)
    y = x
    plt.plot(x, y)
    plt.axis('equal')
    plt.savefig('task_3dop.png')
lesenka_plotter(N=5)

