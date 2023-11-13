import unittest
from models.rectangle import Rectangle
from io import StringIO
from unittest.mock import patch

class TestRectangle(unittest.TestCase):

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_init(self):
        # Test case for the constructor (__init__)
        rectangle = Rectangle(4, 5, 1, 2, 10)
        self.assertEqual(rectangle.width, 4)
        self.assertEqual(rectangle.height, 5)
        self.assertEqual(rectangle.x, 1)
        self.assertEqual(rectangle.y, 2)
        self.assertEqual(rectangle.id, 10)

    def test_area(self):
        # Test case for the area method
        rectangle = Rectangle(4, 5)
        self.assertEqual(rectangle.area(), 20)

    def test_display(self):
        # Test case for the display method
        rectangle = Rectangle(3, 2)
        expected_output = "###\n" \
                          "###\n"
        with patch('sys.stdout', new_callable=StringIO) as mock_stdout:
            rectangle.display()
            self.assertEqual(mock_stdout.getvalue(), expected_output)

    def test_str(self):
        # Test case for the __str__ method
        rectangle = Rectangle(4, 5, 1, 2, 10)
        self.assertEqual(str(rectangle), "[Rectangle] (10) 1/2 - 4/5")

    def test_update(self):
        # Test case for the update method
        rectangle = Rectangle(4, 5, 1, 2, 10)
        rectangle.update(20, 6, 7, 8, 9)
        self.assertEqual(rectangle.id, 20)
        self.assertEqual(rectangle.width, 6)
        self.assertEqual(rectangle.height, 7)
        self.assertEqual(rectangle.x, 8)
        self.assertEqual(rectangle.y, 9)

    def test_to_dictionary(self):
        # Test case for the to_dictionary method
        rectangle = Rectangle(4, 5, 1, 2, 10)
        expected_dict = {'id': 10, 'width': 4, 'height': 5, 'x': 1, 'y': 2}
        self.assertEqual(rectangle.to_dictionary(), expected_dict)

if __name__ == '__main__':
    unittest.main()
