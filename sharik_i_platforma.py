import pygame
import random


x = 0
y = 0
z = 1

g= 1
xr = 250
dx = 10

def jump(x, g, z):
    z = 1
    for i in range(0, 50):
        x -= 10






pygame.init()
win = pygame.display.set_mode((500, 500))
lol = 0
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            quit()



    if pygame.key.get_pressed()[pygame.K_LEFT]:
        xr -= 1
    if pygame.key.get_pressed()[pygame.K_RIGHT]:
        xr += 1


    if x > 270 and xr > 150 and xr < 300:
        dx=-100
        x+=dx
        jump(x, g, z)
    elif dx < 0 and x > 270:
        x += dx
    elif dx < 0 and x < 270:
        dx=1
        x += dx
    else:
        x += 0.01 * z
        z += 1.1
        if x > 500:
            quit()




    y += 1

    win.fill((255, 255, 255))

    pygame.draw.circle(win, (255, 255, 0), (250, x), 30)
    pygame.draw.rect(win, (255, 0, 255), (xr, 300, 100,50))
    pygame.display.update()


    pygame.time.delay(100)
