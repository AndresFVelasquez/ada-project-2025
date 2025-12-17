import json
from core.domain.point import Point
from core.domain.figure import Figure

class DataManager:
    """
    Handles saving and loading points and figures from files.
    """
    
    #Listas de pruebas
    def test_list(self, number):
        lists = [[Point(0, 0), Point(3, 0), Point(0, 4), Point(3, 4)],
                 [Point(3, 20), Point(14, 9), Point(4, 5), Point(3, 2),Point(15, 2), Point(-4, -5), Point(7, -5), Point(24, -5),Point(7, -24)],
                 [Point(1,1), Point(1,5), Point(5,1), Point(1,-2), Point(5,-2)],
                 []
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

    def save_points(self):
        pass  # luego lo implementas

    def load_points(self):
        pass  # luego lo implementas

