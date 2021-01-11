# OOP:

class Animal:
	def walk(self): ...
	def talk(self):
		print("Hi, I'm ", self.name)

class Dog(Animal):   # <-- can also walk
	def talk(self):  # <-- talks differently (override super method)
		print("Woof woof, I'm ", self.name)


# FP
# ... define Dog a subtype of Animal ...

def talk(a: Animal):
	print("Hi, I'm ", a.name)


def walk(a: Animal):  # <-- can also be called on Dog
	...

def talk(a: Dog):     # <-- dogs talk differently
	print("Woof woof, I'm ", a.name)
