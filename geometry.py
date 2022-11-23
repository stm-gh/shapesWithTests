# area and perimeter for shapes
import math


class Circle:
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi*(self.radius**2)

    def perimeter(self):
        return 2*self.radius*math.pi


class Triangle:
    def __init__(self, base, height):
        self.base = base
        self.height = height

    def area(self):
        return 0.5*self.base*self.height

    def perimeter(self):
        return self.base+self.height


class Rectangle:
    def __init__(self,width,height):
        self.width = width
        self.height = height

    def area(self):
        return self.width*self.height

    def perimeter(self):
        return 2*(self.width+self.height)
