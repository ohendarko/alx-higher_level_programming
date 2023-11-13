import unittest
from models.square import Square
from io import StringIO
from unittest.mock import patch

class TestSquare(unittest.TestCase):

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_init(self):
        # Test case for the constructor (__init__)
        square = Square(5, 1, 2, 10)
        self.assertEqual(square.size, 5)
        self.assertEqual(square.x, 1)
        self.assertEqual(square.y, 2)
        self.assertEqual(square.id, 10)

    def test_size_property(self):
        # Test case for the size property and setter
        square = Square(3)
        square.size = 7
        self.assertEqual(square.size, 7)
        self.assertEqual(square.width, 7)
        self.assertEqual(square.height, 7)

    def test_update(self):
        # Test case for the update method
        square = Square(4, 1, 2, 10)
        square.update(20, 6, 8, 9)
        self.assertEqual(square.id, 20)
        self.assertEqual(square.size, 6)
        self.assertEqual(square.x, 8)
        self.assertEqual(square.y, 9)

    def test_str(self):
        # Test case for the __str__ method
        square = Square(5, 1, 2, 10)
        self.assertEqual(str(square), "[Square] (10) 1/2 - 5")

    def test_to_dictionary(self):
        # Test case for the to_dictionary method
        square = Square(4, 1, 2, 10)
        expected_dict = {'id': 10, 'size': 4, 'x': 1, 'y': 2}
        self.assertEqual(square.to_dictionary(), expected_dict)

    def test_to_csv_row(self):
        # Test case for the to_csv_row method
        square = Square(3, 2, 1, 5)
        expected_row = [5, 3, 2, 1]
        self.assertEqual(square.to_csv_row(), expected_row)

    def test_create_from_csv_row(self):
        # Test case for the create_from_csv_row method
        row = [5, 3, 2, 1]
        square = Square.create_from_csv_row(row)
        self.assertEqual(square.id, 5)
        self.assertEqual(square.size, 3)
        self.assertEqual(square.x, 2)
        self.assertEqual(square.y, 1)

if __name__ == '__main__':
    unittest.main()
