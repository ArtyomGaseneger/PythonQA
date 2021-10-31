import pytest
from ..src.Rectangle import Rectangle


@pytest.mark.parametrize("rectangle_name, rectangle_side_a, rectangle_side_b", [
    ("test_1", 0, 1), ("test_2", -1, 1), ("test_3", 1, 0), ("test_4", 1, -1)
])
def test_rectangle_create_negative(rectangle_name, rectangle_side_a, rectangle_side_b):
    """ Can't create rectangle with any side <= 0"""

    with pytest.raises(ValueError) as ex:
        Rectangle(name=rectangle_name, side_a=rectangle_side_a, side_b=rectangle_side_b)
    assert str(ex.value) == "Rectangle with given sides does not exist"


@pytest.mark.parametrize("rectangle_name, rectangle_side_a, rectangle_side_b, rectangle_perimeter", [
    ("test_1", 1, 2, 6), ("test_2", 3, 7, 20), ("test_3", 10, 100, 220)
])
def test_rectangle_calculate_perimeter(rectangle_name, rectangle_side_a, rectangle_side_b, rectangle_perimeter):
    """" Perimeter of rectangle with sides 1, 2 equals 6
         Perimeter of rectangle with sides 3, 7 equals 20
         Perimeter of rectangle with sides 10, 100 equals 22
    """

    rectangle = Rectangle(name=rectangle_name, side_a=rectangle_side_a, side_b=rectangle_side_b)
    assert rectangle.perimeter == round(rectangle_perimeter, 3)


@pytest.mark.parametrize("rectangle_name, rectangle_side_a, rectangle_side_b, rectangle_area", [
    ("test_1", 1, 2, 2), ("test_2", 3, 7, 21), ("test_3", 10, 100, 1000)
])
def test_rectangle_calculate_area(rectangle_name, rectangle_side_a, rectangle_side_b, rectangle_area):
    """" Area of rectangle with sides 1, 2 equals 2
         Area of rectangle with sides 3, 7 equals 21
         Area of rectangle with sides 10, 100 equals 1000
    """

    rectangle = Rectangle(name=rectangle_name, side_a=rectangle_side_a, side_b=rectangle_side_b)
    assert rectangle.area == round(rectangle_area, 3)
