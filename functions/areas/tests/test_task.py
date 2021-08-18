import unittest

from task import square
from task import rectangle
from task import triangle
from task import circle


# todo: replace this with an actual test
class TestCase(unittest.TestCase):
    def test_square(self):
        self.assertEqual(square(2), 4, msg="the area of a 2x2 square = 4")

    def test_rectangle(self):
        self.assertEqual(rectangle(4,3), 12, msg="the area of a 4x3 rectangle = 12")

    def test_triangle(self):
        self.assertEqual(triangle(4,3), 6, msg="the area of a 4x3 triangle = 6")

    def test_circle(self):
        self.assertEqual(circle(2), 12.566370614359172, msg="the area of a 2 radius circle = 12 and a bit")
