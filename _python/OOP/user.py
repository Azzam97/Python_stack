class user:
    def __init__(self,name,balance=0):
        self.name = name
        self.balance = balance
    def make_deposit(self,amount):
        self.balance += amount
        return self
    def make_withdrawal(self,amount):
        self.balance -= amount
        return self
    def display_user_balance(self):
        print(self.name,self.balance)
    def transfer_money(self,other_user,amount):
        self.balance -= amount
        other_user.balance += amount

Azzam = user("Azzam Ahmad")
Islam = user("Islam Minawi")
Ammar = user("Ammar Abu Baker")
Azzam.make_deposit(100).make_deposit(100).make_deposit(100).make_withdrawal(100).display_user_balance()
Islam.make_deposit(500).make_deposit(1000).make_withdrawal(300).make_withdrawal(600).display_user_balance()
Ammar.make_deposit(3000).make_withdrawal(500).make_withdrawal(900).make_withdrawal(1000).display_user_balance()
Azzam.transfer_money(Islam,500)
Islam.display_user_balance()