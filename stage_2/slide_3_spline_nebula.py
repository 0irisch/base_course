import numpy as np
from scipy import interpolate
import matplotlib.pyplot as plt

img = plt.imread("Butterfly_Nebula.jpg")
fig, ax = plt.subplots()
ax.imshow(img, extent=[0, 640, 0, 640])

