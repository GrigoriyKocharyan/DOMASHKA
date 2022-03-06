import pygame
import random

pygame.init()
win = pygame.display.set_mode((500, 500))
lol = 0
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            quit()

    win.fill((0, 0, 0))
    for i in range(0,550, 50):
        pygame.draw.ellipse(win, (255,255,255), (0,250-(i/2)-lol,500,1+i),2)
    for l in range(0, 550, 50):
        pygame.draw.ellipse(win, (255,255,255), (250-(l/2)-lol,0,1+l,500),2)
    lol = pygame.mouse.get_pos()[0]
    pygame.display.update()
