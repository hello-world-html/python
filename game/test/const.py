import pygame
import sys
from pygame.locals import *
class BlockType:
    RED = 0
    GREEN = 1
    BLUE = 2
    YELLOW = 3
    ORANGE = 4
    PURPLE = 5
    CYAN = 6
    BLOCKMAX = 7

BLOCK_RES = {
    BlockType.RED: "pic/red.png",
    BlockType.GREEN: "pic/green.png",
    BlockType.BLUE: "pic/blue.png",
    BlockType.YELLOW: "pic/yellow.png",
    BlockType.ORANGE: "pic/orange.png",
    BlockType.PURPLE: "pic/purple.png",
    BlockType.CYAN: "pic/cyan.png",
}
