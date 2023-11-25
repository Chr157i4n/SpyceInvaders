"""
player module
"""
import copy
import time
import pygame
from spyce_object import SpyceObject
from spyce_shot import SpyceShot



class SpycePlayer(SpyceObject):
    """
    Player class
    """
    _last_shot_time = 0
    _shoot_delay = 1

    def __init__(self, image, position=pygame.Rect(0,0,0,0)):
        """constructor"""
        SpyceObject.__init__(self, image, position)


    def shoot(self, shot_list, image):
        """shoot"""
        current_time = time.time()
        if(current_time < self._last_shot_time + self._shoot_delay):
            return False
        self._last_shot_time = current_time
        shot_position = copy.deepcopy(self._position)
        shot_position.x += 40
        shot = SpyceShot(image, shot_position)
        shot_list.append(shot)
        return True
