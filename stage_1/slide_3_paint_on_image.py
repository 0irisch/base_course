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

#правое крыло


coords = circle(160, 550, 385, 13*np.pi/18, 8*np.pi/9, 0.1)
plt.plot(coords[0], coords[1], lw=0.5, color='w')
plt.savefig('slide_2_paint_image.png')









plt.plot([480, 490], [490, 505], lw=0.5, color='w')
plt.savefig('slide_2_paint_image.png')

coords = circle(30, 510, 478, 5*np.pi/12, 7*np.pi/9, 0.1)
plt.plot(coords[0], coords[1], lw=0.5, color='w')
plt.savefig('slide_2_paint_image.png')

plt.plot([555, 520], [530, 505], lw=0.5, color='w')
plt.savefig('slide_2_paint_image.png')

# coords = circle(30, 565, 500, 0, 2*np.pi/3, 0.1)
# plt.plot(coords[0], coords[1], lw=0.5, color='w')
# plt.savefig('slide_2_paint_image.png')

# coords = circle(60, 555, 460, np.pi/12, 5*np.pi/18, 0.1)
# plt.plot(coords[0], coords[1], lw=0.5, color='w')
# plt.savefig('slide_2_paint_image.png')

# plt.plot([605, 610], [460, 475], lw=0.5, color='w')
# plt.savefig('slide_2_paint_image.png')

# coords = circle(30, 575, 460, 0, 7*np.pi/18, 0.1)
# plt.plot(coords[0], coords[1], lw=0.5, color='w')
# plt.savefig('slide_2_paint_image.png')

# plt.plot([575, 590], [478, 488], lw=0.5, color='w')
# plt.savefig('slide_2_paint_image.png')

# plt.plot([567, 575], [495, 478], lw=0.5, color='w')
# plt.savefig('slide_2_paint_image.png')

# plt.plot([555, 567], [473, 495], lw=0.5, color='w')
# plt.savefig('slide_2_paint_image.png')

# plt.plot([536, 555], [475, 473], lw=0.5, color='w')
# plt.savefig('slide_2_paint_image.png')

# plt.plot([531, 536], [490, 475], lw=0.5, color='w')
# plt.savefig('slide_2_paint_image.png')

# coords = circle(80, 558, 417, 11*np.pi/18, 31*np.pi/36, 0.1)
# plt.plot(coords[0], coords[1], lw=0.5, color='w')
# plt.savefig('slide_2_paint_image.png')

# plt.plot([505, 490], [448, 455], lw=0.5, color='w')
# plt.savefig('slide_2_paint_image.png')

# plt.plot([500, 505], [420, 448], lw=0.5, color='w')
# plt.savefig('slide_2_paint_image.png')

# coords = circle(60, 517, 363, 7*np.pi/12, 8*np.pi/9, 0.1)
# plt.plot(coords[0], coords[1], lw=0.5, color='w')
# plt.savefig('slide_2_paint_image.png')

# coords = circle(20, 455, 370, np.pi/3, 7*np.pi/6, 0.1)
# plt.plot(coords[0], coords[1], lw=0.5, color='w')
# plt.savefig('slide_2_paint_image.png')

# plt.plot([398, 440], [320, 360], lw=0.5, color='w')
# plt.savefig('slide_2_paint_image.png')

# coords = circle(100, 380, 420, 14*np.pi/9, 11*np.pi/6, 0.1)
# plt.plot(coords[0], coords[1], lw=0.5, color='w')
# plt.savefig('slide_2_paint_image.png')

# plt.plot([459, 469], [362, 353], lw=0.5, color='w')
# plt.savefig('slide_2_paint_image.png')

# coords = circle(60, 435, 405, 5*np.pi/3, 16*np.pi/9, 0.1)
# plt.plot(coords[0], coords[1], lw=0.5, color='w')
# plt.savefig('slide_2_paint_image.png')

# plt.plot([475, 483], [345, 370], lw=0.5, color='w')
# plt.savefig('slide_2_paint_image.png')

# coords = circle(60, 532, 359, 13*np.pi/12, 13*np.pi/9, 0.1)
# plt.plot(coords[0], coords[1], lw=1, color='w')
# plt.savefig('slide_2_paint_image.png')

# coords = circle(60, 540, 246, np.pi/2, 3*np.pi/4, 0.1)
# plt.plot(coords[0], coords[1], lw=1, color='w')
# plt.savefig('slide_2_paint_image.png')

# coords = circle(150, 395, 400, 23*np.pi/18, 16*np.pi/9, 0.1)
# plt.plot(coords[0], coords[1], lw=1, color='w')
# plt.savefig('slide_2_paint_image.png')




# coords = circle(150, 420, 370, 43*np.pi/36, 25*np.pi/18, 0.1) #нижняя верхняя часть
# plt.plot(coords[0], coords[1], lw=1, color='w')
# plt.savefig('slide_2_paint_image.png')

# coords = circle(80, 350, 314, 7*np.pi/6, 55*np.pi/36, 0.1) #нижняя нижняя часть
# plt.plot(coords[0], coords[1], lw=1, color='w')
# plt.savefig('slide_2_paint_image.png')

# coords = circle(150, 167, 185, 11*np.pi/36, 19*np.pi/36, 0.1) #верхняя нижняя часть
# plt.plot(coords[0], coords[1], lw=1, color='w')
# plt.savefig('slide_2_paint_image.png')

# coords = circle(80, 210, 260, 11*np.pi/36, 23*np.pi/36, 0.1) #верхняя верхняя часть
# plt.plot(coords[0], coords[1], lw=1, color='w')
# plt.savefig('slide_2_paint_image.png')

