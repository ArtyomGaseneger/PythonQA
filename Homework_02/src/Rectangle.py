from Homework_02.src.Figure import Figure


class Rectangle(Figure):
    def __init__(self, name: str, side_a: int | float, side_b: int | float) -> None:
        if (side_a <= 0) or (side_b <= 0):
            raise ValueError("Rectangle with given sides does not exist")
        self.name = name
        self.side_a = side_a
        self.side_b = side_b

    @property
    def perimeter(self) -> int | float:
        perimeter = 2 * (self.side_a + self.side_b)
        return round(perimeter, 3)

    @property
    def area(self) -> int | float:
        area = self.side_a * self.side_b
        return round(area, 3)
