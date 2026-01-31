import matplotlib.pyplot as plt
import numpy as np

def sinusoida_plotter(fr=-10, to=10, n=0.01):
    x = np.arange(-10, 10, 0.1)
    y = np.sin(x)
    plt.plot(x, y)
    plt.axis('equal')
    plt.savefig('task__2_2_sinusoida.png')
    plt.close()
sinusoida_plotter(fr=-10, to=10, n=0.01)

def log_criv(fr=-10, to=10, n=0.01):
    x = np.arange(-10, 10, 0.1)
    y = np.log2(x)
    plt.plot(x, y)
    plt.axis('equal')
    plt.savefig('task__2_2_log_criv.png')
    plt.close()
log_criv(fr=-10, to=10, n=0.01)

def giper_sinusoida(fr=-5, to=5, n=0.1):
    x = np.arange(-5, 5, 0.1)
    y = (np.e**x + np.e**-x)/2
    plt.plot(x, y)
    plt.axis('equal')
    plt.savefig('task__2_2_giper_sinusoida.png')
    plt.close()
giper_sinusoida(fr=-10, to=10, n=0.01)