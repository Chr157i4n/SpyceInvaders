"""
player module
"""
import pygame
from spyce_object import SpyceObject
from spyce_shot import SpyceShot

class SpycePlayer(SpyceObject):
    """
    Player class
    """
    def __init__(self, image_path):
        """constructor"""
        SpyceObject.__init__(self, image_path)
        self._image = pygame.transform.scale(self._image, (100, 100))

    def shoot(self, shot_list):
        """shoot"""
        shot = SpyceShot(self._position)
        shot_list.append(shot)