# # #левое крыло
# coords = circle(300, 15, 130, 0, np.pi/6, 0.1)
# plt.plot(coords[0], coords[1], lw=2, color='w')
# plt.savefig('slide_2_paint_image.png')

# coords = circle(120, 205, 88, 0, 5*np.pi/36, 0.1)
# plt.plot(coords[0], coords[1], lw=2, color='w')
# plt.savefig('slide_2_paint_image.png')

# coords = circle(100, 225, 65, np.pi/18, 7*np.pi/36, 0.1)
# plt.plot(coords[0], coords[1], lw=2, color='w')
# plt.savefig('slide_2_paint_image.png')

# plt.plot([300, 310], [100, 120], lw=1.5, color='w')
# plt.savefig('slide_2_paint_image.png')

# plt.plot([295, 300], [120, 100], lw=1.5, color='w')
# plt.savefig('slide_2_paint_image.png')

# plt.plot([282, 295], [114, 120], lw=1, color='w')
# plt.savefig('slide_2_paint_image.png')

# coords = circle(120, 165, 116, 0, 7*np.pi/36, 0.1)
# plt.plot(coords[0], coords[1], lw=1, color='w')
# plt.savefig('slide_2_paint_image.png')

# coords = circle(90, 178, 190, 5*np.pi/3, 2*np.pi, 0.1)
# plt.plot(coords[0], coords[1], lw=0.5, color='w')
# plt.savefig('slide_2_paint_image.png')

# coords = circle(90, 158, 175, 31*np.pi/18, 2*np.pi, 0.1)
# plt.plot(coords[0], coords[1], lw=0.5, color='w')
# plt.savefig('slide_2_paint_image.png')

# coords = circle(100, 310, 90, 13*np.pi/18, 35*np.pi/36, 0.1)
# plt.plot(coords[0], coords[1], lw=0.5, color='w')
# plt.savefig('slide_2_paint_image.png')

# plt.plot([195, 210], [80, 107], lw=0.5, color='w')
# plt.savefig('slide_2_paint_image.png')

# plt.plot([200, 195], [115, 80], lw=0.5, color='w')
# plt.savefig('slide_2_paint_image.png')

# plt.plot([175, 200], [80, 115], lw=0.5, color='w')
# plt.savefig('slide_2_paint_image.png')

# plt.plot([180, 175], [110, 80], lw=0.5, color='w')
# plt.savefig('slide_2_paint_image.png')

# coords = circle(10, 144, 70, 11*np.pi/18, 2*np.pi, 0.1)
# plt.plot(coords[0], coords[1], lw=0.5, color='w')
# plt.savefig('slide_2_paint_image.png')

# coords = circle(50, 205, 67, 2*np.pi/3, 37*np.pi/36, 0.1)
# plt.plot(coords[0], coords[1], lw=0.5, color='w')
# plt.savefig('slide_2_paint_image.png')

# coords = circle(60, 200, 80, 13*np.pi/18, 37*np.pi/36, 0.1)
# plt.plot(coords[0], coords[1], lw=0.5, color='w')
# plt.savefig('slide_2_paint_image.png')

# plt.plot([110, 160], [80, 125], lw=0.5, color='w')
# plt.savefig('slide_2_paint_image.png')

# plt.plot([115, 110], [115, 80], lw=0.5, color='w')
# plt.savefig('slide_2_paint_image.png')

# coords = circle(50, 85, 157, 17*np.pi/12, 31*np.pi/18, 0.1)
# plt.plot(coords[0], coords[1], lw=0.5, color='w')
# plt.savefig('slide_2_paint_image.png')

# coords = circle(60, 50, 163, 14*np.pi/9, 71*np.pi/36, 0.1)
# plt.plot(coords[0], coords[1], lw=0.5, color='w')
# plt.savefig('slide_2_paint_image.png')

# plt.plot([90, 110], [152, 155], lw=0.5, color='w')
# plt.savefig('slide_2_paint_image.png')

# coords = circle(30, 80, 180, 59*np.pi/36, 71*np.pi/36, 0.1)
# plt.plot(coords[0], coords[1], lw=0.5, color='w')
# plt.savefig('slide_2_paint_image.png')

# coords = circle(60, 80, 120, np.pi/3, 5*np.pi/9, 0.1)
# plt.plot(coords[0], coords[1], lw=0.5, color='w')
# plt.savefig('slide_2_paint_image.png')

# plt.plot([105, 65], [195, 175], lw=0.5, color='w')
# plt.savefig('slide_2_paint_image.png')

# plt.plot([43, 105], [180, 195], lw=1, color='w')
# plt.savefig('slide_2_paint_image.png')

# coords = circle(60, 20, 235, 59*np.pi/36, 71*np.pi/36, 0.1)
# plt.plot(coords[0], coords[1], lw=1.5, color='w')
# plt.savefig('slide_2_paint_image.png')

# coords = circle(20, 75, 205, 4*np.pi/9, 7*np.pi/9, 0.1)
# plt.plot(coords[0], coords[1], lw=1.5, color='w')
# plt.savefig('slide_2_paint_image.png')

# coords = circle(150, 190, 143, 11*np.pi/18, 31*np.pi/36, 0.1)
# plt.plot(coords[0], coords[1], lw=2, color='w')
# plt.savefig('slide_2_paint_image.png')

# plt.plot([110, 130], [275, 280], lw=2, color='w')
# plt.savefig('slide_2_paint_image.png')

# coords = circle(150, 210, 165, 5*np.pi/12, 3*np.pi/4, 0.1)
# plt.plot(coords[0], coords[1], lw=2, color='w')
# plt.savefig('slide_2_paint_image.png')



