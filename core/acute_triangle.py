from core.triangle import Triangle


class Acute_Triangle(Triangle):
    def __init__(self, points):
        super().__init__(points, name = "Acute Triangle")