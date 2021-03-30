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

class User:		
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.account = BankAccount(int_rate=0.02 , balance=0)
        print(self.account.balance)
    def make_deposit(self, amount):
        self.account.deposit(100)
        print(self.account.balance)
    def make_withdrawl(self,amount):
        self.account.withdraw(20)
        print(self.account.balance)
    def transfer_money(self,other_user,amount):
        self.account.withdraw(30)
        other_user.account.deposit(30)

user1=User("Mario" , "mariohysaj@gmail.com")
print(23)
print(user1.account.balance)