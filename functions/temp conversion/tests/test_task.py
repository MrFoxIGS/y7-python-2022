import unittest

from task import to_kelvin
from task import to_fahrenheit
from task import temp_convert


# todo: replace this with an actual test
class TestCase(unittest.TestCase):
    def test_kelvin(self):
        self.assertEqual(to_kelvin(30), 303.15, msg="30C is 303.15K")
    def test_fahrenheit(self):
        self.assertEqual(to_fahrenheit(30), 86.0, msg="30C is 86K")
    def test_convertF(self):
        self.assertEqual(temp_convert("fahrenheit",20),68.0, msg="20C is 68F")
    def test_convertK(self):
        self.assertEqual(temp_convert("kelvin",20),293.15, msg="20C is 293.15K")
