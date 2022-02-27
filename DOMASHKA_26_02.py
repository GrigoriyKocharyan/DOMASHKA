import pygame

x = 50
y = 400
z = 75

w = 300
v = 100

YELLOW = (255,255,0)
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
CYAN = (0, 255, 255)
LIGHT = (255, 228, 181)


pygame.init()
win = pygame.display.set_mode((500,500))


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            quit()


    win.fill(CYAN)

    pygame.draw.line(win, (LIGHT), (250, 250), (250, 350), 10)
    pygame.draw.line(win, (LIGHT), (250, 275), (275, 325), 10)
    pygame.draw.line(win, (LIGHT), (250, 275), (225, 325), 10)
    pygame.draw.line(win, (BLUE), (250, 275), (235, 300), 15)
    pygame.draw.line(win, (BLUE), (250, 275), (265, 300), 15)
    pygame.draw.line(win, (BLUE), (250, 275), (250, 350), 15)
    pygame.draw.line(win, (0,0,0), (250, 350), (275, 425), 15)
    pygame.draw.line(win, (0,0,0), (250, 350), (225, 425), 15)
    pygame.draw.circle(win, (LIGHT), (250, 250), 30)
    pygame.draw.rect(win, (GREEN), (0,425,500,100))
    pygame.draw.circle(win, (YELLOW), (100, 100), 30)

    pygame.display.update()
