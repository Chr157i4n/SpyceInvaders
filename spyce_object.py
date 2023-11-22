"""
object module
"""
import pygame

class SpyceObject:
    """
    Object class
    """
    _image = None
    _position = None

    def __init__(self, image_path):
        """constructor"""
        self._image = pygame.image.load(image_path)
        self._image = pygame.transform.scale(self._image, (100, 100))
        self._position = self._image.get_rect()
        self._position.x = 0
        self._position.y = 0

    def draw(self, screen):
        """draw"""
        screen.blit(self._image, self._position)

    def move_x(self, x):
        """move x relative"""
        self._position.x += x

    def move_y(self, y):
        """move y relative"""
        self._position.y += y

    def get_position(self):
        return self._position
