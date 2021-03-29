class User:		
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.account_balance = 0
    
    def make_deposit(self, amount):
        self.account_balance += amount
        return self

    def make_withdrawl(self,amount):
        self.account_balance -= amount
        return self
    
    def transfer_money(self,other_user,amount):
        self.account_balance -= amount
        other_user.account_balance +=amount
        return self


user1=User("User 1","user1@gmail.com")
user2=User("User 2","user2@gmail.com")
user3=User("User 3","user3@gmail.com")

user1.make_deposit(1).make_deposit(4).make_deposit(7).make_withdrawl(7).transfer_money(user2,2)
user2.make_deposit(2).make_deposit(4).make_withdrawl(1).make_withdrawl(2)
user3.make_deposit(3).make_withdrawl(2).make_withdrawl(1).make_withdrawl(2)


print(user1.account_balance)
print(user2.account_balance)
print(user3.account_balance)


