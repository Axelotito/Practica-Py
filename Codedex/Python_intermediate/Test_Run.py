import unittest

def add(a, b):
    return a+b

class TestAddition(unittest.TestCase):
    #define the first unit test
    def test_add(self):
        result = add(3, 4)

        #define the expected result
        expected_result = 7
        self.assertEqual(result, expected_result)

if __name__ == '__main__':
    unittest.main() 