import unittest
from core.detector.shape_detector import ShapeDetector
from core.domain.point import Point
from core.domain.figure_type import FigureType


class TestShapeDetector(unittest.TestCase):

    def test_square_valid(self):
        A = Point(0, 0)
        B = Point(1, 0)
        C = Point(1, 1)
        D = Point(0, 1)

        desordenados = [C, A, D, B]

        self.assertTrue(
            ShapeDetector.is_square(desordenados)
        )

    def test_rectangle_valid(self):
        A = Point(0, 0)
        B = Point(3, 0)
        C = Point(3, 1)
        D = Point(0, 1)

        desordenados = [B, D, C, A]

        self.assertTrue(
            ShapeDetector.is_rectangle(desordenados)
        )

    def test_not_square_or_rectangle(self):
        puntos = [
            Point(0, 0),
            Point(2, 0),
            Point(3, 1),
            Point(0, 1)
        ]

        self.assertFalse(ShapeDetector.is_square(puntos))
        self.assertFalse(ShapeDetector.is_rectangle(puntos))

    def test_detect_shapes(self):
        puntos = [
            Point(0, 0),
            Point(1, 0),
            Point(1, 1),
            Point(0, 1),
            Point(3, 3)
        ]

        resultados = ShapeDetector.detect_shapes(puntos)

        self.assertTrue(
            any(fig.type == FigureType.SQUARE for fig in resultados)
        )

    def test_detect_multiple_figures(self):
        puntos = [
            Point(0, 0),
            Point(2, 0),
            Point(2, 2),
            Point(0, 2),  # Cuadrado
            Point(5, 0),
            Point(8, 0),
            Point(8, 2),
            Point(5, 2)   # Rectángulo
        ]

        resultados = ShapeDetector.detect_shapes(puntos)

        self.assertTrue(
            any(fig.type == FigureType.SQUARE for fig in resultados)
        )
        self.assertTrue(
            any(fig.type == FigureType.RECTANGLE for fig in resultados)
        )


if __name__ == '__main__':
    unittest.main()
