import unittest
from models.rectangle import Rectangle


class TestRectangle(unittest.TestCase):
    def setUp(self):
        self.rect = Rectangle(4, 5, 1, 2, 7)

    def test_attributes(self):
        self.assertEqual(self.rect.width, 4)
        self.assertEqual(self.rect.height, 5)
        self.assertEqual(self.rect.x, 1)
        self.assertEqual(self.rect.y, 2)
        self.assertEqual(self.rect.id, 7)

    def test_area(self):
        self.assertEqual(self.rect.area(), 20)

    def test_display(self):
        expected_output = "\n\n    ####\n    ####\n    ####\n    ####\n    ####\n"
        with unittest.mock.patch("sys.stdout", new_callable=io.StringIO) as mock_stdout:
            self.rect.display()
            self.assertEqual(mock_stdout.getvalue(), expected_output)

    def test_str(self):
        self.assertEqual(str(self.rect), "[Rectangle] (7) 1/2 - 4/5")


if __name__ == "__main__":
    unittest.main()
