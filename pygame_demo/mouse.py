import pygame, sys
import time
import math
from pygame.locals import *


def dist(x1, y1, x2, y2):
    return math.pow(math.pow(x1 - x2, 2) + math.pow(y1 - y2, 2), 0.5)

pygame.init()
DISPLAYSURF = pygame.display.set_mode((400, 300))
pygame.display.set_caption('Hello Pygame!')

pygame.draw.circle(DISPLAYSURF, (255, 0, 0), (200, 150), 30)

color_bg = (0, 0, 0)
color_bot = (255, 0, 0)

while True: # main game loop
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == MOUSEMOTION:
            (mousex, mousey) = event.pos
            if dist(mousex, mousey, 200, 150) < 30:
                color_bg = (255, 255, 255)
            else:
                color_bg = (0, 0, 0)
        elif event.type == MOUSEBUTTONUP:
            (mousex, mousey) = event.pos
            if dist(mousex, mousey, 200, 150) < 30:
                (c1, c2, c3) = color_bot
                color_bot = (c3, c1, c2)
    DISPLAYSURF.fill(color_bg)
    pygame.draw.circle(DISPLAYSURF, color_bot, (200, 150), 30)
    pygame.display.update()
