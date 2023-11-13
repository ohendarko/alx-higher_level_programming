import unittest
from models.rectangle import Rectangle

class TestRectangle(unittest.TestCase):
    def test_init(self):
        rectangle = Rectangle(10, 20, 5, 8, 1)
        self.assertEqual(rectangle.width, 10)
        self.assertEqual(rectangle.height, 20)
        self.assertEqual(rectangle.x, 5)
        self.assertEqual(rectangle.y, 8)
        self.assertEqual(rectangle.id, 1)

    def test_area(self):
        rectangle = Rectangle(5, 10)
        self.assertEqual(rectangle.area(), 50)

    def test_display(self):
        rectangle = Rectangle(3, 2)
        expected_output = "###\n###\n"
        with unittest.mock.patch('sys.stdout', new_callable=io.StringIO) as mock_stdout:
            rectangle.display()
            self.assertEqual(mock_stdout.getvalue(), expected_output)

    def test_str(self):
        rectangle = Rectangle(4, 5, 2, 1, 7)
        expected_str = "[Rectangle] (7) 2/1 - 4/5"
        self.assertEqual(str(rectangle), expected_str)

    def test_to_dictionary(self):
        rectangle = Rectangle(3, 4, 1, 2, 10)
        expected_dict = {'id': 10, 'width': 3, 'height': 4, 'x': 1, 'y': 2}
        self.assertEqual(rectangle.to_dictionary(), expected_dict)

if __name__ == '__main__':
    unittest.main()
