import unittest
from models.base import Base

class TestBase(unittest.TestCase):
    def test_id_incrementation(self):
        obj1 = Base()
        obj2 = Base()

        self.assertEqual(obj1.id, 1)
        self.assertEqual(obj2.id, 2)

    def test_custom_id(self):
        obj = Base(100)
        self.assertEqual(obj.id, 100)

if __name__ == '__main__':
    unittest.main()
