import pygame
import sys
import random
from pygame.locals import *
from block import *
from const import *
from blockGroup import *

pygame.init()
DISPLAY = pygame.display.set_mode((800, 600))

BlockGroups = []
for x in range(5):
    conf = BlockGroups.GenerateBlockGroupConfig(x*4, x)
    BlockGroups.append( BlockGroups(32, 32, conf, (240, 50)) )

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

    DISPLAY.fill((0, 0, 0))
    for bg in BlockGroups:
        bg.draw(DISPLAY)

    pygame.display.update()
