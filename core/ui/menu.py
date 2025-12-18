import tkinter as tk
from tkinter import ttk, messagebox, simpledialog


from core.data.data_manager import DataManager
from core.detector.shape_detector import ShapeDetector
from core.analysis.shape_sorter import ShapeSorter
from core.ui.draw_service import DrawService
from core.ui.cartesian_plane_component import CartesianPlaneComponent
from core.domain.point import Point

import matplotlib.pyplot as plt


class Menu:
    # --- Colores y Estilos (Dark Tech Theme) ---
    COLOR_BG = "#21252B"       # Fondo oscuro principal
    COLOR_FG = "#D7DAE0"       # Texto claro
    COLOR_ACCENT = "#61AFEF"   # Azul brillante para acciones principales
    COLOR_BTN_BG = "#3E4451"   # Fondo de botones
    COLOR_BTN_HOVER = "#505868"  # Color al pasar el mouse

    FONT_TITLE = ("Segoe UI", 18, "bold")
    FONT_NORMAL = ("Segoe UI", 11)

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
        self.root.configure(bg=self.COLOR_BG)

        # Configurar estilos
        self._configure_styles()

        # Centrar ventana
        self._center_window(450, 550)

        self.root.protocol("WM_DELETE_WINDOW", self._on_close)

        self._build_ui()

    # ----------------------------------------------------
    # Configuración de Estilos (ttk)
    # ----------------------------------------------------
    def _configure_styles(self):
        style = ttk.Style()
        style.theme_use('clam')  # Base theme que permite mayor personalización

        # Configurar Frame principal
        style.configure("TFrame", background=self.COLOR_BG)

        # Configurar Label
        style.configure("TLabel",
                        background=self.COLOR_BG,
                        foreground=self.COLOR_FG,
                        font=self.FONT_NORMAL)

        # Configurar Botones Genéricos
        style.configure("TButton",
                        font=self.FONT_NORMAL,
                        background=self.COLOR_BTN_BG,
                        foreground=self.COLOR_FG,
                        borderwidth=0,
                        focuscolor=self.COLOR_ACCENT)

        # Mapeo de estados para efectos hover/active
        style.map("TButton",
                  background=[('active', self.COLOR_BTN_HOVER),
                              ('pressed', self.COLOR_ACCENT)],
                  foreground=[('active', '#FFFFFF'), ('pressed', '#FFFFFF')])

        # Configurar Separador
        style.configure("TSeparator", background=self.COLOR_BTN_BG)

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
        # Frame principal para aplicar fondo y padding
        main_frame = ttk.Frame(self.root)
        main_frame.pack(fill=tk.BOTH, expand=True, padx=20, pady=20)

        title = tk.Label(main_frame, text="Menú Principal",
                         font=self.FONT_TITLE, bg=self.COLOR_BG, fg=self.COLOR_ACCENT)
        title.pack(pady=(0, 15))

        # Separador inicial
        ttk.Separator(main_frame, orient='horizontal').pack(
            fill='x', pady=(0, 10))

        # Ancho consistente para los botones
        BTN_WIDTH = 32

        # --- SECCIÓN: DATOS ---
        tk.Label(main_frame, text="GESTIÓN DE DATOS",
                 bg=self.COLOR_BG, fg="#ABB2BF", font=("Segoe UI", 9, "bold")).pack(anchor="w", pady=(5, 5))

        ttk.Button(main_frame, text="Agregar Puntos", width=BTN_WIDTH,
                   command=self.show_add_points_window).pack(pady=4)

        ttk.Button(main_frame, text="Guardar Puntos", width=BTN_WIDTH,
                   command=self.save_data).pack(pady=4)

        ttk.Button(main_frame, text="Cargar Puntos", width=BTN_WIDTH,
                   command=self.load_data).pack(pady=4)

        # Separador intermedio
        ttk.Separator(main_frame, orient='horizontal').pack(fill='x', pady=15)

        # --- SECCIÓN: OPERACIONES ---
        tk.Label(main_frame, text="OPERACIONES Y VISUALIZACIÓN",
                 bg=self.COLOR_BG, fg="#ABB2BF", font=("Segoe UI", 9, "bold")).pack(anchor="w", pady=(5, 5))

        ttk.Button(main_frame, text="Detectar Figuras", width=BTN_WIDTH,
                   command=self.detect_shapes).pack(pady=4)

        ttk.Button(main_frame, text="Ordenar Figuras por Área", width=BTN_WIDTH,
                   command=self.sort_figures).pack(pady=4)

        ttk.Button(main_frame, text="Mostrar Figuras Detectadas", width=BTN_WIDTH,
                   command=self.show_figures_window).pack(pady=4)

        ttk.Button(main_frame, text="Mostrar Plano Cartesiano", width=BTN_WIDTH,
                   command=self.refresh_plane).pack(pady=4)

        ttk.Button(main_frame, text="Cargar Prueba", width=BTN_WIDTH,
                   command=self.show_load_test_window).pack(pady=4)

        # Separador final
        ttk.Separator(main_frame, orient='horizontal').pack(fill='x', pady=15)

        ttk.Button(main_frame, text="Salir", width=BTN_WIDTH,
                   command=self._on_close).pack(pady=5)

    # -----------------------------------------------------
    # AGREGAR PUNTOS
    # -----------------------------------------------------
    def show_add_points_window(self):
        win = tk.Toplevel(self.root)
        win.title("Agregar Puntos")
        win.resizable(False, False)
        win.configure(bg=self.COLOR_BG)
        win.protocol("WM_DELETE_WINDOW", win.destroy)

        # Centrar ventana secundaria
        self._center_child_window(win, 350, 250)

        # Contenedor con estilo
        container = ttk.Frame(win)
        container.pack(fill=tk.BOTH, expand=True, padx=20, pady=20)

        tk.Label(container, text="Ingrese un punto en formato x,y:",
                 bg=self.COLOR_BG, fg=self.COLOR_FG, font=self.FONT_NORMAL).pack(pady=10)

        entry = tk.Entry(container, width=20, bg=self.COLOR_BTN_BG,
                         fg="white", insertbackground="white", relief="flat")
        entry.pack(pady=5)

        def agregar():
            value = entry.get().strip()
            try:
                x, y = map(int, value.split(","))
                p = Point(x, y)

                print("Lista actual de puntos:",
                      self.data_manager.get_points())
                print("Intentando agregar:", p)

                if not self.data_manager.add_point(p):
                    messagebox.showerror("Duplicado", "Ese punto ya existe.")
                else:
                    messagebox.showinfo("OK", "Punto agregado.")
                    entry.delete(0, tk.END)  # Limpiar entrada
            except:
                messagebox.showerror("Error", "Formato inválido. Use x,y")

        ttk.Button(container, text="Agregar Punto",
                   command=agregar).pack(pady=15)

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

        self.data_manager.figures = self.sorter.sort_by_area(
            self.data_manager.figures)
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
        win.configure(bg=self.COLOR_BG)
        win.protocol("WM_DELETE_WINDOW", win.destroy)
        self._center_child_window(win, 600, 500)

        container = ttk.Frame(win)
        container.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)

        tk.Label(container, text="Figuras Detectadas",
                 font=self.FONT_TITLE, bg=self.COLOR_BG, fg=self.COLOR_ACCENT).pack(pady=10)

        # Create frame for list and canvas
        content_frame = ttk.Frame(container)
        content_frame.pack(pady=10, fill=tk.BOTH, expand=True)

        # Listbox on the left
        list_frame = ttk.Frame(content_frame)
        list_frame.pack(side=tk.LEFT, padx=10, fill=tk.BOTH, expand=True)

        listbox = tk.Listbox(list_frame, width=55, height=20,
                             bg=self.COLOR_BTN_BG, fg="white", selectbackground=self.COLOR_ACCENT, relief="flat", font=self.FONT_NORMAL)
        listbox.pack(fill=tk.BOTH, expand=True)

        for f in figs:
            listbox.insert(
                tk.END,
                f"{f.name} | Área: {f.area:.2f} | Tipo: {f.type.name}"
            )

    # -----------------------------------------------------
    # MOSTRAR PLANO
    # -----------------------------------------------------
    def refresh_plane(self):
        # Evitar ventanas duplicadas
        plt.close("all")

        points = self.data_manager.get_points()
        figures = self.data_manager.get_figures()

        # Reuse existing instances to maintain matplotlib state
        draw_service = DrawService()
        plane = CartesianPlaneComponent(draw_service)

        plane.update(points, figures)

    # -----------------------------------------------------
    # CARGAR PRUEBA
    # -----------------------------------------------------
    def show_load_test_window(self):
        val = simpledialog.askinteger("Cargar Prueba", "Seleccione lista (0-3):",
                                      parent=self.root, minvalue=0, maxvalue=3)
        if val is not None:
            self.data_manager.points = []
            for p in self.data_manager.test_list(val):
                self.data_manager.add_point(p)
            messagebox.showinfo("Listo", "Puntos cargados.")

    # -----------------------------------------------------
    # INICIAR LOOP
    # -----------------------------------------------------
    def run(self):
        self.root.mainloop()
