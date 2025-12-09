import matplotlib.pyplot as plt
from core.domain.point import Point
from core.domain.figure import Figure

class DrawService:
    
    """
    Responsible for drawing points, figures, and the Cartesian plane.
    Does NOT modify data.
    """
    def __init__(self):
        self.fig, self.ax = plt.subplots()
        self.ax.set_aspect('equal')
        self._connect_events()

    def draw_points(self, points: list):
        pass


    def draw_figures(self, figures: list):
        pass


    def draw_cartesian_plane(self):
        pass
    def _connect_events(self):
        # Eventos para zoom y pan
        self.fig.canvas.mpl_connect('scroll_event', self._on_zoom)
        self.fig.canvas.mpl_connect('button_press_event', self._on_press)
        self.fig.canvas.mpl_connect('motion_notify_event', self._on_drag)

        self.dragging = False
        self.last_mouse_x = None
        self.last_mouse_y = None

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

    def _on_press(self, event):
        # Iniciar arrastre (pan)
        self.dragging = True
        self.last_mouse_x = event.xdata
        self.last_mouse_y = event.ydata

    def _on_drag(self, event):
        if not self.dragging or event.xdata is None or event.ydata is None:
            return

        dx = self.last_mouse_x - event.xdata
        dy = self.last_mouse_y - event.ydata

        x0, x1 = self.ax.get_xlim()
        y0, y1 = self.ax.get_ylim()

        self.ax.set_xlim(x0 + dx, x1 + dx)
        self.ax.set_ylim(y0 + dy, y1 + dy)

        self.fig.canvas.draw_idle()

    def draw_cartesian_plane(self):
        self.ax.axhline(0, color='black', linewidth=1)
        self.ax.axvline(0, color='black', linewidth=1)

        self.ax.set_xlabel('X')
        self.ax.set_ylabel('Y')

        self.ax.grid(True, color="gray", linestyle="--", linewidth=0.5)

    def draw_points(self, points):
        xs = [p.x for p in points]
        ys = [p.y for p in points]

        self.ax.scatter(xs, ys, color='red')

        # Dibujar coordenadas
        for p in points:
            self.ax.text(p.x + 0.1, p.y + 0.1, f"({p.x}, {p.y})", fontsize=9)

        self.fig.canvas.draw_idle()

    def show(self):
        plt.show()
    