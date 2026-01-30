import matplotlib.pyplot as plt
import numpy as np

def giperbola_plotter(a=5, b=5, c=0.1):
    x = np.arange(-10, 10, c)
    y = np.arange(-10, 10, c)
    X, Y = np.meshgrid(x, y)
    G = X**2 / a**2 - Y**2 / b**2 - 1
    plt.contour(X, Y, G, levels=[0])

    plt.axis('equal')
    plt.title('task2')
    plt.savefig('Task__2.png')


giperbola_plotter(a=5, b=5, c=0.1)
