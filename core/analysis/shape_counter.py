from core.domain.figure_type import FigureType
from core.domain.figure import Figure


class ShapeCounter:
    """
    Static class that counts the number of figures per type.
    """
    @staticmethod
    def count_by_type(figures: list) -> dict:
        """
        Returns a dictionary: { FigureType: count }
        Missing categories must appear with count 0.
        """
        counts = {ft: 0 for ft in FigureType}
        for figure in figures:
            if figure.type in counts:
                counts[figure.type] += 1
        return counts