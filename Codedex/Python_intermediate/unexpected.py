import unittest
import math

def get_sqrt(n):
    return math.sqrt(n)

def divide(a , b):
    return a / b

class TestUnexpected(unittest.TestCase):
    def test_get_sqrt(self):
        result = get_sqrt(144)
        self.assertEqual(result, 12)

        with self.assertRaises(ValueError):
            result= get_sqrt(-4)
            self.assertEqual(result, ValueError )

    """ Entonces tecnicamente puedo hacer preubas unitarias para ver si regresa
     algún error en caso de que el valor sea negativo o cero, en este caso"""

    def test_divide(self):
        result = divide(144,12)
        self.assertEqual(result, 12)

        with self.assertRaises(ZeroDivisionError):
            result = divide(12,0)
            self.assertEqual(result,ZeroDivisionError)

if __name__ == '__main__':
    unittest.main()