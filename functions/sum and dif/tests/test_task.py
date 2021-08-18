import unittest

from task import sum
from task import dif

# todo: replace this with an actual test
class TestCase(unittest.TestCase):
    def test_add(self):
        self.assertEqual(sum(1, 2), 3, msg="adds 1 + 2 to equal 3")
    def test_sub(self):
        self.assertAlmostEqual(dif(10,5),5, msg="subtract 5 from 10")
