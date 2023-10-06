import pygame , sys
from pygame.locals import *
import random
pygame.init()
DIsplay = pygame.display.set_mode((800,600))
Imgae = pygame.image.load('pic/red.png')
Rect = Imgae.get_rect()
Rect.center = (400, 300)
while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
    pressed = pygame.key.get_pressed()
    if pressed[K_LEFT]:
        Rect.move_ip(-1 , 0)
    elif pressed[K_RIGHT]:
        Rect.move_ip(1 , 0)
    elif pressed[K_UP]:
        Rect.move_ip(0 , -1)
    elif pressed[K_DOWN]:
        Rect.move_ip(0 , 1)

    DIsplay.fill( (0,0,0) ) 
    DIsplay.blit(Imgae, Rect)

    pygame.display.update()