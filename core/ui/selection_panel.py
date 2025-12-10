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

    def __init__(self, fig, on_selection_change_callback):
        """
        :param fig: Matplotlib Figure (NOT Axes)
        :param on_selection_change_callback: function(FigureType | None)
        """

        self.fig = fig
        self.callback = on_selection_change_callback

        # Configure UI space on the right side of the figure
        self._setup_panel()

    # ---------------------------------------------------------
    # UI creation
    # ---------------------------------------------------------
    def _setup_panel(self):
        # Reserve white space on the right side for the panel
        self.fig.subplots_adjust(right=0.75)

        # Create the axes for the radio buttons
        rax = self.fig.add_axes([0.78, 0.4, 0.18, 0.3])

        labels = ["Todas"] + [ft.name for ft in FigureType]

        self.radio = RadioButtons(rax, labels, active=0)
        self.radio.on_clicked(self._on_radio_clicked)
        rax.set_title("Mostrar:", fontsize=10, fontweight="bold")

    # ---------------------------------------------------------
    # Event handler (UI → callback)
    # ---------------------------------------------------------
    def _on_radio_clicked(self, label):
        if label == "Todas":
            selected = None
        else:
            selected = FigureType[label]

        # Notify listener (DrawService or component)
        self.callback(selected)