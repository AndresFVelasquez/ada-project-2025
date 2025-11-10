from core.figure import Figure

class Rectangle(Figure):
    def __init__(self, points):
        super().__init__(points, name = "Rectangle")

    def calculate_area(self) -> float:
        """Calculate rectangle area."""
        pass

    def is_valid(self) -> bool:
        """Check if points form a valid rectangle."""
        pass