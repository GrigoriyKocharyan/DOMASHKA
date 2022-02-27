import pygame
from random import *

x, y, = 200, 200

ms = 0

def clean():
    win.fill((0, 0, 0))

pygame.init()
win = pygame.display.set_mode((500, 500))

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            quit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                clean()

    ms = pygame.mouse.get_pos()


    a = randint(100, 255)
    b = randint(100, 255)
    c = randint(100, 255)

    ms = pygame.mouse.get_pos()
    pygame.draw.circle(win, (a, b, c), (ms[0], ms[1]), 10)

    pygame.display.update()
