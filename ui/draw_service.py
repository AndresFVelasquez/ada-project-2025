from core.point import Point
from core.figure import Figure

class DrawService:
    """
    Handles all visual drawing (e.g., console or graphical).
    """
    def __init__(self):
        self.points: list[Point] = []

    def draw_points(self):
        """Draw points on a Cartesian plane."""
        pass

    def draw_figures(self, figures: list[Figure]):
        """Draw all detected figures."""
        pass

    def draw_cartesian_plane(self):
        """Render a simple coordinate grid."""
        pass