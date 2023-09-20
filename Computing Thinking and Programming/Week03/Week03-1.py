class Customer:
    def __init__(self, name, balance = 0):
        self.name = name
        self.balance = balance
    
    def withdraw(self, amount):
        self.amount = amount
        if self.amount > self.balance:
            return self.balance
        else:
            self.balance -= self.amount
            return self.balance

    def deposit(self, amount):
        self.amount = amount
        self.balance += self.amount
        return self.balance
    
    def __str__(self):
        return("%s(%s원)" %(self.name, str(self.balance)))
