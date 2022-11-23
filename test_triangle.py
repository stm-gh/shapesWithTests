
from geometry import Triangle

# class based testing.
class TestTriangle:
    def test_area(self):
        assert Triangle(3,4).area() == 6

    def test_perimeter(self):
        'something that describes function'
        assert Triangle(2,3).perimeter() == 5