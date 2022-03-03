import pygame
import random
pygame.init()
win = pygame.display.set_mode((500,500))

clck = pygame.time.Clock
x = 50
y = 400
z = 75
w = 300
v = 100
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            quit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                y = y - 10
                z = z - 5
            elif event.key == pygame.K_DOWN:
                y = y + 10
                z = z + 5
            elif event.key == pygame.K_LEFT:
                x = x - 10
                w = w + 5
                v = v + 5
            elif event.key == pygame.K_RIGHT:
                x = x + 10
                w = w - 5
                v = v - 5
    x = pygame.mouse.get_pos()[0]
    y = pygame.mouse.get_pos()[1]
    z = pygame.mouse.get_pos()[1] / 2 -100
    v = -(pygame.mouse.get_pos()[0] / 2 - 100)
    w = -(pygame.mouse.get_pos()[0] / 2 )+ 350

    win.fill((255, 255, 255))

    pygame.draw.line(win, (0, 0, 0), (x, y), (x+400, y), 3)
    pygame.draw.line(win, (0, 0, 0), (x+400, y), (x + w, y-z), 3)
    pygame.draw.line(win, (0, 0, 0), (x+w, y-z), (x + v, y-z), 3)
    pygame.draw.line(win, (0, 0, 0), (x + v, y-z), (x, y), 3)




    pygame.display.update()
