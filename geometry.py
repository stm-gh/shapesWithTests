# area and perimeter for shapes
import math

def area_circle(r):
    return math.pi*(r**2)

def perimeter_circle(r):
    return 2*r*math.pi

def area_rectangle(w,h):
    return w*h

def perimeter_rectangle(w,h):
    return 2*(w+h)

def area_triangle(b,h):
    return 0.5*b*h

def perimeter_triangle(b,h):
    return b+h
    