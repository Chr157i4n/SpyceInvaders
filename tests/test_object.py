"""
test for spyce_object.py
"""

import unittest
from spyce_object import SpyceObject

class TestSpyceObject(unittest.TestCase):
    """
    testclass
    """

    def setUp(self):
        """setup"""
        self.object = SpyceObject("images/spaceship.png")

    def test_move(self):
        """test move function"""
        self.object.move_x(10)
        self.assertEqual(self.object.get_position().x, 10, "x position after move_x is wrong")
        self.object.move_y(20)
        self.assertEqual(self.object.get_position().y, 20, "y position after move_y is wrong")

if __name__ == '__main__':
    unittest.main()
