from core.ui.draw_service import DrawService
from core.ui.selection_panel import SelectionPanel

class CartesianPlaneComponent:

    def __init__(self, draw_service):
        self.draw_service = draw_service
        self.selection_panel = None  # se creará en update()

    def update(self, points, figures):
        # Crear panel de selección SOLO la primera vez
        # Pasamos figures para que calcule los conteos
        if self.selection_panel is None:
            self.selection_panel = SelectionPanel(
                self.draw_service.fig,
                self.on_selection_change,
                figures=figures
            )

        self.draw_service.ax.clear()
        self.draw_service.draw_cartesian_plane()
        self.draw_service.draw_points(points)
        self.draw_service.draw_figures(figures)
        self.draw_service.show()

    def on_selection_change(self, selected_type):
        self.draw_service.set_filter(selected_type)
        self.draw_service.redraw()
