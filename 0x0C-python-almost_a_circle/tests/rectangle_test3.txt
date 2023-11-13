import unittest
from models.rectangle import Rectangle

class TestRectangle(unittest.TestCase):
    def test_area(self):
        # Test case 1
        rect1 = Rectangle(5, 10)
        self.assertEqual(rect1.area(), 50, "Area calculation is incorrect for rect1")

        # Test case 2
        rect2 = Rectangle(3, 7)
        self.assertEqual(rect2.area(), 21, "Area calculation is incorrect for rect2")

        # Test case 3
        rect3 = Rectangle(0, 0)
        self.assertEqual(rect3.area(), 0, "Area calculation is incorrect for rect3")

    def test_validations(self):
        # Test case 1: Negative width
        with self.assertRaises(ValueError):
            rect = Rectangle(-5, 10)

        # Test case 2: Non-integer width
        with self.assertRaises(TypeError):
            rect = Rectangle("5", 10)

        # Test case 3: Negative height
        with self.assertRaises(ValueError):
            rect = Rectangle(5, -10)

        # Test case 4: Non-integer height
        with self.assertRaises(TypeError):
            rect = Rectangle(5, "10")

        # Test case 5: Negative x
        with self.assertRaises(ValueError):
            rect = Rectangle(5, 10, -2)

        # Test case 6: Non-integer x
        with self.assertRaises(TypeError):
            rect = Rectangle(5, 10, "2")

        # Test case 7: Negative y
        with self.assertRaises(ValueError):
            rect = Rectangle(5, 10, 2, -3)

        # Test case 8: Non-integer y
        with self.assertRaises(TypeError):
            rect = Rectangle(5, 10, 2, "3")

if __name__ == "__main__":
    unittest.main()
