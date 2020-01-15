from abc import ABC, abstractmethod


class Shape(ABC):
    @abstractmethod
    def calculate_area(self):
        pass
    
    @abstractmethod
    def draw(self):
        pass


class Rectangle(Shape):
    def __init__(self, ...):
        ...

    def calculate_area(self):
        # concrete implementation here
