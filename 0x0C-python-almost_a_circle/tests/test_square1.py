import unittest
from models.square import Square

class TestSquare(unittest.TestCase):
    def test_update_method(self):
        square = Square(5, 2, 3, 1)
        square.update(7, 10, 4, 5)
        self.assertEqual(square.to_dictionary(), {"id": 7, "size": 10, "x": 4, "y": 5})

        square.update(size=8, x=1, y=2)
        self.assertEqual(square.to_dictionary(), {"id": 7, "size": 8, "x": 1, "y": 2})

        square.update(3)
        self.assertEqual(square.to_dictionary(), {"id": 3, "size": 8, "x": 1, "y": 2})

        # Add more test cases as needed

if __name__ == "__main__":
    unittest.main()
