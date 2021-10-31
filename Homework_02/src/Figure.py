class Figure:
    name = None

    @property
    def perimeter(self):
        raise NotImplementedError("Property perimeter is not implemented")

    @property
    def area(self):
        raise NotImplementedError("Property area is not implemented")

    def add_area(self, other) -> int | float:
        if not isinstance(other, Figure):
            raise ValueError("Can not add areas - given argument has incorrect class")
        return self.area + other.area
