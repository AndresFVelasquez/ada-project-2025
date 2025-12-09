from core.ui.draw_service import DrawService

class CartesianPlaneComponent:

    def __init__(self, draw_service: DrawService):
        self.draw_service = draw_service

    def update(self, points):
        # Limpiar
        self.draw_service.ax.clear()

        # Redibujar todo
        self.draw_service.draw_cartesian_plane()
        self.draw_service.draw_points(points)

        # Mostrar ventana
        self.draw_service.show()