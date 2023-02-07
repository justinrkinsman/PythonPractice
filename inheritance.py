class Mammal:
    def walk(self):
        print("walk")


class Dog(Mammal):
    def bark(self):
        print("bark")
        

class Cat(Mammal):
    def meow(self):
        print("meow")


kitty = Cat()
kitty.walk()
kitty.meow()

dog1 = Dog()
dog1.walk()
dog1.bark()