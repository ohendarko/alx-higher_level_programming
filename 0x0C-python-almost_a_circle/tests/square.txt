import unittest
from models.square import Square

class TestSquare(unittest.TestCase):
    def setUp(self):
        self.square = Square(4, 1, 2, 7)

    def test_attributes(self):
        self.assertEqual(self.square.size, 4)
        self.assertEqual(self.square.width, 4)
        self.assertEqual(self.square.height, 4)
        self.assertEqual(self.square.x, 1)
        self.assertEqual(self.square.y, 2)
        self.assertEqual(self.square.id, 7)

    def test_size_setter(self):
        self.square.size = 6
        self.assertEqual(self.square.size, 6)
        self.assertEqual(self.square.width, 6)
        self.assertEqual(self.square.height, 6)

        with self.assertRaises(ValueError) as cm:
            self.square.size = -3
        self.assertEqual(str(cm.exception), "width must be > 0")

        with self.assertRaises(TypeError) as cm:
            self.square.size = "invalid"
        self.assertEqual(str(cm.exception), "width must be an integer")

    def test_str_method(self):
        self.assertEqual(str(self.square), "[Square] (7) 1/2 - 4")

    # Add more test cases as needed

if __name__ == "__main__":
    unittest.main()
