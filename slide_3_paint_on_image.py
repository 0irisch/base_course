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



#plt.plot([250, 100], [320, 290], lw=2, color='w')
#plt.savefig('slide_2_paint_image.png')

#plt.plot([250, 280], [320, 520], lw=2, color='w')
#plt.savefig('slide_2_paint_image.png')

coords = circle(120, 205, 190, 29*np.pi/36, 11*np.pi/6, 0.1)
plt.plot(coords[0], coords[1], lw=2, color='w')
plt.savefig('slide_2_paint_image.png')

coords = circle(150, 200, 160, np.pi/3, 29*np.pi/36, 0.1)
plt.plot(coords[0], coords[1], lw=2, color='w')
plt.savefig('slide_2_paint_image.png')


#plt.plot([300, 310], [280, 100], lw=2, color='w')
#plt.savefig('slide_2_paint_image.png')

#plt.plot([300, 500], [280, 250], lw=2, color='w')
#plt.savefig('slide_2_paint_image.png')

#plt.plot([500, 470], [250, 370], lw=2, color='w')
#plt.savefig('slide_2_paint_image.png')

#plt.plot([280, 470], [520, 460], lw=2, color='w')
#plt.savefig('slide_2_paint_image.png')



# coords = circle(150, 300, 370, np.pi+np.pi/2.15, 2*np.pi-np.pi/6, 0.1)
# plt.plot(coords[0], coords[1], lw=2, color='w')
# plt.savefig('slide_2_paint_image.png')

#oords = circle(120, 320, 345, 2*np.pi-np.pi/6, 2*np.pi+np.pi/1.27, 0.1)
#plt.plot(coords[0], coords[1], lw=2, color='w')
#plt.savefig('slide_2_paint_image.png')