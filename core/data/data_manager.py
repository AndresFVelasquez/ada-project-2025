import json
from core.domain.point import Point
from core.domain.figure import Figure


class DataManager:
    """
    Handles saving and loading points and figures from files.
    """

    # Listas de pruebas
    def test_list(self, number):
        lists = [[Point(0, 0), Point(3, 0), Point(0, 4), Point(3, 4)],
                 [Point(3, 20), Point(14, 9), Point(4, 5), Point(3, 2), Point(
                     15, 2), Point(-4, -5), Point(7, -5), Point(24, -5), Point(7, -24)],
                 [Point(1, 1), Point(1, 5), Point(5, 1),
                  Point(1, -2), Point(5, -2)],
                 [Point(2, 1), Point(2, 5), Point(6, 5),
                  Point(6, 1), Point(2, 5), Point(4, 8)]
                 ]

        return lists[number]

    def __init__(self):
        self.points = []
        self.figures = []

    def add_point(self, p):
        if p in self.points:
            return False
        self.points.append(p)
        return True

    def add_points(self, points):

        pass

    def get_points(self):
        return self.points

    def get_figures(self):
        return self.figures

    def save_figures(self, filename: str):
        """
        Guarda la lista de figuras en un archivo JSON con el formato solicitado:
        - identificador (nombre)
        - área
        - conjunto de puntos
        
        Si hay múltiples figuras del mismo tipo, agrega un número secuencial (ej. "Triángulo 1", "Triángulo 2").
        """
        data = []
        name_counters = {}

        for fig in self.figures:
            # Obtener contador actual para este nombre, por defecto 0
            count = name_counters.get(fig.name, 0) + 1
            name_counters[fig.name] = count
            
            # Crear identificador único
            identifier = f"{fig.name} {count}"

            data.append({
                "identifier": identifier,
                "area": fig.area,
                "points": [{"x": p.x, "y": p.y} for p in fig.vertices]
            })
        
        try:
            with open(filename, 'w') as f:
                json.dump(data, f, indent=4)
            return True
        except Exception as e:
            print(f"Error saving figures: {e}")
            return False

    def save_points(self):
        pass  # luego lo implementas

    def load_points(self):
        pass  # luego lo implementas
