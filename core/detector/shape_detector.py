import math
from core.domain.point import Point
from core.factory.figure_factory import FigureFactory
from core.domain.figure_type import FigureType


class ShapeDetector:
    """
    Static class responsible for detecting geometric shapes from
    combinations of 3 and 4 points.
    """

    # ----------------------------------------------------
    # MÉTODOS PRINCIPALES
    # ----------------------------------------------------
    @staticmethod
    def detect_shapes(point_list: list) -> list:
        """
        Given a list of points, generate all combinations and detect valid
        geometric figures. Returns a list of Figure objects.
        """
        figures = []

        # 1. Generar combinaciones de 3 puntos (triángulos)
        tri_combinations = ShapeDetector.combine_three_points(point_list)

        for combo in tri_combinations:
            if ShapeDetector.is_right_triangle(combo):
                normalized = ShapeDetector.normalize_vertices(combo)
                fig = FigureFactory.create_figure(
                    normalized, FigureType.RIGHT_TRIANGLE)
                figures.append(fig)
            elif ShapeDetector.is_acute_triangle(combo):
                normalized = ShapeDetector.normalize_vertices(combo)
                fig = FigureFactory.create_figure(
                    normalized, FigureType.ACUTE_TRIANGLE)
                figures.append(fig)

        # 2. Generar combinaciones de 4 puntos (cuadriláteros)
        quad_combinations = ShapeDetector.combine_four_points(point_list)

        for combo in quad_combinations:
            if ShapeDetector.is_square(combo):
                normalized = ShapeDetector.normalize_vertices(combo)
                fig = FigureFactory.create_figure(
                    normalized, FigureType.SQUARE)
                figures.append(fig)
            elif ShapeDetector.is_rectangle(combo):
                normalized = ShapeDetector.normalize_vertices(combo)
                fig = FigureFactory.create_figure(
                    normalized, FigureType.RECTANGLE)
                figures.append(fig)

        return figures

    @staticmethod
    def normalize_vertices(points: list) -> list:
        """
        Ordena los puntos en sentido horario alrededor del centro
        Acepta 3 o 4 puntos
        """
        if len(points) not in (3, 4):
            raise ValueError("normalize_vertices solo acepta 3 o 4 puntos")

        # A. Centroide
        cx = sum(p.x for p in points) / len(points)
        cy = sum(p.y for p in points) / len(points)

        # B. Calcular ángulo de cada punto
        def angle(p: Point):
            return math.atan2(p.y - cy, p.x - cx)

        # C. Ordenar por ángulo (sentido horario: angulos descendentes)
        ordered = sorted(points, key=angle, reverse=True)

        return ordered

    @staticmethod
    def compute_sides(vertices: list) -> list[float]:
        """
        Calcula las longitudes de los lados consecutivos entre puntos ordenados.
        Retorna una lista de distancias.
        """

        n = len(vertices)
        if n not in (3, 4):
            raise ValueError(
                "compute_sides solo acepta triángulos o cuadriláteros.")

        sides = []
        for i in range(n):
            p1 = vertices[i]
            # conecta con el siguiente, y el último con el primero
            p2 = vertices[(i + 1) % n]
            sides.append(p1.distance_to(p2))

        return sides

    @staticmethod
    def compute_vectors(vertices: list) -> list:
        """
        Devuelve una lista de vectores (tuplas dx, dy) entre puntos consecutivos.
        Útil para detectar ángulos mediante producto punto.
        Acepta 3 o 4 vértices ordenados.
        """

        n = len(vertices)
        if n not in (3, 4):
            raise ValueError(
                "compute_vectors solo acepta triángulos o cuadriláteros.")

        vectors = []

        for i in range(n):
            p1 = vertices[i]
            p2 = vertices[(i + 1) % n]  # siguiente, y el último con el primero

            dx = p2.x - p1.x
            dy = p2.y - p1.y

            vectors.append((dx, dy))

        return vectors

    @staticmethod
    def dot(v1: tuple, v2: tuple) -> float:
        """
        Producto punto entre dos vectores 2D.
        """
        return v1[0] * v2[0] + v1[1] * v2[1]

    @staticmethod
    def is_perpendicular(v1, v2, tol=1e-6) -> bool:
        return abs(ShapeDetector.dot(v1, v2)) < tol

    @staticmethod
    def is_acute(v1, v2) -> bool:
        return ShapeDetector.dot(v1, v2) > 0
    # ----------------------------------------------------
    # COMBINACIONES
    # ----------------------------------------------------

    @staticmethod
    def combine_three_points(points: list) -> list:
        """Generate all combinations of 3 points."""
        results = []
        n = len(points)
        for i in range(n - 2):
            for j in range(i + 1, n - 1):
                for k in range(j + 1, n):
                    results.append([points[i], points[j], points[k]])

        return results

    @staticmethod
    def combine_four_points(points: list) -> list:
        """Generate all combinations of 4 points."""
        results = []
        n = len(points)
        for i in range(n - 3):
            for j in range(i + 1, n - 2):
                for k in range(j + 1, n - 1):
                    for l in range(k + 1, n):
                        results.append(
                            [points[i], points[j], points[k], points[l]])

        return results

    # ----------------------------------------------------
    # DETECCIONES DE FIGURAS
    # ----------------------------------------------------
    @staticmethod
    def is_square(points: list) -> bool:
        """
        Return True if the 4 points form a valid square.
        Reglas:
        - Debe ser un rectángulo
        - Todos los lados deben ser iguales
        """

        # Primero asegurar que es un rectángulo
        if not ShapeDetector.is_rectangle(points):
            return False

        vertices = ShapeDetector.normalize_vertices(points)
        sides = ShapeDetector.compute_sides(vertices)

        # Verificar que todos los lados sean iguales
        tol = 1e-6
        for i in range(1, 4):
            if abs(sides[i] - sides[0]) > tol:
                return False

        return True

    @staticmethod
    def is_rectangle(points: list) -> bool:
        """
        Return True if the 4 points form a valid rectangle.
        Regla:
        - 4 puntos
        - vértices ordenados (normalize_vertices)
        - todos los ángulos son rectos (producto punto ≈ 0)
        - lados opuestos son iguales
        """

        if len(points) != 4:
            return False

        vertices = ShapeDetector.normalize_vertices(points)
        sides = ShapeDetector.compute_sides(vertices)

        # 1. Verificar ángulos rectos en cada vértice
        # Para cada vértice, necesitamos el vector que ENTRA y el que SALE
        for i in range(4):
            # Vector que entra al vértice i (desde i-1 a i)
            p_prev = vertices[(i - 1) % 4]
            p_curr = vertices[i]
            p_next = vertices[(i + 1) % 4]

            # Vector entrante: de p_prev a p_curr
            v_in = (p_curr.x - p_prev.x, p_curr.y - p_prev.y)
            # Vector saliente: de p_curr a p_next
            v_out = (p_next.x - p_curr.x, p_next.y - p_curr.y)

            if not ShapeDetector.is_perpendicular(v_in, v_out):
                return False

        # 2. Verificar lados opuestos iguales (tolerancia)
        tol = 1e-6
        if abs(sides[0] - sides[2]) > tol:
            return False
        if abs(sides[1] - sides[3]) > tol:
            return False

        return True

    @staticmethod
    def is_right_triangle(points: list) -> bool:
        """Return True if the 3 points form a right triangle."""
        if len(points) != 3:
            return False

        vertices = ShapeDetector.normalize_vertices(points)
        vectors = ShapeDetector.compute_vectors(vertices)

        # Evaluar los 3 ángulos
        for i in range(3):
            v1 = vectors[i]
            v2 = vectors[(i + 1) % 3]
            if ShapeDetector.is_perpendicular(v1, v2):
                return True

        return False

    @staticmethod
    def is_acute_triangle(points: list) -> bool:
        """Return True if the 3 points form an acute triangle."""
        if len(points) != 3:
            return False

        vertices = ShapeDetector.normalize_vertices(points)
        vectors = ShapeDetector.compute_vectors(vertices)

        # Si algún ángulo NO es agudo → no es triángulo agudo
        for i in range(3):
            v1 = vectors[i]
            v2 = vectors[(i + 1) % 3]
            if not ShapeDetector.is_acute(v1, v2):
                return False

        return True
