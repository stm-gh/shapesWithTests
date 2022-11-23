import pytest
from geometry import Rectangle

@pytest.fixture
def rectangle1():
    """Fixture to execute asserts before and after a test is run"""
    return Rectangle(3,4)

# class based testing.
class TestRectangle:
    """testing rectangle methods"""
    def test_area(self, rectangle1):
        """testing rectangle area"""
        assert rectangle1.area() == 12

    def test_perimeter(self, rectangle1):
        """testing rectangle perimeter"""
        assert rectangle1.perimeter() == 14