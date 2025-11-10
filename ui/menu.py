from data.data_manager import DataManager
from core.shape_detector import ShapeDetector
from core.shape_sorter import ShapeSorter
from ui.draw_service import DrawService

class Menu:
    """
    Handles user interaction and menu navigation.
    """
    def __init__(self):
        self.data_manager = DataManager()
        self.detector = ShapeDetector()
        self.sorter = ShapeSorter()
        self.drawer = DrawService()

    def show_main_menu(self):
        pass

    def show_menu_add_points(self):
        """Menu for adding points manually."""
        pass

    def save_data(self):
        """Save data to JSON."""
        pass

    def load_data(self):
        """Load data from JSON."""
        pass