from core.domain.figure import Figure


class Triangle(Figure):
    def __init__(self, name, vertices, num_sides, figure_type):
        super().__init__(name, vertices, num_sides, figure_type)

    def calculate_area(self) -> float:
        """Calculate area using Heron's formula."""
        pass

    def is_valid(self):
        return super().is_valid()

   