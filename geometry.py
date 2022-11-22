# area and perimeter for shapes
import math

class Circle:
    def area(self,r):
        return math.pi*(r**2)

    def perimeter(self,r):
        return 2*r*math.pi

class Rectangle:
    def area(self,w,h):
        return w*h

    def perimeter(self,w,h):
        return 2*(w+h)

class Triangle:
    def area(self,b,h):
        return 0.5*b*h

    def perimeter(self,b,h):
        return b+h
