from core.domain.triangle import Triangle


class AcuteTriangle(Triangle):
    def __init__(self, name, vertices, num_sides, figure_type):
        super().__init__(name, vertices, num_sides, figure_type)

    def calculate_area(self):
        return super().calculate_area()
    
    def is_valid(self):
        return super().is_valid()

    