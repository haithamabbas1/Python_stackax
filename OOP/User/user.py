class user:
    def __init__(self, name, year_of_birth, balance=0):
        self.name= name
        self.balance= balance
        self.year_of_birth=year_of_birth

    def make_widthdrawal(self, amount):
        if amount <= self.balance:
            self.balance-=amount
            return True
        return False
    def display_user_balance(self):
        print(f"{self.name} balance is: {self.balance}")
    
    def transfer(self, other, amount):
        if self.make_widthdrawal(amount):
            other.deposite(amount)
            return True
        return False

    def deposite(self, amount):
        self.balance+=amount
    

Tami = user("hani", 1992, 10000)
Sami = user("Sami", 1991)

Tami.make_widthdrawal(1000)
Tami.transfer(Sami, 1000)

Tami.display_user_balance()
Sami.display_user_balance()