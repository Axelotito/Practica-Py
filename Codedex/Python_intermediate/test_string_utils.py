import string_utils
import unittest

""" para hacer una prueba unitaria necesitas importar 
unittest y crear una clase que herede de unittest.TestCase"""

class TestStringUtils(unittest.TestCase):
    def test_reverse_string(self):
        result = string_utils.reverse_string('hello')
        self.assertEqual(result, 'olleh')
        self.assertTrue(result in 'olleh')	

    def test_capitalized_string(self):
        result = string_utils.capitalize_string('hello')
        self.assertEqual(result, 'Hello')
        self.assertTrue(result[0] in 'H')

    def test_is_capitalized(self):
        result = string_utils.is_capitalized('Hello')
        self.assertTrue(result, True)

if __name__ == '__main__':
    unittest.main()