import unittest
from core.detector.shape_detector import ShapeDetector
from core.domain.point import Point

class TestShapeDetector(unittest.TestCase):

    def test_square_valid(self):
        """Debe detectar un cuadrado aunque los puntos estén desordenados."""
        A = Point(0, 0)
        B = Point(1, 0)
        C = Point(1, 1)
        D = Point(0, 1)

        desordenados = [C, A, D, B]

        self.assertTrue(
            ShapeDetector.is_square(desordenados),
            "El detector debería reconocer un cuadrado válido."
        )

    def test_rectangle_valid(self):
        """Debe detectar un rectángulo válido incluso con orden aleatorio."""
        A = Point(0, 0)
        B = Point(3, 0)
        C = Point(3, 1)
        D = Point(0, 1)

        desordenados = [B, D, C, A]

        self.assertTrue(
            ShapeDetector.is_rectangle(desordenados),
            "El detector debería reconocer un rectángulo válido."
        )

    def test_not_square_or_rectangle(self):
        """Debe NO detectar cuadrado ni rectángulo si la figura no encaja."""
        puntos = [
            Point(0, 0),
            Point(2, 0),
            Point(3, 1),
            Point(0, 1)
        ]

        self.assertFalse(ShapeDetector.is_square(puntos))
        self.assertFalse(ShapeDetector.is_rectangle(puntos))

    def test_detect_shapes(self):
        """Detecta un cuadrado entre múltiples puntos."""
        puntos = [
            Point(0, 0),
            Point(1, 0),
            Point(1, 1),
            Point(0, 1),
            Point(3, 3)
        ]

        resultados = ShapeDetector.detect_shapes(puntos)

        self.assertIn("Cuadrado", resultados)

    def test_detect_multiple_figures(self):
        """Prueba combinaciones para encontrar múltiples figuras."""
        puntos = [
            Point(0, 0),
            Point(2, 0),
            Point(2, 2),
            Point(0, 2),   # cuadrado
            Point(5, 0),
            Point(8, 0),
            Point(8, 2),
            Point(5, 2)    # rectángulo
        ]

        resultados = ShapeDetector.detect_shapes(puntos)

        self.assertIn("Cuadrado", resultados)
        self.assertIn("Rectángulo", resultados)

if __name__ == '__main__':
    unittest.main()