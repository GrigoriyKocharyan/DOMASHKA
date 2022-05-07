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
            elif mx <= 200 and my <= 200 and FIGURA == 'circle' and POLE[0] == 0:
                POLE[0] = -1
                FIGURA = 'cross'
            if mx >= 200 and my <= 200 and mx <= 400 and my >= 0 and FIGURA == 'cross' and POLE[1] == 0:
                POLE[1] = 1
                FIGURA = 'circle'
            elif mx >= 200 and my <= 200 and mx <= 400 and my >= 0 and FIGURA == 'circle' and POLE[1] == 0:
                POLE[1] = -1
                FIGURA = 'cross'
            if mx >= 400 and my <= 200 and mx <= 600 and my >= 0 and FIGURA == 'cross' and POLE[2] == 0:
                POLE[2] = 1
                FIGURA = 'circle'
            elif mx >= 400 and my <= 200 and mx <= 600 and my >= 0 and FIGURA == 'circle' and POLE[2] == 0:
                POLE[2] = -1
                FIGURA = 'cross'

                
            if mx >= 0 and my <= 400 and mx <= 200 and my >= 200 and FIGURA == 'cross' and POLE[3] == 0:
                POLE[3] = 1
                FIGURA = 'circle'
            elif mx >= 0 and my <= 400 and mx <= 200 and my >= 200 and FIGURA == 'circle' and POLE[3] == 0:
                POLE[3] = -1
                FIGURA = 'cross'
            if mx >= 200 and my <= 400 and mx <= 400 and my >= 200 and FIGURA == 'cross' and POLE[4] == 0:
                POLE[4] = 1
                FIGURA = 'circle'
            elif mx >= 200 and my <= 400 and mx <= 400 and my >= 200 and FIGURA == 'circle' and POLE[4] == 0:
                POLE[4] = -1
                FIGURA = 'cross'
            if mx >= 400 and my <= 400 and mx <= 600 and my >= 200 and FIGURA == 'cross' and POLE[5] == 0:
                POLE[5] = 1
                FIGURA = 'circle'
            elif mx >= 400 and my <= 400 and mx <= 600 and my >= 200 and FIGURA == 'circle' and POLE[5] == 0:
                POLE[5] = -1
                FIGURA = 'cross'

            if mx >= 0 and my <= 600 and mx <= 200 and my >= 400 and FIGURA == 'cross' and POLE[6] == 0:
                POLE[6] = 1
                FIGURA = 'circle'
            elif mx >= 0 and my <= 600 and mx <= 200 and my >= 400 and FIGURA == 'circle' and POLE[6] == 0:
                POLE[6] = -1
                FIGURA = 'cross'
            if mx >= 200 and my <= 600 and mx <= 400 and my >= 400 and FIGURA == 'cross' and POLE[7] == 0:
                POLE[7] = 1
                FIGURA = 'circle'
            elif mx >= 200 and my <= 600 and mx <= 400 and my >= 400 and FIGURA == 'circle' and POLE[7] == 0:
                POLE[7] = -1
                FIGURA = 'cross'
            if mx >= 400 and my <= 600 and mx <= 600 and my >= 400 and FIGURA == 'cross' and POLE[8] == 0:
                POLE[8] = 1
                FIGURA = 'circle'
            elif mx >= 400 and my <= 600 and mx <= 600 and my >= 400 and FIGURA == 'circle' and POLE[8] == 0:
                POLE[8] = -1
                FIGURA = 'cross'

    win.fill(WH)
    for xx in range(-1, 600, 200):
        draw.line(win, (BL), (xx, 0), (xx, 600),2)
    for yy in range(-1, 600, 200):
        draw.line(win, (BL), (0, yy), (600, yy),2)

    print(POLE)

    if POLE[0] == 1:
        draw.line(win, KPECT, (0, 0), (200, 200), 5)
        draw.line(win, KPECT, (0, 200), (200, 0), 5)
    elif POLE[0] == -1:
        draw.circle(win, CIRCLE, (100, 100), 100, 5)
    if POLE[1] == 1:
        draw.line(win, KPECT, (200, 0), (400, 200), 5)
        draw.line(win, KPECT, (200, 200), (400, 0), 5)
    elif POLE[1] == -1:
        draw.circle(win, CIRCLE, (300, 100), 100, 5)
    if POLE[2] == 1:
        draw.line(win, KPECT, (400, 0), (600, 200), 5)
        draw.line(win, KPECT, (400, 200), (600, 0), 5)
    elif POLE[2] == -1:
        draw.circle(win, CIRCLE, (500, 100), 100, 5)

        
    if POLE[3] == 1:
        draw.line(win, KPECT, (0, 0+200), (200, 200+200), 5)
        draw.line(win, KPECT, (0, 200+200), (200, 0+200), 5)
    elif POLE[3] == -1:
        draw.circle(win, CIRCLE, (100, 100+200), 100, 5)
    if POLE[4] == 1:
        draw.line(win, KPECT, (200, 0+200), (400, 200+200), 5)
        draw.line(win, KPECT, (200, 200+200), (400, 0+200), 5)
    elif POLE[4] == -1:
        draw.circle(win, CIRCLE, (300, 100+200), 100, 5)
    if POLE[5] == 1:
        draw.line(win, KPECT, (400, 0+200), (600, 200+200), 5)
        draw.line(win, KPECT, (400, 200+200), (600, 0+200), 5)
    elif POLE[5] == -1:
        draw.circle(win, CIRCLE, (500, 100+200), 100, 5)

    if POLE[6] == 1:
        draw.line(win, KPECT, (0, 0+400), (200, 200+400), 5)
        draw.line(win, KPECT, (0, 200+400), (200, 0+400), 5)
    elif POLE[6] == -1:
        draw.circle(win, CIRCLE, (100, 100+400), 100, 5)
    if POLE[7] == 1:
        draw.line(win, KPECT, (200, 0+400), (400, 200+400), 5)
        draw.line(win, KPECT, (200, 200+400), (400, 0+400), 5)
    elif POLE[7] == -1:
        draw.circle(win, CIRCLE, (300, 100+400), 100, 5)
    if POLE[8] == 1:
        draw.line(win, KPECT, (400, 0+400), (600, 200+400), 5)
        draw.line(win, KPECT, (400, 200+400), (600, 0+400), 5)
    elif POLE[8] == -1:
        draw.circle(win, CIRCLE, (500, 100+400), 100, 5)
       

    if POLE[0] == 1 and POLE[1] == 1 and POLE[2] == 1:
        draw.line(win, RE, (50,100),(550,100), 10)
    elif POLE[0] == -1 and POLE[1] == -1 and POLE[2] == -1:
        draw.line(win, RE, (50,100),(550,100), 10)

    if POLE[3] == 1 and POLE[4] == 1 and POLE[5] == 1:
        draw.line(win, RE, (50,300),(550,300), 10)
    elif POLE[3] == -1 and POLE[4] == -1 and POLE[5] == -1:
        draw.line(win, RE, (50,300),(550,300), 10)

    if POLE[6] == 1 and POLE[7] == 1 and POLE[8] == 1:
        draw.line(win, RE, (50,500),(550,500), 10)
    elif POLE[6] == -1 and POLE[7] == -1 and POLE[8] == -1:
        draw.line(win, RE, (50,500),(550,500), 10)

    if POLE[0] == 1 and POLE[3] == 1 and POLE[6] == 1:
        draw.line(win, RE, (100,50),(100,550), 10)
    elif POLE[0] == -1 and POLE[3] == -1 and POLE[6] == -1:
        draw.line(win, RE, (100,50),(100,550), 10)

    if POLE[1] == 1 and POLE[4] == 1 and POLE[7] == 1:
        draw.line(win, RE, (300,50),(300,550), 10)
    elif POLE[1] == -1 and POLE[4] == -1 and POLE[7] == -1:
        draw.line(win, RE, (300,50),(300,550), 10)

    if POLE[2] == 1 and POLE[5] == 1 and POLE[8] == 1:
        draw.line(win, RE, (500,50),(500,550), 10)
    elif POLE[1] == -1 and POLE[4] == -1 and POLE[7] == -1:
        draw.line(win, RE, (500,50),(500,550), 10)

    if POLE[0] == 1 and POLE[4] == 1 and POLE[8] == 1:
        draw.line(win, RE, (50,50),(550,550), 10)
    elif POLE[0] == -1 and POLE[4] == -1 and POLE[8] == -1:
        draw.line(win, RE, (50,50),(550,550), 10)

    if POLE[2] == 1 and POLE[4] == 1 and POLE[6] == 1:
        draw.line(win, RE, (50,550),(550,50), 10)
    elif POLE[2] == -1 and POLE[4] == -1 and POLE[6] == -1:
        draw.line(win, RE, (50,550),(5S50,50), 10)

    display.update()
