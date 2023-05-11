class user:
    def __init__(self,name,email_address):
        self.name = name
        self.email = email_address
        self.account = BankAccount(int_rate=0.02,balance=0)


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

Azzam = user("Azzam Khames","Azzam.ahmad97@gmail.com")
Azzam.account.deposit(100)
print(Azzam.account.balance)