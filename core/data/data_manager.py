import json
from core.domain.point import Point
from core.domain.figure import Figure

class DataManager:
    """
    Handles saving and loading points and figures from files.
    """
    def __init__(self):
        self.points = []
        self.figures = []

    def add_point(self, p):
        if p in self.points:
            return False
        self.points.append(p)
        return True

    def get_points(self):
        return self.points

    def get_figures(self):
        return self.figures

    def save_points(self):
        pass  # luego lo implementas

    def load_points(self):
        pass  # luego lo implementas

