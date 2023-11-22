"""
player module
"""
from spyce_object import SpyceObject

class SpycePlayer(SpyceObject):
    """
    Player class
    """
    def __init__(self, image_path):
        """constructor"""
        SpyceObject.__init__(self, image_path)
