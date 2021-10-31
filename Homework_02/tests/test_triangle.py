import pytest
from math import sqrt
from ..src.Triangle import Triangle


@pytest.mark.parametrize("triangle_name, triangle_side_a, triangle_side_b, triangle_side_c", [
    ("test_1", -3, -4, -5), ("test_2", -1, -1, 1), ("test_3", 1, 1, -1),
    ("test_4", 0, 1, 1), ("test_5", 2, 1, 3), ("test_6", 5, 10, 4)
])
def test_triangle_create_negative(triangle_name, triangle_side_a, triangle_side_b, triangle_side_c):
    """ Can't create triangle with one side greater or equal than sum of two other sides """

    with pytest.raises(ValueError) as ex:
        Triangle(name=triangle_name, side_a=triangle_side_a, side_b=triangle_side_b, side_c=triangle_side_c)
    assert str(ex.value) == "Triangle with given sides does not exist"


@pytest.mark.parametrize("triangle_name, triangle_side_a, triangle_side_b, triangle_side_c, triangle_perimeter", [
    ("test_1", 3, 4, 5, 12), ("test_2", 5, 6, 7, 18), ("test_3", 13, 14, 15, 42)
])
def test_triangle_calculate_perimeter(triangle_name, triangle_side_a, triangle_side_b, triangle_side_c,
                                      triangle_perimeter):
    """" Perimeter of triangle with sides 3, 4, 5 equals 12
         Perimeter of triangle with sides 5, 6, 7 equals 18
         Perimeter of triangle with sides 13, 14, 15 equals 42
    """

    triangle = Triangle(name=triangle_name, side_a=triangle_side_a, side_b=triangle_side_b, side_c=triangle_side_c)
    assert triangle.perimeter == round(triangle_perimeter, 3)


@pytest.mark.parametrize("triangle_name, triangle_side_a, triangle_side_b, triangle_side_c, triangle_area", [
    ("test_1", 3, 4, 5, 6), ("test_2", 5, 6, 7, 6 * sqrt(6)), ("test_3", 13, 14, 15, 84)
])
def test_triangle_calculate_area(triangle_name, triangle_side_a, triangle_side_b, triangle_side_c,
                                 triangle_area):
    """" Area of triangle with sides 3, 4, 5 equals 6
         Area of triangle with sides 5, 6, 7 equals 6 * sqrt(6)
         Area of triangle with sides 13, 14, 15 equals 84
    """

    triangle = Triangle(name=triangle_name, side_a=triangle_side_a, side_b=triangle_side_b, side_c=triangle_side_c)
    assert triangle.area == round(triangle_area, 3)
