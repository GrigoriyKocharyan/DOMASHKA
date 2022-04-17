from pygame import *
import random


class Circle():
    def __init__(self, x, y, r, c):

        self.x = x
        self.y = y
        self.r = r
        self.c = c

    def h_m(self, x, y, r, c):
        if self.dir == 'right':
            self.x += 1
            if self.x >500:
                self.dir = 'left'
        else:
            self.x += 1
            if self.x < 0:
                self.dir = 'right'

    def draw(self,x,y,r,c):
        draw.circle(win, (c), (x, y), r)


FPS = 300
cl = time.Clock()

x = 0
y = 0
c = 0
r = 0
crug = Circle(x, y, r, c)

a=[]
for h in range(100):
    a.append(Circle(h * 10, h * 5, 30, random.choices(range(256), k=3)))


init()
win = display.set_mode((500, 500))


while True:
    for i in event.get():
        if i.type == QUIT:
            quit()

    win.fill((255, 255, 255))

    

    cl.tick(FPS)
    display.update()
