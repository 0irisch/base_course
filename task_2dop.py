import matplotlib.pyplot as plt
import numpy as np


def function_plotter(a=-2, b=3):
    x0 =  np.arange(a-10, a, 0.01)
    x1 = np.arange(a, b, 0.01)
    x2 = np.arange(b, b+10, 0.01)

    y0 = np.ones(len(x0)) * a**2
    y1 = x1**2
    y2 = np.ones(len(x2)) * b**2

    plt.plot(x0, y0)
    plt.plot(x1, y1)
    plt.plot(x2, y2)

    plt.axis('equal')
    plt.savefig('task_2dop.png')
    plt.close()


function_plotter(a=0, b =2)
    
