from typing import Any
import pygame , sys
from pygame.locals import *
import random
pygame.init()
DIsplay = pygame.display.set_mode((800,600))
class BlockType:
    RED = 0
    GREEN = 1
    BLUE = 2
    YELLOW = 3
    ORANGE = 4
    PURPLE = 5
    CYAN = 6
    BLOCKMAX = 7
Block_RES = {
    BlockType.RED:"pic/red.png"
    }
class Block(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load('pic/red.png')
        self.rect = self.image.get_rect()
        self.rect.center = (400, 300)
    def update(self):
        pressed = pygame.key.get_pressed()
        if pressed[K_LEFT]:
            self.rect.move_ip(-1 , 0)
        elif pressed[K_RIGHT]:
            self.rect.move_ip(1 , 0)
        elif pressed[K_UP]:
            self.rect.move_ip(0 , -1)
        elif pressed[K_DOWN]:
            self.rect.move_ip(0 , 1)
    def draw(self, surface):
        surface.blit(self.image, self.rect)
B = Block()
while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
    B.update()
    DIsplay.fill( (0,0,0) ) 
    B.draw(DIsplay)
    pygame.display.update()