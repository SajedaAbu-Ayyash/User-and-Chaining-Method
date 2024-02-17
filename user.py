class User():
    def __init__(self, name, balance):
        self.name = name
        self.balance = balance

    def make_withdrawal(self, amount):
        self.balance -= amount 

    def deposite(self, amount):
        self.balance += amount

    def display_user_balance(self):
        print(f"User: {self.name}, Balance: {self.balance}")

user1 = User("Guido", 1000)
user1.display_user_balance()
user1.make_withdrawal(300)
user1.display_user_balance()
user1.deposite(200)
user1.display_user_balance()
