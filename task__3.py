import matplotlib.pyplot as plt
import numpy as np

def circle_plotter(a=5, b = 2.5):
    x = np.arange(-10, 10, 0.1)
    y = np.arange(-10, 10, 0.1)
    X, Y = np.meshgrid(x, y)
    E = X**2 / a**2 + Y**2 / b**2 - 1
    plt.contour(X, Y, E, levels=[0])

    plt.axis('equal')
    plt.title('task3')
    plt.savefig('Task__3.png')

circle_plotter(a=5, b = 2.5)

