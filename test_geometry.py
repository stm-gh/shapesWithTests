from geometry import area_circle, area_rectangle, area_triangle
from geometry import perimeter_circle, perimeter_rectangle, perimeter_triangle
import math

def test_area_circle():
    assert area_circle(2) == 4*math.pi

def test_perimeter_circle():
    assert perimeter_circle(2) == 4*math.pi

def test_area_triangle():
    assert area_triangle(3,4) == 6

def test_perimeter_triangle():
    assert perimeter_triangle(2,3) == 5

def test_area_rectangle():
    assert area_rectangle(3,4) == 12

def test_perimeter_rectangle():
    assert perimeter_rectangle(2,3) == 10