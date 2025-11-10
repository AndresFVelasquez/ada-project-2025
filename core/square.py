from core.figure import Figure

class Square(Figure):
    def __init__(self, points):
        super().__init__(points, name = "Square")

    def calculate_area(self) -> float:
        """Calculate square area."""
        pass

    def is_valid(self) -> bool:
        """Check if all sides are equal."""
        pass