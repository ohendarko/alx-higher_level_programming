"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    """uniitest for max_integer"""
    def test_maxinteger(self):
        """test for max int"""
        self.assertEqual(max_integer([1, 2, 3, 4]), 4)
        self.assertEqual(max_integer([1, 3, 4, 2]), 4)
        self.assertEqual(max_integer([-100, -12, 3, 4]), 4)
        self.assertEqual(max_integer([100, -12, 3, 4]), 100)
        self.assertEqual(max_integer([1, 20, 3.8, -4.2]), 20)
        self.assertEqual(max_integer([4]), 4)
        self.assertEqual(max_integer([]), None)


if __name__ == '__main__':
    unittest.main()
