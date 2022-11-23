from geometry import Circle, Rectangle, Triangle
import math

def test_area_circle():
    testCircle = Circle(2)
    assert testCircle.area() == 4*math.pi

def test_perimeter_circle():
    assert Circle(2).perimeter() == 4*math.pi

def test_area_triangle():
    assert Triangle(3,4).area() == 6

def test_perimeter_triangle():
    'something that describes function'
    assert Triangle(2,3).perimeter() == 5

def test_area_rectangle():
    assert Rectangle(3,4).area() == 12

def test_perimeter_rectangle():
    assert Rectangle(2,3).perimeter() == 10