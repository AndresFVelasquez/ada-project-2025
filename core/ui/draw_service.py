import matplotlib.pyplot as plt
from matplotlib.widgets import RadioButtons, Button
from core.domain.point import Point
from core.domain.figure import Figure
from core.domain.figure_type import FigureType


class DrawService:
    """
    Draws points, figures and the Cartesian plane.
    Pure rendering. No UI logic. No filtering logic.
    """

    def __init__(self):
        self.fig, self.ax = plt.subplots(figsize=(10, 6))
        self.ax.set_aspect('equal')
        self._connect_events()

        self._filter_type = None
        # Cache only for redraw, not for UI logic
        self._points = []
        self._figures = []

    def set_filter(self, figure_type):
        self._filter_type = figure_type

    # --------------------------
    # Event hookup
    # --------------------------
    def _connect_events(self):
        self.fig.canvas.mpl_connect('scroll_event', self._on_zoom)

    def _on_zoom(self, event):
        scale = 1.1 if event.button == 'up' else 0.9
        if event.xdata is None or event.ydata is None:
            return

        self.ax.set_xlim(
            event.xdata - (event.xdata - self.ax.get_xlim()[0]) * scale,
            event.xdata + (self.ax.get_xlim()[1] - event.xdata) * scale
        )
        self.ax.set_ylim(
            event.ydata - (event.ydata - self.ax.get_ylim()[0]) * scale,
            event.ydata + (self.ax.get_ylim()[1] - event.ydata) * scale
        )
        self.fig.canvas.draw_idle()

    # --------------------------
    # Drawing
    # --------------------------
    def draw_cartesian_plane(self):
        self.ax.axhline(0, color='black', linewidth=1)
        self.ax.axvline(0, color='black', linewidth=1)
        self.ax.set_xlabel("X")
        self.ax.set_ylabel("Y")
        self.ax.grid(True, linestyle="--", linewidth=0.5, alpha=0.6)

    def draw_points(self, points):
        self._points = points
        xs = [p.x for p in points]
        ys = [p.y for p in points]
        self.ax.scatter(xs, ys, color="red", s=40)

        for p in points:
            self.ax.text(p.x + 0.1, p.y + 0.1,
                         f"({p.x},{p.y})", fontsize=8)

    def draw_figures(self, figures):
        self._figures = figures

        for fig in figures:
            if self._filter_type is not None and fig.type != self._filter_type:
                continue  # No dibujar figuras no seleccionadas

            xs = [p.x for p in fig.vertices] + [fig.vertices[0].x]
            ys = [p.y for p in fig.vertices] + [fig.vertices[0].y]
            lines = self.ax.plot(xs, ys, linewidth=2.5)
            color = lines[0].get_color()
            self.ax.fill(xs, ys, color=color, alpha=0.15)

    # --------------------------
    # Full redraw
    # --------------------------
    def redraw(self):
        self.ax.clear()
        self.draw_cartesian_plane()
        if self._points:
            self.draw_points(self._points)
        if self._figures:
            self.draw_figures(self._figures)
        self.fig.canvas.draw_idle()

    def show(self):
        plt.show()