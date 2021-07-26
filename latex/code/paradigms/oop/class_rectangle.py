class Rectangle:
    def __init__(self, width, height):  # <-- constructor
        # 'self' represents the instance of the class
        self.width = width              # <-- attribute = internal variable
        self.height = height

    def calculate_area(self):           # <-- method (function of class)
        return self.width * self.height


r1 = Rectangle(1, 2)         # <-- object (instance of the class)
print(r1.calculate_area())   # <-- call method of object
print(r1.width)              # <-- get attribute of object
r1.width = 5                 # <-- set attribute of object
