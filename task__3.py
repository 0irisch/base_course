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
    plt.savefig('Task__3_elipse.png')
    plt.close()

circle_plotter(a=5, b = 2.5)

def cassini_plotter(a=5, c=3):
    x = np.arange(-10, 10, 0.1)
    y = np.arange(-10, 10, 0.1)
    X, Y = np.meshgrid(x, y)
    C = (a**4 - c**4) - ((X**2 + Y**2)**2 - 2*c**2*(X**2 - Y**2))
    plt.contour(X, Y, C, levels=[0])

    plt.axis('equal')
    plt.title('task3')
    plt.savefig('Task__3_cassini.png')
    plt.close()
cassini_plotter(a=5, c=3)