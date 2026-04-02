import numpy as np
from scipy import interpolate
import matplotlib.pyplot as plt
from scipy.interpolate import splprep, splev


img = plt.imread("Butterfly_Nebula.jpg")
fig, ax = plt.subplots()
ax.imshow(img, extent=[0, 640, 0, 640])

def circle(R, x0, y0, starst, stop, step):
    t=np.arange(starst, stop, step)
    x = x0 + R * np.cos(t)
    y = y0 + R * np.sin(t)
    return x, y

x = np.array([])
y = np.array([])

coords = circle(150, 167, 185, 11*np.pi/36, 19*np.pi/36, 0.1) #верхняя нижняя часть
x = np.append(x, coords[0])
y = np.append(y, coords[1])

coords = circle(80, 210, 260,11*np.pi/36, 23*np.pi/36, 0.1) #верхняя верхняя часть
x = np.append(x, coords[0])
y = np.append(y, coords[1])

#правое крыло

coords = circle(150, 380, 400, 5*np.pi/6, 7*np.pi/6, 0.1)
x = np.append(x, coords[0])
y = np.append(y, coords[1])

x = np.append(x, [248, 259])
y = np.append(y,  [475, 455])

coords = circle(150, 410, 470, 29*np.pi/36, 19*np.pi/18, 0.1)
x = np.append(x, coords[0])
y = np.append(y, coords[1])

coords = circle(40, 325, 550, 8*np.pi/9, 47*np.pi/36, 0.1)
x = np.append(x, coords[0])
y = np.append(y, coords[1])

x = np.append(x, [304, 320])
y = np.append(y,  [515, 530])

x = np.append(x, [319, 335])
y = np.append(y,  [530, 510])

coords = circle(60, 390, 490, 8*np.pi/9, 7*np.pi/6, 0.1)
x = np.append(x, coords[0])
y = np.append(y, coords[1])

coords = circle(60, 390, 440, np.pi/2, 8*np.pi/9, 0.1)
x = np.append(x, coords[0])
y = np.append(y, coords[1])

x = np.append(x, [395, 385])
y = np.append(y,  [460, 500])

x = np.append(x, [390, 394])
y = np.append(y,  [428, 460])

x = np.append(x, [423, 390])
y = np.append(y,  [468, 427])

coords = circle(80, 490, 425, np.pi/2, 5*np.pi/6, 0.1)
x = np.append(x, coords[0])
y = np.append(y, coords[1])

x = np.append(x, [480, 490])
y = np.append(y,  [490, 505])

coords = circle(30, 510, 478, 5*np.pi/12, 7*np.pi/9, 0.1)
x = np.append(x, coords[0])
y = np.append(y, coords[1])

x = np.append(x, [555, 520])
y = np.append(y,  [530, 505])

coords = circle(30, 565, 500, 0, 2*np.pi/3, 0.1)
x = np.append(x, coords[0])
y = np.append(y, coords[1])

coords = circle(60, 555, 460, np.pi/12, 5*np.pi/18, 0.1)
x = np.append(x, coords[0])
y = np.append(y, coords[1])

x = np.append(x, [605, 610])
y = np.append(y,  [460, 475])

coords = circle(30, 575, 460, 0, 7*np.pi/18, 0.1)
x = np.append(x, coords[0])
y = np.append(y, coords[1])

x = np.append(x, [536, 555])
y = np.append(y,  [475, 472])

coords = circle(80, 558, 417, 11*np.pi/18, 31*np.pi/36, 0.1)
x = np.append(x, coords[0])
y = np.append(y, coords[1])

x = np.append(x, [505, 490])
y = np.append(y,  [448, 455])

x = np.append(x, [500, 505])
y = np.append(y,  [420, 449])

coords = circle(60, 517, 363, 7*np.pi/12, 8*np.pi/9, 0.1)
x = np.append(x, coords[0])
y = np.append(y, coords[1])

coords = circle(20, 455, 370, np.pi/3, 7*np.pi/6, 0.1)
x = np.append(x, coords[0])
y = np.append(y, coords[1])

x = np.append(x, [398, 440])
y = np.append(y,  [320, 360])

coords = circle(100, 380, 420, 14*np.pi/9, 11*np.pi/6, 0.1)
x = np.append(x, coords[0])
y = np.append(y, coords[1])

x = np.append(x, [459, 469])
y = np.append(y,  [362, 353])

coords = circle(60, 435, 405, 5*np.pi/3, 16*np.pi/9, 0.1)
x = np.append(x, coords[0])
y = np.append(y, coords[1])

x = np.append(x, [475, 483])
y = np.append(y,  [345, 370])

coords = circle(60, 532, 359, 13*np.pi/12, 13*np.pi/9, 0.1)
x = np.append(x, coords[0])
y = np.append(y, coords[1])

coords = circle(60, 540, 246, np.pi/2, 3*np.pi/4, 0.1)
x = np.append(x, coords[0])
y = np.append(y, coords[1])

