import matplotlib.pyplot as plt
import numpy as np

def function_plotter(a=-2, b =3):
    x = np.arange(-2, 3, 0.1)
    y_vse= []
    for i in x:
        if i < a:
            y = a**2
        elif i >= a and i <= b:
            y = i**2
        else:
            y = b**2
        y_vse.append(y)
    plt.plot(x, y_vse)
    plt.axis('equal')
    plt.savefig('task_2dop.png')
    plt.close()
function_plotter(a=-10, b =10)
    
