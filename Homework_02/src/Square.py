from Homework_02.src.Rectangle import Rectangle


class Square(Rectangle):
    def __init__(self, name: str, side: int | float) -> None:
        if side <= 0:
            raise ValueError("Square with given side does not exist")
        super().__init__(name=name, side_a=side, side_b=side)
