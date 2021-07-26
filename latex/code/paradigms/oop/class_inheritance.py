class Person:
    def __init__(self, name):
        self.name = name

    def greet(self):
        print(f"Hello, I'm {self.name}")


class Child(Person):
    def __init__(self, name, school):
        super().__init__(name)
        self.school = school

    def learn(self):
        print(f"I'm learning a lot at {self.school}")


c1 = Child("john", "iCSC20")
c1.greet()
c1.learn()
