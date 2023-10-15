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


class BlockGruopType:
    FIXED = 0
    DROP = 1
    MOVE = 2
    BLOCKMAX = 3


BLOCK_RES = {
    BlockType.RED: "pic/red.png",
    BlockType.GREEN: "pic/green.png",
    BlockType.BLUE: "pic/blue.png",
    BlockType.YELLOW: "pic/yellow.png",
    BlockType.ORANGE: "pic/orange.png",
    BlockType.PURPLE: "pic/purple.png",
    BlockType.CYAN: "pic/cyan.png",
}

GAME_ROW = 17
GAME_COL = 10


BLOCK_SIZE_W = 32
BLOCK_SIZE_H = 32


BLOCK_SHAPE = [
    [(0, 0), (0, 1), (1, 0), (1, 1)],
    [(0, 0), (0, 1), (0, 2), (0, 3)],
    [(0, 0), (0, 1), (1, 1), (1, 2)],
    [(0, 1), (1, 0), (1, 1), (1, 2)],
]
