from math import sqrt
from Homework_02.src.Figure import Figure


class Triangle(Figure):
    def __init__(self, name: str, side_a: int | float, side_b: int | float, side_c: int | float) -> None:
        x, y, z = sorted([side_a, side_b, side_c])
        if z >= x + y:
            raise ValueError("Triangle with given sides does not exist")
        self.name = name
        self.side_a = side_a
        self.side_b = side_b
        self.side_c = side_c

    @property
    def perimeter(self) -> int | float:
        perimeter = self.side_a + self.side_b + self.side_c
        return round(perimeter, 3)

    @property
    def area(self) -> int | float:
        area = sqrt(self.perimeter * (self.perimeter - 2 * self.side_a) * (self.perimeter - 2 * self.side_b) *
                    (self.perimeter - 2 * self.side_c))/4
        if area.is_integer():
            return int(area)
        else:
            return round(area, 3)
