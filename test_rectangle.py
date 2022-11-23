
from geometry import Rectangle

# class based testing.
class TestRectangle:
    def test_area(self):
        assert Rectangle(3,4).area() == 12

    def test_perimeter(self):
        assert Rectangle(2,3).perimeter() == 10