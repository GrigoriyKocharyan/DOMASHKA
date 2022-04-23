from pygame import *
from random import *



FPS = 60
cl = time.Clock()
a = 0
x = 0
y = 0
c = 0
r = 0
aa = 0

init()
win = display.set_mode((500, 500))

win.fill((0,0,0))

while True:
    for i in event.get():
        if i.type == QUIT:
            exit()

    if mouse.get_pressed()[0]:
        a = mouse.get_pos()
        if aa == 0:
            draw.circle(win, (randint(0,255),randint(0,255),randint(0,255)), (a[0], a[1]), 50)
        elif aa == 1:
            draw.rect(win, (randint(0,255),randint(0,255),randint(0,255)), (a[0] -20, a[1]-20, 40,40))


    if key.get_pressed()[K_w]:
        if aa == 0:
            aa = 1
            win.fill((0, 0, 0))
        if aa == 1:
            aa = 0
            win.fill((0, 0, 0))

    if key.get_pressed()[K_SPACE]:
        win.fill((0, 0, 0))

    display.update()
