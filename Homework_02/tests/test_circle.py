import pytest
from math import pi
from ..src.Circle import Circle


@pytest.mark.parametrize("circle_name, circle_radius", [("test_1", -1), ("test_2", 0)])
def test_circle_create_negative(circle_name, circle_radius):
    """ Can't create circle with radius <= 0"""

    with pytest.raises(ValueError) as ex:
        Circle(name=circle_name, radius=circle_radius)
    assert str(ex.value) == "Circle with given radius does not exist"


@pytest.mark.parametrize("circle_name, circle_radius, circle_perimeter", [
    ("test_1", 1, 2 * pi), ("test_2", 10, 20 * pi), ("test_3", 100, 200 * pi)
])
def test_circle_calculate_perimeter(circle_name, circle_radius, circle_perimeter):
    """" Perimeter of circle with radius 1 equals 2 * pi
         Perimeter of circle with radius 10 equals 20 * pi
         Perimeter of circle with radius 100 equals 200 * pi
    """

    circle = Circle(name=circle_name, radius=circle_radius)
    assert circle.perimeter == round(circle_perimeter, 3)


@pytest.mark.parametrize("circle_name, circle_radius, circle_area", [
    ("test_1", 1, pi), ("test_2", 10, 100 * pi), ("test_3", 100, 10000 * pi)
])
def test_circle_calculate_area(circle_name, circle_radius, circle_area):
    """" Area of circle with radius 1 equals pi
         Area of circle with radius 10 equals 100 * pi
         Area of circle with radius 100 equals 10000 * pi
    """

    circle = Circle(name=circle_name, radius=circle_radius)
    assert circle.area == round(circle_area, 3)
