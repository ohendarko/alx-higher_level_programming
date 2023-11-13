import unittest
from models.rectangle import Rectangle


class TestRectangle(unittest.TestCase):
    def setUp(self):
        self.rect = Rectangle(4, 5, 1, 2, 7)

    def test_update_with_args(self):
        self.rect.update(10, 8, 6, 3, 4)
        self.assertEqual(self.rect.id, 10)
        self.assertEqual(self.rect.width, 8)
        self.assertEqual(self.rect.height, 6)
        self.assertEqual(self.rect.x, 3)
        self.assertEqual(self.rect.y, 4)

    def test_update_with_kwargs(self):
        self.rect.update(width=12, y=9, id=11)
        self.assertEqual(self.rect.id, 11)
        self.assertEqual(self.rect.width, 12)
        self.assertEqual(self.rect.height, 5)
        self.assertEqual(self.rect.x, 1)
        self.assertEqual(self.rect.y, 9)


if __name__ == "__main__":
    unittest.main()
