import pytest
from geometry import Square

@pytest.fixture
def square1():
    """Fixture to execute asserts before and after a test is run"""
    return Square(4)

# class based testing.
class TestSquare:
    """testing square methods"""
    def test_area(self, square1):
        """testing square area"""
        assert square1.area() == 16

    def test_perimeter(self, square1):
        """testing square perimeter"""
        assert square1.perimeter() == 16