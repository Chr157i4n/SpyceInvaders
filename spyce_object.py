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

    def __init__(self, image_path, position=pygame.Rect(0,0,0,0)):
        """constructor"""
        self._image = pygame.image.load(image_path)
        self._position = self._image.get_rect()
        self._position.x = position.x
        self._position.y = position.y

    def draw(self, screen):
        """draw"""
        screen.blit(self._image, self._position)

    def move(self, move=pygame.Rect(0,0,0,0)):
        """move"""
        self._position.x = move.x
        self._position.y = move.y

    def move_x(self, x):
        """move x relative"""
        self._position.x += x

    def move_y(self, y):
        """move y relative"""
        self._position.y += y

    def get_position(self):
        """get postion"""
        return self._position
