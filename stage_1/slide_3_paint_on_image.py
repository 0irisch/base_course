import matplotlib.pyplot as plt
import numpy as np

img = plt.imread("Butterfly_Nebula.jpg")
fig, ax = plt.subplots()
ax.imshow(img, extent=[0, 640, 0, 640])


def circle(R, x0, y0, starst, stop, step):
    t=np.arange(starst, stop, step)
    x = x0 + R * np.cos(t)
    y = y0 + R * np.sin(t)
    return x, y

coords = circle(90, 158, 175, 16*np.pi/9, 2*np.pi, 0.1)
plt.plot(coords[0], coords[1], lw=0.5, color='w')
plt.savefig('slide_2_paint_image.png')






coords = circle(100, 310, 90, 13*np.pi/18, 35*np.pi/36, 0.1)
plt.plot(coords[0], coords[1], lw=0.5, color='w')
plt.savefig('slide_2_paint_image.png')

plt.plot([195, 210], [80, 107], lw=0.5, color='w')
plt.savefig('slide_2_paint_image.png')

plt.plot([200, 195], [115, 80], lw=0.5, color='w')
plt.savefig('slide_2_paint_image.png')

plt.plot([175, 200], [80, 115], lw=0.5, color='w')
plt.savefig('slide_2_paint_image.png')

plt.plot([180, 175], [110, 80], lw=0.5, color='w')
plt.savefig('slide_2_paint_image.png')

coords = circle(10, 144, 70, 11*np.pi/18, 2*np.pi, 0.1)
plt.plot(coords[0], coords[1], lw=0.5, color='w')
plt.savefig('slide_2_paint_image.png')

coords = circle(50, 205, 67, 2*np.pi/3, 37*np.pi/36, 0.1)
plt.plot(coords[0], coords[1], lw=0.5, color='w')
plt.savefig('slide_2_paint_image.png')

coords = circle(60, 200, 80, 13*np.pi/18, 37*np.pi/36, 0.1)
plt.plot(coords[0], coords[1], lw=0.5, color='w')
plt.savefig('slide_2_paint_image.png')

plt.plot([110, 160], [80, 125], lw=0.5, color='w')
plt.savefig('slide_2_paint_image.png')

plt.plot([115, 110], [115, 80], lw=0.5, color='w')
plt.savefig('slide_2_paint_image.png')

coords = circle(50, 85, 157, 17*np.pi/12, 31*np.pi/18, 0.1)
plt.plot(coords[0], coords[1], lw=0.5, color='w')
plt.savefig('slide_2_paint_image.png')

coords = circle(60, 50, 163, 14*np.pi/9, 71*np.pi/36, 0.1)
plt.plot(coords[0], coords[1], lw=0.5, color='w')
plt.savefig('slide_2_paint_image.png')

plt.plot([90, 110], [152, 155], lw=0.5, color='w')
plt.savefig('slide_2_paint_image.png')

coords = circle(30, 80, 180, 59*np.pi/36, 71*np.pi/36, 0.1)
plt.plot(coords[0], coords[1], lw=0.5, color='w')
plt.savefig('slide_2_paint_image.png')

coords = circle(60, 80, 120, np.pi/3, 5*np.pi/9, 0.1)
plt.plot(coords[0], coords[1], lw=0.5, color='w')
plt.savefig('slide_2_paint_image.png')

plt.plot([105, 65], [195, 175], lw=0.5, color='w')
plt.savefig('slide_2_paint_image.png')

plt.plot([43, 105], [180, 195], lw=0.5, color='w')
plt.savefig('slide_2_paint_image.png')

coords = circle(60, 20, 235, 59*np.pi/36, 71*np.pi/36, 0.1)
plt.plot(coords[0], coords[1], lw=0.5, color='w')
plt.savefig('slide_2_paint_image.png')

coords = circle(20, 75, 205, 4*np.pi/9, 7*np.pi/9, 0.1)
plt.plot(coords[0], coords[1], lw=0.5, color='w')
plt.savefig('slide_2_paint_image.png')

coords = circle(150, 190, 143, 11*np.pi/18, 31*np.pi/36, 0.1)
plt.plot(coords[0], coords[1], lw=1, color='w')
plt.savefig('slide_2_paint_image.png')

plt.plot([110, 130], [275, 280], lw=0.5, color='w')
plt.savefig('slide_2_paint_image.png')

coords = circle(150, 210, 165, 5*np.pi/12, 3*np.pi/4, 0.1)
plt.plot(coords[0], coords[1], lw=1, color='w')
plt.savefig('slide_2_paint_image.png')



