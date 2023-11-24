"""
player module
"""
import pygame
from spyce_object import SpyceObject
from spyce_shot import SpyceShot

class SpyceInvader(SpyceObject):
    """
    Player class
    """
    def __init__(self, image, position=pygame.Rect(0,0,0,0)):
        """constructor"""
        SpyceObject.__init__(self, image, position)
        

    def shoot(self, shot_list, image):
        """shoot"""
        shot = SpyceShot(image, self._position)
        shot_list.append(shot)
