import unittest
from models.rectangle import Rectangle

class TestRectangle(unittest.TestCase):
    def test_valid_instantiation(self):
        # Test valid instantiation
        rectangle = Rectangle(10, 20, 2, 3, 1)
        self.assertEqual(rectangle.id, 1)
        self.assertEqual(rectangle.width, 10)
        self.assertEqual(rectangle.height, 20)
        self.assertEqual(rectangle.x, 2)
        self.assertEqual(rectangle.y, 3)

    def test_invalid_width(self):
        # Test invalid width (not an integer)
        with self.assertRaises(TypeError):
            rectangle = Rectangle("invalid", 20, 2, 3, 1)

        # Test invalid width (<= 0)
        with self.assertRaises(ValueError):
            rectangle = Rectangle(0, 20, 2, 3, 1)

    def test_invalid_height(self):
        # Test invalid height (not an integer)
        with self.assertRaises(TypeError):
            rectangle = Rectangle(10, "invalid", 2, 3, 1)

        # Test invalid height (<= 0)
        with self.assertRaises(ValueError):
            rectangle = Rectangle(10, 0, 2, 3, 1)

    def test_invalid_x(self):
        # Test invalid x (not an integer)
        with self.assertRaises(TypeError):
            rectangle = Rectangle(10, 20, "invalid", 3, 1)

        # Test invalid x (< 0)
        with self.assertRaises(ValueError):
            rectangle = Rectangle(10, 20, -1, 3, 1)

    def test_invalid_y(self):
        # Test invalid y (not an integer)
        with self.assertRaises(TypeError):
            rectangle = Rectangle(10, 20, 2, "invalid", 1)

        # Test invalid y (< 0)
        with self.assertRaises(ValueError):
            rectangle = Rectangle(10, 20, 2, -1, 1)

if __name__ == '__main__':
    unittest.main()
