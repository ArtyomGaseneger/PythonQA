from .Figure import Figure


class Square(Figure):
    def __init__(self, name: str, side: int | float) -> None:
        if side > 0:
            self.name = name
            self.side = side
        else:
            raise ValueError("Square with given side does not exist")

    @property
    def perimeter(self) -> int | float:
        perimeter = 4 * self.side
        return round(perimeter, 3)

    @property
    def area(self) -> int | float:
        area = self.side ** 2
        return round(area, 3)
