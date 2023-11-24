#pylint: disable=global-variable-not-assigned
"""
Space Invaders game 
"""
import pygame
from spyce_player import SpycePlayer
from spyce_invader import SpyceInvader


ORANGE  = ( 255, 140, 0)
RED     = ( 255, 0, 0)
GREEN   = ( 0, 255, 0)
BLACK = ( 0, 0, 0)
WHITE   = ( 255, 255, 255)

WINDOWSIZEX = 1366
WINDOWSIZEY = 768

RUN_GAME = True



pygame.init()

pygame.display.set_caption("Spyce Invaders")
program_icon = pygame.image.load('images/spaceship.png')
pygame.display.set_icon(program_icon)
screen = pygame.display.set_mode((WINDOWSIZEX, WINDOWSIZEY))

background_image = pygame.image.load("images/background.png")
background_image = pygame.transform.scale(background_image, (WINDOWSIZEX, WINDOWSIZEY))


image_spaceship = pygame.image.load("images/spaceship.png")
image_spaceship = pygame.transform.scale(image_spaceship, (80, 80))
image_invader = pygame.image.load("images/invader.png")
image_invader = pygame.transform.scale(image_invader, (80, 80))
image_shot = pygame.image.load("images/ammo.png")
image_shot = pygame.transform.scale(image_shot, (16, 36))


player = SpycePlayer(image_spaceship, pygame.Rect(WINDOWSIZEX/2, WINDOWSIZEY-100, 0, 0))
shot_list = []
invader_list = []
for i in range(10):
    invader = SpyceInvader(image_invader, pygame.Rect(100*i, 40, 0, 0))
    invader_list.append(invader)

clock = pygame.time.Clock()



def run_game():
    """run game function"""
    global ORANGE, RED, GREEN, BLACK, WHITE, WINDOWSIZEX, WINDOWSIZEY, RUN_GAME
    global screen, player, clock

    while RUN_GAME:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                RUN_GAME = False
                print("Quit button was pressed")
            else:

                keys=pygame.key.get_pressed()
                if keys[pygame.K_a]:
                    player.move(pygame.Rect(-2, 0, 0, 0))
                if keys[pygame.K_d]:
                    player.move(pygame.Rect(2, 0, 0, 0))
                if keys[pygame.K_w]:
                    player.move(pygame.Rect(0, -2, 0, 0))
                if keys[pygame.K_s]:
                    player.move(pygame.Rect(0, 2, 0, 0))
                if keys[pygame.K_SPACE]:
                    player.shoot(shot_list, image_shot)

        screen.fill(WHITE)
        screen.blit(background_image, (0, 0))
        player.draw(screen)
        for shot in shot_list.copy():
            shot.move()
            if shot.get_position().y < 20:
                shot_list.remove(shot)
                continue
            for invader in invader_list.copy():
                if shot.check_collision(invader):
                    invader_list.remove(invader)
            shot.draw(screen)
        for invader in invader_list.copy():
            invader.draw(screen)

        pygame.display.flip()

        clock.tick(60)


if __name__ == '__main__':
    run_game()
