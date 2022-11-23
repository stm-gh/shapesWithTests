from geometry import Circle
import math

# class based testing.
class TestCircle:
    def test_area(self):
        testCircle = Circle(2)
        assert testCircle.area() == 4*math.pi
    
    def test_perimeter(self):
        assert Circle(2).perimeter() == 4*math.pi
    