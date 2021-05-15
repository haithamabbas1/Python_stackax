class bank_account:
    def __init__(self, ir=0.01, balance=0):
        self.balance = balance
        self.ir = ir
        
    def deposite(self, amount):
        self.balance+=amount

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance-=amount
            return True
        else:
            print("insufficient funds, charged a fee of 5")
            self.balance-= 5
            return false
    def display_account(self):
        print(f"balance: {self.balance}")

    def yield_intrest(self):
        self.balance += self.ir * self.balance

account= bank_account()
account.deposite(10000)
account.yield_intrest()
account.display_account()
