import pygame
import sys
from pygame.locals import *
from const import *
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
    def draw(self,surface):
        surface.blit(self.image, self.rect)