import bank_conta
import unittest

class TestBankAccount(unittest.TestCase):
    def test_initial_balace(self):
        cuenta = BankAccount(100)
        self.assertEqual(cuenta.balance, 100)

if __name__ == '__main__':
    unittest.main()