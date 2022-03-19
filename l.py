import pygame
import random

color = [255,255,0]
x = 10
y = 10
z = 1

g= 1
xr = 250
dx = 10
press = 0


k = 20


pygame.init()
win = pygame.display.set_mode((500, 500))
lol = 0
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            quit()



    if pygame.key.get_pressed()[pygame.K_LEFT]:
        press = 1
        x -= c
    if pygame.key.get_pressed()[pygame.K_RIGHT]:
        x += c
        press = 1
    if pygame.key.get_pressed()[pygame.K_UP]:
        y -= c
        press = 1
    if pygame.key.get_pressed()[pygame.K_DOWN]:
        y += c
        press = 1








    if x >= 510:
        x = -100
    else:
        if x <= -110:
            x = 500

    if y >= 510:
        y = -100
    else:
        if y <= -110:
            y = 500



    if x > 400:
        color = [255,0,0]
        c = 0.5
        k = 40
    elif y > 400:
        color = [255, 0, 0]
        c = 0.5
        k = 40
    elif x < 100:
        color = [255, 0, 0]
        c = 0.5
        k = 40
    elif y < 100:
        color = [255, 0, 0]
        c = 0.5
        k = 40

    elif y > 240 and y < 260 and x > 240 and x < 260:
        color = [0, 255, 0]
        c = 0.5
        k = 10

    else:
        color = [255,255,0]
        c= 1
        k = 20

    win.fill((255, 255, 255))


    pygame.draw.circle(win, (color), (x, y), k)
    pygame.display.update()


    pygame.time.delay(1)
