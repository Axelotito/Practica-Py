class BankAccount:
    balance = 0
    def __init__(self, initial_balance=0):
        self.balance = initial_balance

    def deposit(self, amount):
        if amount <= 0:
            #raise regresa un mensaje de error si el valor es negativo 
            raise ValueError('Deposit amount must be positive')
        self.balance += amount
        return self.balance

    def withdraw(self, amount):
        if amount <=0:
            raise ValueError('Withdrawal amount must be positive')
        elif amount > self.balance:
            raise ValueError('Insufficient funds')
        self.balance -= amount
