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