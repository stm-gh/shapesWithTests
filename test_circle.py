import math
import pytest
from geometry import Circle

@pytest.fixture
def circle1():
    """Fixture to execute asserts before and after a test is run"""
    return Circle(2)

class TestCircle:
    """testing circle methods"""
    def test_area(self, circle1):
        """testing area of circle"""
        assert circle1.area() == 4*math.pi
    
    def test_perimeter(self, circle1):
        """testing perimeter of circle"""
        assert circle1.perimeter() == 4*math.pi
    
