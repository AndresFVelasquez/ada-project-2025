import tkinter as tk
from tkinter import ttk, messagebox


from core.data.data_manager import DataManager
from core.detector.shape_detector import ShapeDetector
from core.analysis.shape_sorter import ShapeSorter
from core.ui.draw_service import DrawService
from core.ui.cartesian_plane_component import CartesianPlaneComponent
from core.domain.point import Point

import matplotlib.pyplot as plt
class Menu:

    def __init__(self):
        # --- Dependencias del sistema ---
        self.data_manager = DataManager()
        self.detector = ShapeDetector
        self.sorter = ShapeSorter
        self.draw_service = DrawService()
        self.plane = CartesianPlaneComponent(self.draw_service)

        # --- Ventana raíz ---
        self.root = tk.Tk()
        self.root.title("Sistema Geométrico - Menú Principal")
        self.root.resizable(False, False)

        # Centrar ventana
        self._center_window(450, 550)

        self.root.protocol("WM_DELETE_WINDOW", self._on_close)

        self._build_ui()

    # ----------------------------------------------------
    # Cerrar todas las ventanas
    # ----------------------------------------------------
    def _on_close(self):
        plt.close("all")   # Cerrar TODAS las ventanas de Matplotlib
        self.root.destroy()  # Cerrar Tk correctamente
    # -----------------------------------------------------
    # Centrar ventana en pantalla
    # -----------------------------------------------------
    def _center_window(self, width, height):
        self.root.update_idletasks()
        screen_w = self.root.winfo_screenwidth()
        screen_h = self.root.winfo_screenheight()

        x = (screen_w // 2) - (width // 2)
        y = (screen_h // 2) - (height // 2)

        self.root.geometry(f"{width}x{height}+{x}+{y}")

    # -----------------------------------------------------
    # UI PRINCIPAL
    # -----------------------------------------------------
    def _build_ui(self):
        title = tk.Label(self.root, text="Menú Principal", font=("Arial", 18, "bold"))
        title.pack(pady=15)

        # Ancho consistente para los botones
        BTN_WIDTH = 32

        ttk.Button(self.root, text="Agregar Puntos", width=BTN_WIDTH,
                   command=self.show_add_points_window).pack(pady=8)

        ttk.Button(self.root, text="Guardar Puntos", width=BTN_WIDTH,
                   command=self.save_data).pack(pady=8)

        ttk.Button(self.root, text="Cargar Puntos", width=BTN_WIDTH,
                   command=self.load_data).pack(pady=8)

        ttk.Button(self.root, text="Detectar Figuras", width=BTN_WIDTH,
                   command=self.detect_shapes).pack(pady=8)

        ttk.Button(self.root, text="Ordenar Figuras por Área", width=BTN_WIDTH,
                   command=self.sort_figures).pack(pady=8)

        ttk.Button(self.root, text="Mostrar Figuras Detectadas", width=BTN_WIDTH,
                   command=self.show_figures_window).pack(pady=8)

        ttk.Button(self.root, text="Mostrar Plano Cartesiano", width=BTN_WIDTH,
                   command=self.refresh_plane).pack(pady=8)

        ttk.Button(self.root, text="Salir", width=BTN_WIDTH,
                   command=self.root.quit).pack(pady=20)

    # -----------------------------------------------------
    # AGREGAR PUNTOS
    # -----------------------------------------------------
    def show_add_points_window(self):
        win = tk.Toplevel(self.root)
        win.title("Agregar Puntos")
        win.resizable(False, False)
        win.protocol("WM_DELETE_WINDOW", win.destroy)

        # Centrar ventana secundaria
        self._center_child_window(win, 350, 250)

        tk.Label(win, text="Ingrese un punto en formato x,y:").pack(pady=10)

        entry = tk.Entry(win, width=20)
        entry.pack()

        def agregar():
            value = entry.get().strip()
            try:
                x, y = map(int, value.split(","))
                p = Point(x, y)

                print("Lista actual de puntos:", self.data_manager.get_points())
                print("Intentando agregar:", p)

                if not self.data_manager.add_point(p):
                    messagebox.showerror("Duplicado", "Ese punto ya existe.")
                else:
                    messagebox.showinfo("OK", "Punto agregado.")
            except:
                messagebox.showerror("Error", "Formato inválido. Use x,y")

        ttk.Button(win, text="Agregar Punto", command=agregar).pack(pady=15)

        

    # Centrar ventanas hijas
    def _center_child_window(self, win, w, h):
        win.update_idletasks()
        x = (win.winfo_screenwidth() // 2) - (w // 2)
        y = (win.winfo_screenheight() // 2) - (h // 2)
        win.geometry(f"{w}x{h}+{x}+{y}")

    # -----------------------------------------------------
    # GUARDAR / CARGAR PUNTOS
    # -----------------------------------------------------
    def save_data(self):
        self.data_manager.save_points()
        messagebox.showinfo("Guardado", "Puntos guardados exitosamente.")

    def load_data(self):
        self.data_manager.load_points()
        messagebox.showinfo("Cargado", "Puntos cargados exitosamente.")

    # -----------------------------------------------------
    # DETECTAR FIGURAS
    # -----------------------------------------------------
    def detect_shapes(self):
        points = self.data_manager.get_points()
        if len(points) < 3:
            messagebox.showerror("Error", "Necesita al menos 3 puntos.")
            return

        figures = self.detector.detect_shapes(points)
        self.data_manager.figures = figures

        messagebox.showinfo("OK", f"Figuras detectadas: {len(figures)}")

    # -----------------------------------------------------
    # ORDENAR FIGURAS
    # -----------------------------------------------------
    def sort_figures(self):
        if not self.data_manager.figures:
            messagebox.showwarning("Sin figuras", "Primero detecte figuras.")
            return

        self.data_manager.figures = self.sorter.sort_by_area(self.data_manager.figures)
        messagebox.showinfo("OK", "Figuras ordenadas por área.")

    # -----------------------------------------------------
    # VENTANA PARA VER FIGURAS DETECTADAS
    # -----------------------------------------------------
    def show_figures_window(self):
        figs = self.data_manager.get_figures()
        if not figs:
            messagebox.showwarning("Sin Figuras", "No hay figuras detectadas.")
            return

        win = tk.Toplevel(self.root)
        win.title("Figuras Detectadas")
        win.resizable(False, False)
        win.protocol("WM_DELETE_WINDOW", win.destroy)
        self._center_child_window(win, 400, 500)

        tk.Label(win, text="Figuras Detectadas", font=("Arial", 14)).pack(pady=10)

        listbox = tk.Listbox(win, width=55, height=20)
        listbox.pack(pady=10, fill=tk.BOTH, expand=False)

        for f in figs:
            listbox.insert(
                tk.END,
                f"{f.name} | Área: {f.area:.2f} | Tipo: {f.type.name} | Visible: {f.visible}"
            )

    # -----------------------------------------------------
    # MOSTRAR PLANO
    # -----------------------------------------------------
    def refresh_plane(self):
        points = self.data_manager.get_points()
        figures = self.data_manager.get_figures()
        self.plane.update(points, figures)

    # -----------------------------------------------------
    # INICIAR LOOP
    # -----------------------------------------------------
    def run(self):
        self.root.mainloop()
