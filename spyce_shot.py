"""
player module
"""
import pygame
from spyce_object import SpyceObject

class SpyceShot(SpyceObject):
    """
    Player class
    """
    def __init__(self, position):
        """constructor"""
        SpyceObject.__init__(self, "images/ammo.png", position)
        self._image = pygame.transform.scale(self._image, (16, 36))

    def move(self):
        """move only up"""
        self._position.y -= 1