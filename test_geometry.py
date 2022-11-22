from geometry import Circle, Rectangle, Triangle
import math

def test_area_circle():
    assert Circle().area(2) == 4*math.pi

def test_perimeter_circle():
    assert Circle().perimeter(2) == 4*math.pi

def test_area_triangle():
    assert Triangle().area(3,4) == 6

def test_perimeter_triangle():
    assert Triangle().perimeter(2,3) == 5

def test_area_rectangle():
    assert Rectangle().area(3,4) == 12

def test_perimeter_rectangle():
    assert Rectangle().perimeter(2,3) == 10