import matplotlib.pyplot as plt
from matplotlib.widgets import RadioButtons, Button
from core.domain.point import Point
from core.domain.figure import Figure
from core.domain.figure_type import FigureType


class DrawService:

    """
    Responsible for drawing points, figures, and the Cartesian plane.
    Does NOT modify data.
    """

    def __init__(self):
        self.fig, self.ax = plt.subplots(figsize=(10, 6))
        self.ax.set_aspect('equal')
        self.selected_figure_type = None  # None significa "Todas"
        self._setup_radio_buttons()
        self._connect_events()

        # Color palette for triangles
        self.triangle_colors = ['red', 'blue', 'green',
                                'purple', 'cyan', 'magenta', 'yellow', 'orange']
        self.triangle_color_index = 0

    def _setup_radio_buttons(self):
        # Crear espacio para los botones de radio a la derecha
        self.fig.subplots_adjust(right=0.75)
        rax = self.fig.add_axes([0.78, 0.4, 0.18, 0.3])

        # Opciones de selección
        labels = ['Todas', 'SQUARE', 'RECTANGLE',
                  'RIGHT_TRIANGLE', 'ACUTE_TRIANGLE']
        self.radio = RadioButtons(rax, labels, active=0)
        self.radio.on_clicked(self._on_radio_change)

        # Título para el selector
        rax.set_title('Colorear:', fontsize=10, fontweight='bold')

    def _on_radio_change(self, label):
        # Actualizar el tipo de figura seleccionado
        if label == 'Todas':
            self.selected_figure_type = None
        else:
            self.selected_figure_type = FigureType[label]

        # Reset triangle color index
        self.triangle_color_index = 0

        # Redibujar todo
        self.ax.clear()
        self.draw_cartesian_plane()
        if hasattr(self, '_cached_points'):
            self.draw_points(self._cached_points)
        if hasattr(self, '_cached_figures'):
            self.draw_figures(self._cached_figures)
        self.fig.canvas.draw_idle()

    def draw_points(self, points: list):
        pass

    def draw_figures(self, figures: list):
        # Guardar figuras en caché para redibujar
        self._cached_figures = figures

        # Reset triangle color index at the start of drawing
        self.triangle_color_index = 0

        for figure in figures:
            # Determinar si esta figura debe ser coloreada
            should_color = (self.selected_figure_type is None or
                            figure.type == self.selected_figure_type)

            if should_color:
                # Aplicar color según el tipo
                if figure.type == FigureType.SQUARE:
                    color = 'green'
                elif figure.type == FigureType.RECTANGLE:
                    color = 'orange'
                elif figure.type in [FigureType.RIGHT_TRIANGLE, FigureType.ACUTE_TRIANGLE]:
                    # Assign unique color to each triangle
                    color = self.triangle_colors[self.triangle_color_index % len(
                        self.triangle_colors)]
                    self.triangle_color_index += 1
                else:
                    color = 'black'

                # Figuras seleccionadas: muy visibles con bordes gruesos
                alpha = 0.7
                linewidth = 5
            else:
                # Figuras no seleccionadas en gris y más transparentes
                color = 'gray'
                alpha = 0.2
                linewidth = 1.5

            # Dibujar solo el borde del polígono (sin relleno)
            xs = [p.x for p in figure.vertices]
            ys = [p.y for p in figure.vertices]

            # Solo dibujar la línea del contorno
            self.ax.plot(xs + [xs[0]], ys + [ys[0]], color=color,
                         linewidth=linewidth, label=figure.type.name)

    def draw_cartesian_plane(self):
        pass

    def _connect_events(self):
        # Evento para zoom solamente
        self.fig.canvas.mpl_connect('scroll_event', self._on_zoom)

    def _on_zoom(self, event):
        # Zoom con la rueda del mouse
        scale = 1.1 if event.button == 'up' else 0.9
        self.ax.set_xlim(
            event.xdata - (event.xdata - self.ax.get_xlim()[0]) * scale,
            event.xdata + (self.ax.get_xlim()[1] - event.xdata) * scale
        )
        self.ax.set_ylim(
            event.ydata - (event.ydata - self.ax.get_ylim()[0]) * scale,
            event.ydata + (self.ax.get_ylim()[1] - event.ydata) * scale
        )
        self.fig.canvas.draw_idle()

    def draw_cartesian_plane(self):
        self.ax.axhline(0, color='black', linewidth=1)
        self.ax.axvline(0, color='black', linewidth=1)

        self.ax.set_xlabel('X')
        self.ax.set_ylabel('Y')

        self.ax.grid(True, color="gray", linestyle="--", linewidth=0.5)

    def draw_points(self, points):
        # Guardar puntos en caché para redibujar
        self._cached_points = points
        xs = [p.x for p in points]
        ys = [p.y for p in points]
        self.ax.scatter(xs, ys, color='red')
        # Dibujar coordenadas
        for p in points:
            self.ax.text(p.x + 0.1, p.y + 0.1, f"({p.x}, {p.y})", fontsize=9)
        self.fig.canvas.draw_idle()

    def show(self):
        plt.show()
