import unittest
from models.square import Square

class TestSquare(unittest.TestCase):
    def setUp(self):
        self.square = Square(4, 1, 2, 7)

    def test_str_representation(self):
        self.assertEqual(str(self.square), "[Square] (7) 1/2 - 4")

    def test_size_attribute(self):
        self.assertEqual(self.square.size, 4)

    def test_update_with_size(self):
        self.square.update(size=8)
        self.assertEqual(self.square.size, 8)
        self.assertEqual(self.square.width, 8)
        self.assertEqual(self.square.height, 8)

if __name__ == "__main__":
    unittest.main()
