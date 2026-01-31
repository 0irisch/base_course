import matplotlib.pyplot as plt
import numpy as np


def lissage_plotter(a, A, q, b, B):
    t = np.arange(1, 18, 0.01)
    x = A * np.cos(a * t + q)
    y = B * np.sin(b * t)
    plt.plot(x, y)
    plt.savefig('task__1dop_lissage.png')


a = 1
A = 1
q = np.pi / 2
B = 0.3
b = 0.25

lissage_plotter(a, A, q, b, B)