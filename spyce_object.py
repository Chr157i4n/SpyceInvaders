"""
object module
"""
import pygame

class SpyceObject:
    """
    Object class
    """
    image = None
    position = None

    def __init__(self, image_path):
        """constructor"""
        self.image = pygame.image.load(image_path)
        self.image = pygame.transform.scale(self.image, (100, 100))
        self.position = self.image.get_rect()
        print(self.position)
        self.position.x = 50
        self.position.y = 50

    def draw(self, screen):
        """draw"""
        screen.blit(self.image, self.position)

    def move_x(self, x):
        """move x relative"""
        self.position.x += x

    def move_y(self, y):
        """move y relative"""
        self.position.y += y
