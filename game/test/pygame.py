import pygame
import sys
from pygame.locals import *
import random

pygame.init()
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
DISPLAY = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

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

class Block(pygame.sprite.Sprite):
    def __init__(self, blockType, pos):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(BLOCK_RES[blockType])
        self.rect = self.image.get_rect()
        self.rect.center = pos

    def update(self):
        pressed = pygame.key.get_pressed()
        if pressed[K_LEFT]:
            self.rect.move_ip(-1, 0)
        elif pressed[K_RIGHT]:
            self.rect.move_ip(1, 0)
        elif pressed[K_UP]:
            self.rect.move_ip(0, -1)
        elif pressed[K_DOWN]:
            self.rect.move_ip(0, 1)

    def draw(self, surface):
        surface.blit(self.image, self.rect)

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
import pygame
import sys
from pygame.locals import *
import random

pygame.init()
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
DISPLAY = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

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

class Block(pygame.sprite.Sprite):
    def __init__(self, blockType, pos):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(BLOCK_RES[blockType])
        self.rect = self.image.get_rect()
        self.rect.center = pos

    def update(self):
        pressed = pygame.key.get_pressed()
        if pressed[K_LEFT]:
            self.rect.move_ip(-1, 0)
        elif pressed[K_RIGHT]:
            self.rect.move_ip(1, 0)
        elif pressed[K_UP]:
            self.rect.move_ip(0, -1)
        elif pressed[K_DOWN]:
            self.rect.move_ip(0, 1)

    def draw(self, surface):
        surface.blit(self.image, self.rect)

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
