import unittest
from models.rectangle import Rectangle
from models.base import Base

class TestBaseMethods(unittest.TestCase):
    def test_save_to_file(self):
        # Create instances of Rectangle for testing
        r1 = Rectangle(10, 7, 2, 8)
        r2 = Rectangle(2, 4)

        # Save instances to file
        Rectangle.save_to_file([r1, r2])

        # Read the file content
        with open("Rectangle.json", "r") as file:
            content = file.read()

        # Convert the JSON content back to a list of dictionaries
        loaded_data = Base.from_json_string(content)

        # Check if the loaded data matches the original data
        self.assertEqual(len(loaded_data), 2)
        self.assertEqual(loaded_data[0]["width"], r1.width)
        self.assertEqual(loaded_data[1]["height"], r2.height)

if __name__ == '__main__':
    unittest.main()
