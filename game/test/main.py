import pygame
import sys
from pygame.locals import *
from block import *
from const import *


pygame.init()
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
DISPLAY = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

P = Block(BlockType.PURPLE, (200, 300))
C = Block(BlockType.CYAN, (600, 300))

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
    P.update()
    C.update()
    DISPLAY.fill((0, 0, 0))
    P.draw(DISPLAY)
    C.draw(DISPLAY)
    pygame.display.update()
