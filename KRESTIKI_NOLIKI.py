from pygame import *
from random import *
from math import *

POLE = [0, 0, 0,
        0, 0, 0,
        0, 0, 0]

my, mx = 0, 0

FIGURA = 'cross'

BL = (0, 0, 0)
GR = (100, 100, 100)
WH = (255, 255, 255)
RE = (255, 0, 0)
YE = (255, 255, 0)
LG = (0, 200, 200)

KPECT = '#046582'
CIRCLE = '#e4bad4'

init()
win = display.set_mode((600, 600))
win.fill((0,0,0))
FPS = 60
cl = time.Clock()

while True:
    for i in event.get():
        if i.type == QUIT:
            exit()
        if i.type == MOUSEBUTTONDOWN:
            mx = mouse.get_pos()[0]
            my = mouse.get_pos()[1]
            if mx <= 200 and my <= 200 and FIGURA == 'cross' and POLE[0] == 0:
                POLE[0] = 1
                FIGURA = 'circle'
            if mx <= 200 and my <= 200 and FIGURA == 'circle' and POLE[0] == 0:
                POLE[0] = -1
                FIGURA = 'cross'
            if mx >= 200 and my <= 200 and mx <= 400 and my >= 0 and FIGURA == 'cross' and POLE[0] == 0:
                POLE[1] = 1
                FIGURA = 'circle'
            if mx >= 200 and my <= 200 and mx <= 400 and my >= 0 and FIGURA == 'circle' and POLE[0] == 0:
                POLE[1] = -1
                FIGURA = 'cross'




    win.fill(WH)
    for xx in range(-1, 600, 200):
        draw.line(win, (BL), (xx, 0), (xx, 600),2)
    for yy in range(-1, 600, 200):
        draw.line(win, (BL), (0, yy), (600, yy),2)



    if POLE[0] == 1:
        draw.line(win, KPECT, (0, 0), (200, 200), 5)
        draw.line(win, KPECT, (0, 200), (200, 0), 5)
    if POLE[0] == -1:
        draw.circle(win, CIRCLE, (100, 100), 100, 5)
    if POLE[1] == 1:
        draw.line(win, KPECT, (200, 0), (400, 200), 5)
        draw.line(win, KPECT, (200, 200), (400, 0), 5)
    if POLE[1] == -1:
        draw.circle(win, CIRCLE, (300, 100), 100, 5)
    display.update()
