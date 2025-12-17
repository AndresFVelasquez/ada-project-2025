
from core.domain.figure import Figure

class ShapeSorter:
    """
    Clase estática encargada de ordenar figuras según su área.
    """


    @staticmethod
    def sort_by_area(figures, ascending=True):
        """
        sort a list of figures by your area.

        parameters:
        - Figures: list[Figure]
          list of figures. Each figure must have a .area attribute
        - ascending: bool
          true -> Order from minor to major
          false -> Order from major to minor

        return:
        - New list of figures ordered by area.
        """
        
        #  Caso base: lista vacía o de 1 elemento 
        if len(figures) <= 1:
            return figures[:]  

        #  Merge Sort 
        def merge_sort(lista):
            if len(lista) <= 1:
                return lista[:]

            mid = len(lista) // 2
            left = merge_sort(lista[:mid])
            right = merge_sort(lista[mid:])
            return merge(left, right)

        def merge(left, right):
            """Mezcla dos listas de figuras, ordenadas por área."""
            result = []
            i = j = 0

            # Combinar en orden aumentando
            while i < len(left) and j < len(right):
                if left[i].area <= right[j].area:
                    result.append(left[i])
                    i += 1
                else:
                    result.append(right[j])
                    j += 1

            # Agregar lo sobrante de cualquiera de las 2 listas
            result.extend(left[i:])
            result.extend(right[j:])
            return result

        # Orden ascendente por defecto
        ordered = merge_sort(figures)

        # Si se pide descendente, invertir la lista
        if not ascending:
            ordered = ordered[::-1]

        return ordered
