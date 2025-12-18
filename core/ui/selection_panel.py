import matplotlib.pyplot as plt
from matplotlib.widgets import RadioButtons
from core.domain.figure_type import FigureType


class SelectionPanel:
    """
    UI component responsible only for letting the user choose
    which figure type to highlight.

    Fully SOLID:
    - SRP: Only manages UI selection.
    - DIP: Depends on a callback, not on DrawService.
    - ISP: Only exposes one method.
    """

    def __init__(self, fig, on_selection_change_callback, figures=None):
        """
        :param fig: Matplotlib Figure (NOT Axes)
        :param on_selection_change_callback: function(FigureType | None)
        :param figures: Optional list of figures to calculate counts
        """

        self.fig = fig
        self.callback = on_selection_change_callback
        self.figures = figures if figures else []

        # Configure UI space on the right side of the figure
        self._setup_panel()

    # ---------------------------------------------------------
    # UI creation
    # ---------------------------------------------------------
    def _setup_panel(self):
        # Reserve white space on the right side for the panel
        self.fig.subplots_adjust(right=0.75)

        # Create the axes for the radio buttons
        rax = self.fig.add_axes([0.78, 0.4, 0.21, 0.3])

        # Calcular conteos
        counts = {ft: 0 for ft in FigureType}
        for fig in self.figures:
            if fig.type in counts:
                counts[fig.type] += 1
        
        # Generar etiquetas con conteo
        labels = [f"Todas ({len(self.figures)})"]
        self.label_map = {"Todas": None} # Mapeo inverso de texto a tipo

        for ft in FigureType:
            label = f"{ft.name} ({counts[ft]})"
            labels.append(label)
            self.label_map[label] = ft

        self.radio = RadioButtons(rax, labels, active=0)
        self.radio.on_clicked(self._on_radio_clicked)
        rax.set_title("Mostrar:", fontsize=10, fontweight="bold")

    # ---------------------------------------------------------
    # Event handler (UI → callback)
    # ---------------------------------------------------------
    def _on_radio_clicked(self, label):
        # Extraer el nombre base (ignorando el conteo si es necesario)
        # Pero mejor usamos el mapa que creamos
        selected = self.label_map.get(label)
        
        # En caso de que el label no esté en el mapa (defensivo)
        if selected is None and "Todas" not in label:
             # Fallback simple
             pass

        # Notify listener (DrawService or component)
        self.callback(selected)