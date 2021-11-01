import pytest
from ..src.Circle import Circle
from ..src.Rectangle import Rectangle
from ..src.Square import Square
from ..src.Triangle import Triangle


class X:
    pass


figures = [
    Circle(name="circle_1", radius=1),
    Circle(name="circle_2", radius=2),
    Rectangle(name="rectangle", side_a=3, side_b=4),
    Square(name="square", side=5),
    Triangle(name="triangle", side_a=6, side_b=8, side_c=10)
]


def id_func(elem_list):
    return [elem.name for elem in elem_list]


@pytest.fixture(params=figures, ids=id_func(figures))
def figure(request):
    return request.param


def test_add_area_negative(figure):
    """Can't add area if added object is not inherited from class Figure"""

    x = X()
    with pytest.raises(ValueError) as ex:
        figure.add_area(x)
    assert str(ex.value) == "Can not add areas - given argument has incorrect class"


def test_add_area_total():
    """Areas of different figures can be added in pairs for calculation of total area """

    num_figures = len(figures)
    if num_figures % 2 == 0:
        start = 0
        area_add = 0
        area_sum = 0
    else:
        start = 1
        area_add = figures[0].area
        area_sum = figures[0].area
    for i in range(start, num_figures, 2):
        area_add += figures[i].add_area(figures[i + 1])
        area_sum += figures[i].area + figures[i + 1].area

    assert area_add == area_sum
