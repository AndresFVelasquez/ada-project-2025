from core.domain.figure import Figure

class Square(Figure):
    def __init__(self, name, vertices, num_sides, figure_type):
        super().__init__(name, vertices, num_sides, figure_type)

    def calculate_area(self) -> float:
        """Calculate square."""
        pass

    def is_valid(self):
        return super().is_valid()
