import pytest
from ..src.Square import Square


@pytest.mark.parametrize("square_name, square_side", [("test_1", -1), ("test_2", 0)])
def test_square_create_negative(square_name, square_side):
    """ Can't create square with side <= 0"""

    with pytest.raises(ValueError) as ex:
        Square(name=square_name, side=square_side)
    assert str(ex.value) == "Square with given side does not exist"


@pytest.mark.parametrize("square_name, square_side, square_perimeter", [
    ("test_1", 1, 4), ("test_2", 10, 40), ("test_3", 100, 400)
])
def test_square_calculate_perimeter(square_name, square_side, square_perimeter):
    """" Perimeter of square with side 1 equals 4
         Perimeter of square with side 10 equals 40
         Perimeter of square with side 100 equals 400
    """

    square = Square(name=square_name, side=square_side)
    assert square.perimeter == round(square_perimeter, 3)


@pytest.mark.parametrize("square_name, square_side, square_area", [
    ("test_1", 1, 1), ("test_2", 10, 100), ("test_3", 100, 10000)
])
def test_square_calculate_area(square_name, square_side, square_area):
    """" Area of square with sides 1 equals 1
         Area of square with sides 10 equals 100
         Area of square with sides 100 equals 10000
    """

    square = Square(name=square_name, side=square_side)
    assert square.area == round(square_area, 3)
