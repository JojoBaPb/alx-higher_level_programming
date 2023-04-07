import unittest
from max_integer import max_integer

class TestMaxInteger(unittest.TestCase):

    def test_empty_list(self):
        self.assertIsNone(max_integer([]))

    def test_positive_numbers(self):
        self.assertEqual(max_integer([1, 2, 3]), 3)
        self.assertEqual(max_integer([5, 3, 9, 2]), 9)
        self.assertEqual(max_integer([9]), 9)

    def test_negative_numbers(self):
        self.assertEqual(max_integer([-1, -2, -3]), -1)
        self.assertEqual(max_integer([-5, -3, -9, -2]), -2)
        self.assertEqual(max_integer([-9]), -9)

    def test_mixed_numbers(self):
        self.assertEqual(max_integer([-5, 0, 5]), 5)
        self.assertEqual(max_integer([-5, 0, 5, -10, 10]), 10)

    def test_invalid_input(self):
        with self.assertRaises(TypeError):
            max_integer("hello")
        with self.assertRaises(TypeError):
            max_integer([1, 2, "three"])
