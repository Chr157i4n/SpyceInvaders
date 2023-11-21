"""
Space Invaders game 
"""
import pygame

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

spaceship_image = pygame.image.load("images/spaceship.png")
spaceship_image = pygame.transform.scale(spaceship_image, (100, 100))
spaceship_imagerect = spaceship_image.get_rect()
spaceship_imagerect.x = WINDOWSIZEX/2-50
spaceship_imagerect.y = WINDOWSIZEY-100

print(spaceship_imagerect)

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
                spaceship_imagerect.x -= 1
            if keys[pygame.K_d]:
                spaceship_imagerect.x += 1
            if keys[pygame.K_w]:
                spaceship_imagerect.y -= 1
            if keys[pygame.K_s]:
                spaceship_imagerect.y += 1


    screen.fill(WHITE)
    screen.blit(background_image, (0, 0))
    screen.blit(spaceship_image, spaceship_imagerect)

    pygame.display.flip()

    clock.tick(60)
