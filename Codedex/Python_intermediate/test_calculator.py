# Write code below 💖
import unittest


class Calculator:
    def add(self, a, b):
        return a + b

    def subtract(self, a, b):
        return a - b


class TestCalculator(unittest.TestCase):

    def setUp(self):
        self.calculator = Calculator()

    def tearDown(self):
        self.calculator = None

    def test_addition(self):
        self.assertEqual(self.calculator.subtract(10, 4), 6)

    def test_subtraction(self):
        self.assertEqual(self.calculator.subtract(10, 4), 6)


if __name__ == "__main__":
    unittest.main()
