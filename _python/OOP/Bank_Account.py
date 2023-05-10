class BankAccount:
    def __init__(self, int_rate=0.02, balance=0):
        self.int_rate = int_rate
        self.balance = balance
    def deposit(self, amount):
        self.balance += amount
        return self
    def withdraw(self, amount):
        self.balance -= amount
        return self
    def display_account_info(self):
        print ("Balance: ", self.interest_yield)
        return self
    def yield_interest(self):
        self.interest_yield = (self.int_rate * self.balance) + self.balance
        return self

Account1 = BankAccount(0.02,0)
Account2 = BankAccount(0.02, 500)
Account1.deposit(100).deposit(100).deposit(100).withdraw(100).yield_interest().display_account_info()
Account2.deposit(100).deposit(100).withdraw(50).withdraw(100).withdraw(150).withdraw(30).yield_interest().display_account_info()