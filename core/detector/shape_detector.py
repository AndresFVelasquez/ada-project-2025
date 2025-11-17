from core.domain.point import Point
from core.factory.figure_factory import FigureFactory
from core.domain.figure_type import FigureType

class ShapeDetector:
    """
    Static class responsible for detecting geometric shapes from
    combinations of 3 and 4 points.
    """


    @staticmethod
    def detect_shapes(point_list: list) -> list:
        """
        Given a list of points, generate all combinations and detect valid
        geometric figures. Returns a list of Figure objects.
        """
        pass


    @staticmethod
    def combine_three_points(points: list) -> list:
        """Generate all combinations of 3 points."""
        pass


    @staticmethod
    def combine_four_points(points: list) -> list:
        """Generate all combinations of 4 points."""
        pass


    @staticmethod
    def is_square(points: list) -> bool:
        """Return True if the 4 points form a valid square."""
        pass


    @staticmethod
    def is_rectangle(points: list) -> bool:
        """Return True if the 4 points form a valid rectangle."""
        pass


    @staticmethod
    def is_right_triangle(points: list) -> bool:
        """Return True if the 3 points form a right triangle."""
        pass


    @staticmethod
    def is_acute_triangle(points: list) -> bool:
        """Return True if the 3 points form an acute triangle."""
        pass