# CONTRATOS DEL SISTEMA

Este documento define los **contratos de interacción entre módulos** del sistema.  
Aquí se describe qué espera cada clase como entrada, qué entrega como salida y cuáles son sus reglas de operación.

Importante:  
Los contratos definen **qué debe cumplir la implementación**, no cómo se implementa.

---

# 1. MÓDULO: DOMINIO (CORE)

---

## 1.1 Clase `Point`

### Responsabilidad
Representa un punto del plano cartesiano con coordenadas enteras.

### Contrato
**Atributos**
- `x: int`
- `y: int`

**Métodos**
- `distance_to(other: Point) → float`
- `equals(other: Point) → bool`
- getters/setters

**Reglas**
- Las coordenadas deben ser enteras.
- No pueden repetirse puntos dentro de una misma lista.

---

## 1.2 Clase abstracta `Figure`

### Responsabilidad
Clase base para todas las figuras geométricas.

### Contrato
**Atribututos**
- `name: String`
- `vertices: List<Point>`
- `area: float`
- `num_sides: int`
- `type: FigureType`

**Métodos**
- `calculate_area() → float`
- getters/setters

**Reglas**
- El `type` se asigna dentro de la fábrica.
- Cada subclase debe implementar `calculate_area()`.

---

## 1.3 Subclases de `Figure`
- `Square`
- `Rectangle`
- `RightTriangle`
- `AcuteTriangle`

### Contrato
- Deben implementar `calculate_area()`.
- Reciben una lista de puntos válida desde `FigureFactory`.

---

## 1.4 Enum `FigureType`

### Responsabilidad
Identificar los tipos de figura permitidos.

### Valores
- `SQUARE`
- `RECTANGLE`
- `RIGHT_TRIANGLE`
- `ACUTE_TRIANGLE`

---

# 2. MÓDULO: FÁBRICA DE FIGURAS

---

## 2.1 Clase `FigureFactory`

### Responsabilidad
Crear instancias de figuras geométricas.

### Contrato
```python
create_figure(points: List[Point], type: FigureType) → Figure
```

### Reglas
- No valida geometría.
- Construye el objeto de la figura indicada.
- Asigna automáticamente:
  - `type`
  - `name` con el formato: `Tipo + consecutivo`
- Puede crear:
  - `Square`
  - `Rectangle`
  - `RightTriangle`
  - `AcuteTriangle`

---

# 3. MÓDULO: DETECCIÓN GEOMÉTRICA

---

## 3.1 Clase `ShapeDetector` (estática)

### Responsabilidad
Detectar figuras válidas mediante combinaciones de 3 y 4 puntos.

### Contrato
```python
detect_shapes(point_list: List[Point]) → List[Figure]
```

### Métodos
- `combine_three_points(points) → List[List[Point]]`
- `combine_four_points(points) → List[List[Point]]`
- `is_square(points: List[Point]) → bool`
- `is_rectangle(points: List[Point]) → bool`
- `is_right_triangle(points: List[Point]) → bool`
- `is_acute_triangle(points: List[Point]) → bool`

### Reglas
- Solo detecta — **no crea** figuras.
- Usa combinaciones matemáticas C(n,3) y C(n,4).
- Una combinación puede formar más de un tipo de figura.
- No elimina figuras solapadas.
- Cuando una figura es válida, delega su creación a `FigureFactory`.

---

# 4. MÓDULO: ANÁLISIS Y PROCESAMIENTO

---

## 4.1 Clase `ShapeCounter` (estática)

### Responsabilidad
Contar cuántas figuras hay por categoría.

### Contrato
```python
count_by_type(figures: List[Figure]) → Dict[FigureType, int]
```

### Reglas
- Debe generar un contador inicial con **todos** los valores de `FigureType`.
- Usa `figure.type` para clasificar.
- Si un tipo no aparece, debe retornar 0.

---

## 4.2 Clase `ShapeSorter` (estática)

### Responsabilidad
Ordenar figuras por su área.

### Contrato
```python
sort_by_area(figures: List[Figure], ascending: bool) → List[Figure]
```

### Reglas
- Puede devolver una nueva lista o la misma lista ordenada.
- Ordena usando `area` como criterio.
- Puede ordenar de forma `ascendente` o `descendente`.

---

# 5. MÓDULO: PERSISTENCIA

---

## 5.1 Clase `DataManager` (estática)

### Responsabilidad
Guardar y cargar puntos y figuras desde archivo.

### Atributos
- `points: List[Point]`
- `figures: List[Figure]`

### Métodos
- `save_points()`
- `load_points()`
- `save_figures()`
- `load_figures()`
- `add_point(point: Point)`
- `remove_point(point: Point)`
- `get_points() → List[Point]`
- `get_figures() → List[Figure]`

### Reglas
- Debe impedir puntos duplicados.
- El formato de persistencia es libre.
- No debe realizar detección ni análisis geométrico.

---

# 6. MÓDULO: UI Y DIBUJO

---

## 6.1 Clase `DrawService`

### Responsabilidad
Dibujar puntos, figuras y el plano cartesiano.

### Métodos
- `draw_points(points: List[Point])`
- `draw_figures(figures: List[Figure])`
- `draw_cartesian_plane()`

### Reglas
- No modifica datos.
- Las figuras deben dibujarse con colores distintos al plano.
- Cada punto debe mostrar sus coordenadas.

---

## 6.2 Clase `Menu`

### Responsabilidad
Gestionar interacción con el usuario.

### Métodos
- `show_main_menu()`
- `show_menu_add_points()`
- `save_data()`
- `load_data()`
- `select_figures_to_draw()`

### Reglas
- No procesa geometría.
- Coordina:
  - `DataManager`
  - `ShapeDetector`
  - `ShapeCounter`
  - `ShapeSorter`
  - `DrawService`

---

# 7. ENUMERACIÓN

## 7.1 Enum `FigureType`

### Valores
- `SQUARE`
- `RECTANGLE`
- `RIGHT_TRIANGLE`
- `ACUTE_TRIANGLE`
