import pygame
import sys
import random
from pygame.locals import *
from game import *
from const import *

pygame.init()
DISPLAY = pygame.display.set_mode((800, 600))
game = Game(DISPLAY)


while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
    game.update()
    DISPLAY.fill((0, 0, 0))
    game.draw()

    pygame.display.update()
