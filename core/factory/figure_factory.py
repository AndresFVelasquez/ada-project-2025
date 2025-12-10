from core.domain.square import Square
from core.domain.rectangle import Rectangle
from core.domain.right_triangle import RightTriangle
from core.domain.acute_triangle import AcuteTriangle
from core.domain.figure_type import FigureType
from core.domain.figure import Figure


class FigureFactory:
    """
    Responsible for creating figure instances based on type.
    Does NOT validate geometry; only instantiates objects.
    """

    @staticmethod
    def create_figure(points: list, figure_type: FigureType) -> Figure:
        """
        Creates and returns a new figure instance based on the provided type.
        Assigns name automatically following the format: Type_consecutive
        """
        if figure_type == FigureType.SQUARE:
            figure = Square(points)

        elif figure_type == FigureType.RECTANGLE:
            figure = Rectangle(points)

        elif figure_type == FigureType.RIGHT_TRIANGLE:
            figure = RightTriangle(points)

        elif figure_type == FigureType.ACUTE_TRIANGLE:
            figure = AcuteTriangle(points)

        else:
            raise ValueError(f"Unsupported FigureType: {figure_type}")

        # Calculate the area before returning the figure
        figure.calculate_area()
        return figure
