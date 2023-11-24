"""
player module
"""
import pygame
from spyce_object import SpyceObject

class SpyceShot(SpyceObject):
    """
    Player class
    """
    def __init__(self, image, position):
        """constructor"""
        SpyceObject.__init__(self, image, position)
        

    def move(self, move=pygame.Rect(0,0,0,0)):
        """move only up"""
        del move
        self._position.y -= 1