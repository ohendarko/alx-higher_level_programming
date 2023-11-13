import unittest
from models.rectangle import Rectangle

class TestRectangle(unittest.TestCase):
    def test_str_representation(self):
        rectangle = Rectangle(5, 10, 2, 3, 1)
        self.assertEqual(str(rectangle), "[Rectangle] (1) 2/3 - 5/10")

    def test_area_calculation(self):
        rectangle = Rectangle(5, 10)
        self.assertEqual(rectangle.area(), 50)

    def test_validations(self):
        with self.assertRaises(TypeError):
            Rectangle("invalid", 10, 2, 3)

        with self.assertRaises(ValueError):
            Rectangle(0, 10, 2, 3)

        with self.assertRaises(ValueError):
            Rectangle(5, -10, 2, 3)

        with self.assertRaises(ValueError):
            Rectangle(5, 10, -2, 3)

    def test_default_values(self):
        rectangle = Rectangle(5, 10)
        self.assertEqual(rectangle.x, 0)
        self.assertEqual(rectangle.y, 0)
        self.assertIsNone(rectangle.id)

if __name__ == "__main__":
    unittest.main()
