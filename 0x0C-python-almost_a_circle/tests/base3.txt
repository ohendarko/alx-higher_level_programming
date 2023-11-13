import unittest
from models.rectangle import Rectangle  # Import your Rectangle class

class TestBaseMethods(unittest.TestCase):

    def test_create_with_attributes(self):
        # Test create method with specified attributes
        rectangle_attributes = {'width': 10, 'height': 5, 'x': 2, 'y': 3}
        rectangle_instance = Rectangle.create(**rectangle_attributes)

        self.assertEqual(rectangle_instance.width, 10)
        self.assertEqual(rectangle_instance.height, 5)
        self.assertEqual(rectangle_instance.x, 2)
        self.assertEqual(rectangle_instance.y, 3)

    def test_create_with_empty_attributes(self):
        # Test create method with an empty dictionary
        rectangle_instance = Rectangle.create()

        # Assuming default dummy values (1) for all attributes
        self.assertEqual(rectangle_instance.width, 1)
        self.assertEqual(rectangle_instance.height, 1)
        self.assertEqual(rectangle_instance.x, 1)
        self.assertEqual(rectangle_instance.y, 1)

    def test_create_with_partial_attributes(self):
        # Test create method with only some attributes specified
        rectangle_attributes = {'width': 10, 'height': 5}
        rectangle_instance = Rectangle.create(**rectangle_attributes)

        # Assuming default dummy values (1) for x and y
        self.assertEqual(rectangle_instance.width, 10)
        self.assertEqual(rectangle_instance.height, 5)
        self.assertEqual(rectangle_instance.x, 1)
        self.assertEqual(rectangle_instance.y, 1)

if __name__ == '__main__':
    unittest.main()
