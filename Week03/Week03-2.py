class Pet:
    def __init__(self, name, age):
        self.name = name
        self.age = float(age)

    def human_age(self):
        return self.age * 4
    
    def __str__(self):
        return self.name

class Dog(Pet):
    def bark(self, n):
        return print("bark!\n" * n)

class Cat(Pet):
    def meow(self, n):
        return print("meow~\n" * n)