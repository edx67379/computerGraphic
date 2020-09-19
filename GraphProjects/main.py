from graphics import*
from math import sqrt

width = 300
height = 300
title = "Множество Джулиа"

win = GraphWin(title, width, height)

mx = width // 2
my = height // 2

max = 50
iter = 24

img = Image(Point(mx, my), width, height)

for y in range(-my, my):
    for x in range(-mx, mx):
        n = 0
        z = complex(x * 0.008, y * 0.008)
        c = complex(0.11, -0.66)
        while (abs(z) < sqrt(max)) and (n < iter):
            z = z * z + c
            n += 1
        if n < iter:
            col = (n * 6) % 255
            img.setPixel(mx + x, my + y, color_rgb(col, 0, 0))
img.draw(win)
win.getMouse()
win.close()