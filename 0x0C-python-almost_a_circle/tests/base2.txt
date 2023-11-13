import unittest
from models.base import Base

class TestBaseMethods(unittest.TestCase):

    def test_to_json_string(self):
        # Test when list_dictionaries is not empty
        list_dicts = [{'id': 1, 'name': 'Alice'}, {'id': 2, 'name': 'Bob'}]
        result = Base.to_json_string(list_dicts)
        expected_result = '[{"id": 1, "name": "Alice"}, {"id": 2, "name": "Bob"}]'
        self.assertEqual(result, expected_result)

        # Test when list_dictionaries is empty
        result_empty = Base.to_json_string([])
        self.assertEqual(result_empty, '[]')

        # Test when list_dictionaries is None
        result_none = Base.to_json_string(None)
        self.assertEqual(result_none, '[]')

    def test_from_json_string(self):
        # Test when json_string is not empty
        json_string = '[{"id": 1, "name": "Alice"}, {"id": 2, "name": "Bob"}]'
        result = Base.from_json_string(json_string)
        expected_result = [{'id': 1, 'name': 'Alice'}, {'id': 2, 'name': 'Bob'}]
        self.assertEqual(result, expected_result)

        # Test when json_string is empty
        result_empty = Base.from_json_string('')
        self.assertEqual(result_empty, [])

        # Test when json_string is None
        result_none = Base.from_json_string(None)
        self.assertEqual(result_none, [])

if __name__ == '__main__':
    unittest.main()
