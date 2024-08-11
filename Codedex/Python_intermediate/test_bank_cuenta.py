from bank_conta import BankAccount #tenemos que importar cada clase 
import unittest

class TestBankAccount(unittest.TestCase):
    def test_initial_balace(self):
        cuenta = BankAccount(100)
        self.assertEqual(cuenta.balance, 100)
    
    def test_deposit_zero_amount(self):
        self.assertEqual(self.cuenta.deposit(0), ValueError('Deposit amount must be positive'))

    def test_deposit_positive_amount(self):
        self.cuenta.deposit(50)
        self.assertEqual(self.cuenta.balance, 150)

    def setUp(self):
        self.cuenta = BankAccount(100)

    def tearDown(self):
        self.cuenta = None

if __name__ == '__main__':
    unittest.main()