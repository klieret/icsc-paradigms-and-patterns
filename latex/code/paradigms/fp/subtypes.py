# OOP:

class Animal:
	def walk(self): ...
	def talk(self):
		print("Hi, I'm ", self.name)

class Dog(Animal):   # <-- can also walk
	def talk(self):  # <-- talks differently (override super method)
		print("Woof woof, I'm ", self.name)


# FP (not actual python code):
# ... define Dog a subtype of Animal ...

def talk(Animal a):
	print("Hi, I'm ", a.name)


def walk(Animal a):  # <-- can also be called on Dog
	...

def talk(Dog a):     # <-- dogs talk differently
	print("Woof woof, I'm ", a.name)
