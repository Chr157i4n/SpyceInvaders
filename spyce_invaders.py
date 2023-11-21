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

screen = pygame.display.set_mode((640, 480))
pygame.display.set_caption("Spyce Invaders")

clock = pygame.time.Clock()

RUN_GAME = True

while RUN_GAME:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            RUN_GAME = False
            print("Quit button was pressed")
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                print("Arrow right")
            elif event.key == pygame.K_LEFT:
                print("Arrow left")
            elif event.key == pygame.K_UP:
                print("Arrow up")
            elif event.key == pygame.K_DOWN:
                print("Arrow down")
            elif event.key == pygame.K_SPACE:
                print("Space")

            elif event.key == pygame.K_w:
                print("W")
            elif event.key == pygame.K_a:
                print("A")
            elif event.key == pygame.K_s:
                print("S")
            elif event.key == pygame.K_d:
                print("D")

        elif event.type == pygame.MOUSEBUTTONDOWN:
            print("Mouse button")


    screen.fill(WHITE)


    pygame.display.flip()

    clock.tick(60)