coords = circle(150, 395, 400, 23*np.pi/18, 16*np.pi/9, 0.1)
x = np.append(x, coords[0])
y = np.append(y, coords[1])

coords = circle(150, 420, 370, 43*np.pi/36, 25*np.pi/18, 0.1) #нижняя верхняя часть
x = np.append(x, coords[0])
y = np.append(y, coords[1])

coords = circle(80, 350, 314, 7*np.pi/6, 55*np.pi/36, 0.1) #нижняя нижняя часть
x = np.append(x, coords[0])
y = np.append(y, coords[1])


# # #левое крыло
# coords = circle(300, 15, 130, 0, np.pi/6, 0.1)
# x = np.append(x, coords[0])
# y = np.append(y, coords[1])

# coords = circle(120, 205, 88, 0, 5*np.pi/36, 0.1)
# x = np.append(x, coords[0])
# y = np.append(y, coords[1])

# coords = circle(100, 225, 65, np.pi/18, 7*np.pi/36, 0.1)
# x = np.append(x, coords[0])
# y = np.append(y, coords[1])

# x = np.append(x, [300, 310])
# y = np.append(y,  [100, 120])

# x = np.append(x, [295, 300])
# y = np.append(y,  [120, 100])

# x = np.append(x, [282, 295])
# y = np.append(y,  [114, 120])

# coords = circle(120, 165, 116, 0, 7*np.pi/36, 0.1)
# x = np.append(x, coords[0])
# y = np.append(y, coords[1])

# coords = circle(90, 178, 190, 5*np.pi/3, 2*np.pi, 0.1)
# x = np.append(x, coords[0])
# y = np.append(y, coords[1])

# coords = circle(90, 158, 175, 31*np.pi/18, 2*np.pi, 0.1)
# x = np.append(x, coords[0])
# y = np.append(y, coords[1])

# coords = circle(100, 310, 90, 13*np.pi/18, 35*np.pi/36, 0.1)
# x = np.append(x, coords[0])
# y = np.append(y, coords[1])

# x = np.append(x, [195, 210])
# y = np.append(y,  [80, 107])

# x = np.append(x, [200, 195])
# y = np.append(y,  [115, 80])

# x = np.append(x, [175, 200])
# y = np.append(y,  [80, 115])

# x = np.append(x, [180, 175])
# y = np.append(y,  [110, 80])

# coords = circle(10, 144, 70, 11*np.pi/18, 2*np.pi, 0.1)
# x = np.append(x, coords[0])
# y = np.append(y, coords[1])

# coords = circle(50, 205, 67, 2*np.pi/3, 37*np.pi/36, 0.1)
# x = np.append(x, coords[0])
# y = np.append(y, coords[1])

# coords = circle(60, 200, 80, 13*np.pi/18, 37*np.pi/36, 0.1)
# x = np.append(x, coords[0])
# y = np.append(y, coords[1])

# x = np.append(x, [110, 160])
# y = np.append(y,  [80, 125])

# x = np.append(x, [115, 110])
# y = np.append(y,  [115, 80])

# coords = circle(50, 85, 157, 17*np.pi/12, 31*np.pi/18, 0.1)
# x = np.append(x, coords[0])
# y = np.append(y, coords[1])

# coords = circle(60, 50, 163, 14*np.pi/9, 71*np.pi/36, 0.1)
# x = np.append(x, coords[0])
# y = np.append(y, coords[1])

# x = np.append(x, [90, 110])
# y = np.append(y,  [152, 155])

# coords = circle(30, 80, 180, 59*np.pi/36, 71*np.pi/36, 0.1)
# x = np.append(x, coords[0])
# y = np.append(y, coords[1])

# coords = circle(60, 80, 120, np.pi/3, 5*np.pi/9, 0.1)
# x = np.append(x, coords[0])
# y = np.append(y, coords[1])

# x = np.append(x, [105, 65])
# y = np.append(y,  [195, 175])

# x = np.append(x, [43, 105])
# y = np.append(y,  [180, 195])

# coords = circle(60, 20, 235, 59*np.pi/36, 71*np.pi/36, 0.1)
# x = np.append(x, coords[0])
# y = np.append(y, coords[1])

# coords = circle(20, 75, 205, 4*np.pi/9, 7*np.pi/9, 0.1)
# x = np.append(x, coords[0])
# y = np.append(y, coords[1])

# coords = circle(150, 190, 143, 11*np.pi/18, 31*np.pi/36, 0.1)
# x = np.append(x, coords[0])
# y = np.append(y, coords[1])

# x = np.append(x, [110, 130])
# y = np.append(y,  [275, 280])

# coords = circle(150, 210, 165, 5*np.pi/12, 3*np.pi/4, 0.1)
# x = np.append(x, coords[0])
# y = np.append(y, coords[1])

spline_coords, figure_spline_part = interpolate.splprep([x, y], s=0)
spline_curve = interpolate.splev(figure_spline_part, spline_coords)

plt.plot(x, y, 'bo')
plt.plot(spline_curve[0], spline_curve[1], 'g')

plt.savefig('slide_2_spline_nebula.png')