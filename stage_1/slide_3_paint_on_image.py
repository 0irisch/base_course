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



coords = circle(50, 120, 210, 11*np.pi/18, 4*np.pi/3, 0.1)
plt.plot(coords[0], coords[1], lw=2, color='w')
plt.savefig('slide_2_paint_image.png')


coords = circle(50, 140, 150, 8*np.pi/9, 13*np.pi/9, 0.1)
plt.plot(coords[0], coords[1], lw=2, color='w')
plt.savefig('slide_2_paint_image.png')

coords = circle(25, 152, 90, 8*np.pi/9, 5*np.pi/3, 0.1)
plt.plot(coords[0], coords[1], lw=2, color='w')
plt.savefig('slide_2_paint_image.png')

coords = circle(20, 185, 75, np.pi/3, 19*np.pi/18, 0.1)
plt.plot(coords[0], coords[1], lw=2, color='w')
plt.savefig('slide_2_paint_image.png')

coords = circle(45, 190, 140, 14*np.pi/9, 2*np.pi, 0.1)
plt.plot(coords[0], coords[1], lw=2, color='w')
plt.savefig('slide_2_paint_image.png')

coords = circle(140, 220, 177, 4*np.pi/9, 29*np.pi/36, 0.1)
plt.plot(coords[0], coords[1], lw=2, color='w')
plt.savefig('slide_2_paint_image.png')

#plt.plot([290, 310], [280, 130], lw=2, color='w')
#plt.savefig('slide_2_paint_image.png')

#coords = circle(140, 390, 380, 5*np.pi/4, 11*np.pi/6, 0.1)
#plt.plot(coords[0], coords[1], lw=2, color='w')
#plt.savefig('slide_2_paint_image.png')

#coords = circle(170, 405, 410, 13*np.pi/18, 43*np.pi/36, 0.1)
#plt.plot(coords[0], coords[1], lw=2, color='w')
#plt.savefig('slide_2_paint_image.png')

#coords = circle(180, 550, 350, 7*np.pi/18, 7*np.pi/9, 0.1)
#plt.plot(coords[0], coords[1], lw=2, color='w')
#plt.savefig('slide_2_paint_image.png')

#plt.plot([510, 450], [310, 370], lw=2, color='w')
#plt.savefig('slide_2_paint_image.png')

#plt.plot([295, 410], [540, 470], lw=2, color='w')
#plt.savefig('slide_2_paint_image.png')

#coords = circle(190, 605, 270, np.pi/2, 5*np.pi/6, 0.1)
#plt.plot(coords[0], coords[1], lw=2, color='w')
#plt.savefig('slide_2_paint_image.png')

#plt.plot([610, 604], [517, 460], lw=2, color='w')
#plt.savefig('slide_2_paint_image.png')
