from core.triangle import Triangle


class Right_Triangle(Triangle):
    def __init__(self, points):
        super().__init__(points, name = "Right Triangle")

    def is_valid(self) -> bool:
        """Check if it’s a right triangle (Pythagoras theorem)."""
        pass