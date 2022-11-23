"""area and perimeter for shapes"""

import math
from interface import implements, Interface  # type: ignore


class ShapeInterface(Interface):
    # pylint: disable=W0107 # disables unnecessary pass warning
    """todo"""

    def area(self):
        """todo"""
        pass

    def perimeter(self):
        """todo"""
        pass


class Circle(implements(ShapeInterface)):  # type: ignore
    """todo"""

    def __init__(self, radius: float):
        self.radius = radius

    def area(self):
        """todo"""
        return math.pi * (self.radius**2)

    def perimeter(self):
        """todo"""
        return 2 * self.radius * math.pi


class Triangle(implements(ShapeInterface)):  # type: ignore
    """todo"""

    def __init__(self, base: float, height: float):
        self.base = base
        self.height = height

    def area(self):
        """todo"""
        return 0.5 * self.base * self.height

    def perimeter(self):
        """todo"""
        return self.base + self.height


class Rectangle(implements(ShapeInterface)):  # type: ignore
    """todo"""

    def __init__(self, width: float, height: float):
        self.width = width
        self.height = height

    def area(self):
        """todo"""
        return self.width * self.height

    def perimeter(self):
        """todo"""
        return 2 * (self.width + self.height)


class Square(Rectangle):
    """todo"""

    def __init__(self, side: float):
        super().__init__(side, side)
