# area and perimeter for shapes

# pylint: disable=E0401 # disables interface improperly used warning

import math
from interface import implements, Interface


class ShapeInterface(Interface):
    # pylint: disable=W0107 # disables unnecessary pass warning
    """todo"""
    def area(self):
        """todo"""
        pass

    def perimeter(self):
        """todo"""
        pass


class Circle(implements(ShapeInterface)):
    """todo"""
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        """todo"""
        return math.pi*(self.radius**2)

    def perimeter(self):
        """todo"""
        return 2*self.radius*math.pi


class Triangle(implements(ShapeInterface)):
    """todo"""
    def __init__(self, base, height):
        self.base = base
        self.height = height

    def area(self):
        """todo"""
        return 0.5*self.base*self.height

    def perimeter(self):
        """todo"""
        return self.base+self.height


class Rectangle(implements(ShapeInterface)):
    """todo"""
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        """todo"""
        return self.width*self.height

    def perimeter(self):
        """todo"""
        return 2*(self.width+self.height)

class Square(Rectangle):
    """todo"""
    def __init__(self, side):
        super().__init__(side, side)