from abc import ABC, abstractmethod
from math import pi

class Shape(ABC):
    pass

    @abstractmethod
    def calculate_area(self):
        pass

    @abstractmethod
    def calculate_perimeter(self):
        pass

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def calculate_area(self):
        return pi * self.radius * self.radius

    def calculate_perimeter(self):
        return 2 * pi * self.radius

class Rectangle(Shape):
    def __init__(self, height, width):
        self.height = height
        self.width = width

    def calculate_area(self):
        return self.height * self.width

    def calculate_perimeter(self):
        return  self.height * 2 + self.width * 2

circle = Circle(5)
print(circle.calculate_area())
print(circle.calculate_perimeter())

rectangle = Rectangle(10, 20)
print(rectangle.calculate_area())
print(rectangle.calculate_perimeter())
