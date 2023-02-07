class Person:
    def __init__(self, name):
        self.name = name
        pass
    
    def talk(self):
        print(f"Helo, my name is {self.name}")

person1 = Person("Justin")
person1.talk()
print(person1.name)