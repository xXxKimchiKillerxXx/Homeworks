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
    
if __name__ == '__main__':
    c1 = Customer('Bill')
    c2 = Customer('Steve', 50000)
    c3 = Customer('Tim', 100000)
    print(c1, c2, c3)

    c1.deposit(50000)
    c2.deposit(30000)
    c3.withdraw(100000)
    print(c1, c2, c3)

    c2.withdraw( 1000000 )
    print(c1, c2, c3)

    print( c3.withdraw(10000), c2.deposit(10000) )
    print(c1, c2, c3)