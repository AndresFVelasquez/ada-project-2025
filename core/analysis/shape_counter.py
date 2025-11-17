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
        pass