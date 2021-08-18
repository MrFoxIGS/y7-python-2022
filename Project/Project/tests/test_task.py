import unittest


class NamesTestCase(unittest.TestCase):

   def test_first_last_name(self):
       result = ("Hello")
       self.assertEqual(result, "Hello")
