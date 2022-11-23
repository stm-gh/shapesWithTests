import pytest
from geometry import Triangle

@pytest.fixture
def triangle1():
    """Fixture to execute asserts before and after a test is run"""
    return Triangle(3,4)

# class based testing.
class TestTriangle:
    """testing triangle methods"""
    def test_area(self, triangle1):
        """testing area"""
        assert triangle1.area() == 6

    def test_perimeter(self, triangle1):
        """testing perimeter"""
        assert triangle1.perimeter() == 7