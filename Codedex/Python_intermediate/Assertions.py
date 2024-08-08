import unittest

class MyTestCase(unittest.TestCase):
    def test_addition(self):
        result = 2 + 3
        self.assertEqual(result, 5)  

    def test_string_length(self):
        text = 'Hello, World!'
        self.assertEqual(len(text), 13)

    def test_text_contains_word(self):
        text = 'Hello, World!'
        self.assertTrue('Hello' in text)
        self.assertIn('World', text)

if __name__ == '__main__':
    unittest.main()
    