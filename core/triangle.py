from core.figure import Figure


class Triangle(Figure):
    def __init__(self, points):
        super().__init__(points, name = "Triangle")

    def calculate_area(self) -> float:
        """Calculate area using Heron's formula."""
        pass

    def is_valid(self) -> bool:
        """Check if points can form a valid triangle."""
        pass