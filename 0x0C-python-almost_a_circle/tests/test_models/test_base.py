import unittest
import os
from models.base import Base, Rectangle

class TestBase(unittest.TestCase):

    def setUp(self):
        # Optional: Set up any common resources or configurations needed for the tests
        pass

    def tearDown(self):
        # Optional: Clean up after each test
        pass

    def test_to_json_string(self):
        # Test case for to_json_string
        obj_list = [Rectangle(1, 2, 3), Rectangle(4, 5, 6)]
        json_str = Base.to_json_string([obj.to_dictionary() for obj in obj_list])
        expected = '[{"id": 1, "width": 1, "height": 2, "x": 3, "y": 0},' \
                   '{"id": 2, "width": 4, "height": 5, "x": 6, "y": 0}]'
        self.assertEqual(json_str, expected)

    def test_from_json_string(self):
        # Test case for from_json_string
        json_str = '[{"id": 1, "width": 1, "height": 2, "x": 3, "y": 0},' \
                   '{"id": 2, "width": 4, "height": 5, "x": 6, "y": 0}]'
        obj_list = Base.from_json_string(json_str)
        self.assertEqual(len(obj_list), 2)
        self.assertIsInstance(obj_list[0], Rectangle)
        self.assertEqual(obj_list[0].width, 1)
        self.assertEqual(obj_list[1].height, 5)

    # Add similar test methods for create, save_to_file, load_from_file, save_to_file_csv, load_from_file_csv

if __name__ == '__main__':
    unittest.main()
