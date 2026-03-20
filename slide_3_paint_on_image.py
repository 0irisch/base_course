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



coords = circle(120, 205, 190, 29*np.pi/36, 11*np.pi/6, 0.1)
plt.plot(coords[0], coords[1], lw=2, color='w')
plt.savefig('slide_2_paint_image.png')

coords = circle(150, 230, 170, 4*np.pi/9, 29*np.pi/36, 0.1)
plt.plot(coords[0], coords[1], lw=2, color='w')
plt.savefig('slide_2_paint_image.png')


plt.plot([290, 310], [280, 130], lw=2, color='w')
plt.savefig('slide_2_paint_image.png')


coords = circle(140, 390, 380, 5*np.pi/4, 11*np.pi/6, 0.1)
plt.plot(coords[0], coords[1], lw=2, color='w')
plt.savefig('slide_2_paint_image.png')


coords = circle(170, 405, 410, 13*np.pi/18, 43*np.pi/36, 0.1)
plt.plot(coords[0], coords[1], lw=2, color='w')
plt.savefig('slide_2_paint_image.png')



plt.plot([510, 450], [310, 370], lw=2, color='w')
plt.savefig('slide_2_paint_image.png')

plt.plot([295, 405], [540, 470], lw=2, color='w')
plt.savefig('slide_2_paint_image.png')



# coords = circle(150, 300, 370, np.pi+np.pi/2.15, 2*np.pi-np.pi/6, 0.1)
# plt.plot(coords[0], coords[1], lw=2, color='w')
# plt.savefig('slide_2_paint_image.png')

#oords = circle(120, 320, 345, 2*np.pi-np.pi/6, 2*np.pi+np.pi/1.27, 0.1)
#plt.plot(coords[0], coords[1], lw=2, color='w')
#plt.savefig('slide_2_paint_image.png')