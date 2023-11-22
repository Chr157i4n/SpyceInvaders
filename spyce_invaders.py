"""
Space Invaders game 
"""
import pygame
from spyce_player import SpycePlayer

pygame.init()

ORANGE  = ( 255, 140, 0)
RED     = ( 255, 0, 0)
GREEN   = ( 0, 255, 0)
BLACK = ( 0, 0, 0)
WHITE   = ( 255, 255, 255)

WINDOWSIZEX = 640
WINDOWSIZEY = 480

pygame.display.set_caption("Spyce Invaders")
program_icon = pygame.image.load('images/spaceship.png')
pygame.display.set_icon(program_icon)
screen = pygame.display.set_mode((WINDOWSIZEX, WINDOWSIZEY))

background_image = pygame.image.load("images/background.png")
background_image = pygame.transform.scale(background_image, (WINDOWSIZEX, WINDOWSIZEY))



player = SpycePlayer("images/spaceship.png")

clock = pygame.time.Clock()

RUN_GAME = True

while RUN_GAME:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            RUN_GAME = False
            print("Quit button was pressed")
        else:

            keys=pygame.key.get_pressed()
            if keys[pygame.K_a]:
                player.move_x(-1)
            if keys[pygame.K_d]:
                player.move_x(1)
            if keys[pygame.K_w]:
                player.move_y(-1)
            if keys[pygame.K_s]:
                player.move_y(1)


    screen.fill(WHITE)
    screen.blit(background_image, (0, 0))
    player.draw(screen)
    
    pygame.display.flip()

    clock.tick(60)
