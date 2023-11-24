"""
player module
"""
import copy
import pygame
from spyce_object import SpyceObject
from spyce_shot import SpyceShot


class SpycePlayer(SpyceObject):
    """
    Player class
    """
    def __init__(self, image, position=pygame.Rect(0,0,0,0)):
        """constructor"""
        SpyceObject.__init__(self, image, position)


    def shoot(self, shot_list, image):
        """shoot"""
        shot_position = copy.deepcopy(self._position)
        shot_position.x += 40
        shot = SpyceShot(image, shot_position)
        shot_list.append(shot)
