# Documentación Técnica del Módulo `shape_detector`

## 1. Propósito General del Módulo

El módulo `shape_detector` implementa un sistema de detección geométrica capaz de identificar figuras 2D a partir de un conjunto de puntos. El procesamiento incluye generación de combinaciones, normalización espacial, evaluación vectorial y verificación geométrica rigurosa. Actualmente se soportan las siguientes figuras:

* Triángulo recto
* Triángulo agudo
* Rectángulo
* Cuadrado

El módulo se integra con los componentes de dominio `FigureFactory` y `FigureType`, permitiendo producir objetos de figura completos para su uso en capas superiores del sistema.

---

## 2. Arquitectura del Módulo

El módulo está organizado como una clase estática (`ShapeDetector`) que centraliza la generación de combinaciones, la normalización geométrica y las funciones de verificación para cada tipo de figura. Su diseño facilita la extensión futura mediante nuevas funciones de verificación y nuevos tipos de figuras.

---

## 3. Función de Alto Nivel

### **`detect_shapes(point_list: list[Point]) -> list`**

Procesa un conjunto de puntos y retorna todas las figuras geométricas válidas construidas a partir de combinaciones de 3 y 4 puntos.

**Entradas:**

* `point_list`: Lista de instancias de `Point`.

**Salidas:**

* Lista de objetos `Figure` generados mediante `FigureFactory`.

**Flujo interno:**

1. Generación de todas las combinaciones de 3 puntos.
2. Evaluación de cada combinación para detectar:

   * Triángulo recto
   * Triángulo agudo
3. Generación de combinaciones de 4 puntos.
4. Evaluación de cada combinación para detectar:

   * Rectángulo
   * Cuadrado
5. Construcción de objetos de figura para cada detección exitosa.

---

## 4. Utilidades Geométricas Internas

### **4.1 Normalización de Vértices**

**`normalize_vertices(points: list) -> list`**

Ordena los puntos alrededor del centroide en sentido horario. Asegura que los algoritmos de cómputo de lados y vectores operen sobre un orden consistente.

Pasos:

1. Cálculo del centroide.
2. Obtención del ángulo polar de cada punto respecto al centroide.
3. Ordenamiento descendente por ángulo (sentido horario).

Acepta únicamente combinaciones de 3 o 4 puntos.

---

### **4.2 Cálculo de Lados**

**`compute_sides(vertices: list) -> list[float]`**

Devuelve las longitudes de los segmentos consecutivos entre vértices ordenados.

* Utiliza distancia euclidiana.
* Retorna una lista con 3 longitudes (triángulo) o 4 (cuadrilátero).

---

### **4.3 Cálculo de Vectores**

**`compute_vectors(vertices: list) -> list[(dx, dy)]`**

Genera vectores entre vértices consecutivos, utilizados para:

* Detección de ángulos rectos (producto punto ≈ 0)
* Identificación de ángulos agudos (producto punto > 0)

---

### **4.4 Producto Punto**

**`dot(v1, v2) -> float`**

Devuelve el producto punto entre dos vectores en 2D.

Funciones auxiliares:

* `is_perpendicular(v1, v2, tol)` → determina si forma ángulo recto.
* `is_acute(v1, v2)` → determina si forma un ángulo agudo.

---

## 5. Generación de Combinaciones

### **5.1 Combinaciones de 3 puntos**

**`combine_three_points(points) -> list`**

Genera todas las combinaciones únicas de 3 puntos empleando iteración triple.

Complejidad: **O(n³)**.

### **5.2 Combinaciones de 4 puntos**

**`combine_four_points(points) -> list`**

Genera todas las combinaciones únicas de 4 puntos mediante iteración cuádruple.

Complejidad: **O(n⁴)**.

---

## 6. Detección de Figuras

### **6.1 Triángulo Recto**

**`is_right_triangle(points: list) -> bool`**

Condiciones:

* Tres puntos.
* Tras normalización, al menos un par de vectores consecutivos forma un ángulo recto.
* Ángulo recto verificado con producto punto ≈ 0.

Resultado: `True` si la combinación representa un triángulo recto.

---

### **6.2 Triángulo Agudo**

**`is_acute_triangle(points: list) -> bool`**

Condiciones:

* Tres puntos.
* Tras normalización, **todos** los productos punto entre vectores consecutivos deben ser positivos.

Resultado: `True` si todos los ángulos son agudos.

---

### **6.3 Rectángulo**

**`is_rectangle(points: list) -> bool`**

Condiciones:

* Cuatro puntos.
* Normalización obligatoria.
* Ángulos rectos en todos los vértices (producto punto ≈ 0).
* Lados opuestos iguales dentro de una tolerancia fija.

Resultado: `True` si representa un rectángulo válido.

---

### **6.4 Cuadrado**

**`is_square(points: list) -> bool`**

Condiciones:

* La figura debe ser primero un rectángulo.
* Adicionalmente, los cuatro lados deben ser iguales dentro de tolerancia.

Resultado: `True` si representa un cuadrado válido.

---

## 7. Complejidad Global del Módulo

Para una lista de `n` puntos:

* Combinaciones de triángulos → O(n³)
* Combinaciones de cuadriláteros → O(n⁴)
* Cada verificación geométrica → O(1)

En escenarios con cantidades moderadas de puntos, el rendimiento es adecuado y predecible.

---

## 8. Limitaciones Actuales

* No se detectan triángulos obtusos.
* No se incluyen polinomios convexos de más de cuatro lados.
* El sistema depende de tolerancias numéricas fijas (1e-6).
* No se calcula área ni orientación final de las figuras.

---

## 9. Extensibilidad

El diseño permite ampliar fácilmente el catálogo de figuras mediante:

1. Implementación de nuevas funciones de validación.
2. Inserción de la nueva lógica en `detect_shapes`.
3. Creación de nuevos tipos en `FigureType`.
4. Implementación correspondiente en `FigureFactory`.

Figuras potenciales:

* Triángulo obtuso
* Rombo
* Trapecio
* Polígonos convexos genéricos

---

## 10. Conclusión

El módulo `shape_detector` constituye un sistema geométrico robusto, modular y extensible para detección de figuras mediante combinatoria y análisis vectorial. Su estructura bien definida permite integrarlo en aplicaciones de análisis geométrico, simulación, gráficos o educación con mínima fricción y alta confiabilidad.
