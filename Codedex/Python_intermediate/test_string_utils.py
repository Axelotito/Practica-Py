import string_utils
import unittest

class TestStringUtils(unittest.TestCase):
    def test_reverse_string(self):
        result = string_utils.reverse_string('hello')
        self.assertEqual(result, 'olleh')
        self.assertTrue(result in 'olleh')	

    def test_capitalized_string(self):
        result = self.string_utils.capitalize_string('hello')
        self.assertEqual(result, 'Hello')
        self.assertTrue(result[0] in 'H')


if __name__ == '__main__':
    unittest.main()