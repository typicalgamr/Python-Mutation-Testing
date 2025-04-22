import unittest
from utils import categorize_age

class TestUtils(unittest.TestCase):
    def test_categorize_age(self):
        self.assertEqual(categorize_age(10), "Child")
        self.assertEqual(categorize_age(15), "Teen")
        self.assertEqual(categorize_age(30), "Adult")
        self.assertEqual(categorize_age(70), "Senior")
        self.assertEqual(categorize_age(13), "Teen")
        self.assertEqual(categorize_age(20), "Adult")

if __name__ == '__main__':
    unittest.main()
