from math import pi


class Rectangle:

    def __init__(self, sideA=0, sideB=0):
        self.sideA = sideA
        self.sideB = sideB

    def get_area(self):
        return self.sideA * self.sideB

    def get_perimeter(self):
        return 2 * (self.sideA + self.sideB)


class Circle:

    def __init__(self, radius=0):
        self.radius = radius

    def get_area(self):
        return pi * (self.radius ** 2)

    def get_perimeter(self):
        return 2 * pi * self.radius


circle = Circle(radius=5)

print(circle.get_area(), circle.get_perimeter())
