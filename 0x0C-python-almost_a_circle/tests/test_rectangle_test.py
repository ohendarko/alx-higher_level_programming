import unittest
from models.rectangle import Rectangle

class TestRectangle(unittest.TestCase):
    def test_constructor(self):
        rectangle = Rectangle(10, 20, 3, 4, 1)
        self.assertEqual(rectangle.width, 10)
        self.assertEqual(rectangle.height, 20)
        self.assertEqual(rectangle.x, 3)
        self.assertEqual(rectangle.y, 4)
        self.assertEqual(rectangle.id, 1)

    def test_setters(self):
        rectangle = Rectangle(10, 20, 3, 4, 1)

        # Test width setter
        rectangle.width = 15
        self.assertEqual(rectangle.width, 15)

        # Test height setter
        rectangle.height = 25
        self.assertEqual(rectangle.height, 25)

        # Test x setter
        rectangle.x = 5
        self.assertEqual(rectangle.x, 5)

        # Test y setter
        rectangle.y = 6
        self.assertEqual(rectangle.y, 6)

    # Add more test methods as needed

if __name__ == '__main__':
    unittest.main()
