class BankAccount:
    def __init__(self, int_rate=0, balance=0):
        self.int_rate=int_rate
        self.balance=balance
    def deposit(self, amount):
        self.balance += amount
        return self
    def withdraw(self, amount):
        self.balance += amount
        return self
    def display_account_info(self):
        print(self.balance)
    def yield_interest(self):
        self.balance += self.int_rate * self.balance
        print(self.balance)
        return self

user1=BankAccount(0.02 , 300)
user2=BankAccount(0.03 , 100)

user1.deposit(5).withdraw(10).deposit(20).withdraw(50).yield_interest().display_account_info()
user2.deposit(70).withdraw(30).deposit(100).deposit(35).withdraw(20).yield_interest().display_account_info()
