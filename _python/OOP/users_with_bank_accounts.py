class User:
    def __init__(self,name,email_address):
        self.name = name
        self.email = email_address
        self.account = BankAccount()

    def make_deposit(self,amount):
        self.account.balance += amount
        return self
    
    def make_withdrawal(self,amount):
        self.account.balance -= amount
        return self
    
    def display_user_balance(self):
        print(f"{self.name}'s balance is: {self.account.balance}")
        return self


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

my_account = BankAccount(0.02,1000)
azzam = User("Azzam Khames","Azzam.ahmad97@gmail.com")
azzam.account = my_account
azzam.make_deposit(100).display_user_balance()
azzam.make_withdrawal(300).display_user_balance()