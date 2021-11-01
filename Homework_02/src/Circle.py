from math import pi
from .Figure import Figure


class Circle(Figure):
    def __init__(self, name: str, radius: int | float) -> None:
        if radius > 0:
            self.name = name
            self.radius = radius
        else:
            raise ValueError("Circle with given radius does not exist")

    @property
    def perimeter(self) -> int | float:
        perimeter = 2 * pi * self.radius
        return round(perimeter, 3)

    @property
    def area(self) -> int | float:
        area = pi * (self.radius ** 2)
        return round(area, 3)
