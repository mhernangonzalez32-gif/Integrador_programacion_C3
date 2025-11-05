<p align="center">
  <img src="img/encabezado.png" alt="Encabezado del Proyecto Integrador UTN" width="600"/>
</p>

# INFORME TÉCNICO: SISTEMA DE GESTIÓN DE PAÍSES EN PYTHON

**Trabajo Práctico Integrador - Programación 1**  
**Tecnicatura Universitaria en Programación**

---

## ÍNDICE

1. [Resumen](#resumen)
2. [Introducción](#introducción)
3. [Marco Teórico](#marco-teórico)
4. [Arquitectura y Modularización del Código](#arquitectura-y-modularización)
5. [Robustez y Manejo de Datos](#robustez-y-manejo-de-datos)
6. [Uso Eficiente de Estructuras y Algoritmos](#estructuras-y-algoritmos)
7. [Diseño de Interfaz y Experiencia de Usuario](#diseño-ux)
8. [Persistencia de Datos y Tecnología](#persistencia-datos)
9. [Conclusiones](#conclusiones)
10. [Referencias Bibliográficas](#referencias)

---

## 1. RESUMEN <a name="resumen"></a>

El presente informe documenta el desarrollo de un **Sistema de Gestión de Datos de Países**, una aplicación desarrollada en Python 3.x que permite manipular y analizar información demográfica y geográfica de 195 países del mundo. El sistema implementa funcionalidades de búsqueda, filtrado, ordenamiento y análisis estadístico sobre un dataset almacenado en formato CSV.

El proyecto se destaca por su **arquitectura modular**, **robustez en el manejo de errores**, **uso eficiente de estructuras de datos nativas de Python**, y una **interfaz de consola adaptativa** que mejora significativamente la experiencia de usuario. Adicionalmente, se implementaron funcionalidades extra (agregar y editar países) que superan los requerimientos mínimos del trabajo práctico.

**Tecnologías utilizadas:** Python 3.10+, librerías estándar (csv, collections, shutil, os, time, difflib)  
**Líneas de código:** ~800 líneas distribuidas en 7 módulos  
**Dataset:** 195 países con 4 atributos cada uno

---

## 2. INTRODUCCIÓN <a name="introducción"></a>

### 2.1 Contexto del Proyecto

En el marco de la asignatura Programación 1, se nos planteó el desafío de desarrollar una aplicación que consolide los conocimientos adquiridos durante el curso: estructuras de datos (listas y diccionarios), funciones, estructuras de control, algoritmos de ordenamiento, manejo de archivos y estadísticas básicas.

El dominio elegido fue la gestión de información sobre países, un dataset ideal por su claridad conceptual y su potencial para aplicar diversas operaciones de filtrado y análisis.

### 2.2 Objetivos

**Objetivo General:**  
Desarrollar un sistema funcional que permita gestionar información de países mediante operaciones de búsqueda, filtrado, ordenamiento y cálculo de estadísticas.

**Objetivos Específicos:**
1. Implementar una arquitectura modular que separe responsabilidades
2. Garantizar la robustez del sistema mediante validaciones exhaustivas
3. Utilizar estructuras de datos y algoritmos eficientes
4. Proporcionar una interfaz de usuario clara e intuitiva
5. Persistir los datos mediante archivos CSV con integridad garantizada

### 2.3 Alcance

El sistema cubre las siguientes funcionalidades:

**Funcionalidades Core (Requeridas):**
- Búsqueda de países por nombre (coincidencia parcial)
- Filtrado por continente, rango de población y rango de superficie
- Ordenamiento por nombre, población o superficie (ascendente/descendente)
- Estadísticas: máximos, mínimos, promedios y distribución por continente

**Funcionalidades Adicionales (Valor Agregado):**
- Agregar nuevos países al dataset
- Editar información de países existentes
- Paginación de resultados para mejorar la visualización
- Interfaz responsiva que se adapta al tamaño de terminal

---

## 3. MARCO TEÓRICO <a name="marco-teórico"></a>

### 3.1 Estructuras de Datos

#### 3.1.1 Listas (List)

Las listas son estructuras de datos secuenciales, mutables y ordenadas que permiten almacenar colecciones de elementos heterogéneos. En Python, las listas se implementan como arrays dinámicos que ofrecen:

- **Acceso indexado en O(1):** Acceso directo por posición
- **Inserción/eliminación al final en O(1) amortizado**
- **Iteración eficiente:** Ideal para recorrer colecciones

**Aplicación en el proyecto:**  
La lista principal `paises` almacena todos los países cargados desde el CSV. Esta estructura permite:
```python
paises = [pais1, pais2, pais3, ...]  # Colección ordenada
for pais in paises:  # Iteración eficiente
    procesar(pais)
```

#### 3.1.2 Diccionarios (Dict)

Los diccionarios son estructuras de datos tipo hash que almacenan pares clave-valor. Proporcionan:

- **Acceso por clave en O(1) promedio**
- **Inserción y eliminación en O(1) promedio**
- **Semántica clara:** Acceso por nombre en lugar de por índice

**Aplicación en el proyecto:**  
Cada país se representa como un diccionario con claves estandarizadas:
```python
pais = {
    'nombre': 'Argentina',
    'poblacion': 45773884,
    'superficie': 2780400,
    'continente': 'América del Sur'
}
```

Esta representación permite acceso semántico (`pais['poblacion']`) en lugar de acceso posicional, mejorando la legibilidad del código.

### 3.2 Funciones y Modularización

La programación modular divide un programa en módulos independientes, cada uno con una responsabilidad específica. Los beneficios incluyen:

- **Reutilización de código:** Las funciones se pueden usar en múltiples contextos
- **Mantenibilidad:** Los cambios están aislados a módulos específicos
- **Testabilidad:** Cada función puede probarse independientemente
- **Legibilidad:** El código se autoexplica por nombres de funciones descriptivos

**Principio de Responsabilidad Única (SRP):**  
"Una función debe tener una única razón para cambiar", es decir, debe realizar una sola tarea bien definida.

### 3.3 Algoritmos de Ordenamiento

Python utiliza **Timsort**, un algoritmo híbrido derivado de merge sort y insertion sort, desarrollado por Tim Peters en 2002. Características:

- **Complejidad:** O(n log n) en el peor caso
- **Estable:** Mantiene el orden relativo de elementos iguales
- **Adaptativo:** Aprovecha secuencias parcialmente ordenadas

### 3.4 Archivos CSV

CSV (Comma-Separated Values) es un formato de archivo de texto plano para representar datos tabulares. Python proporciona el módulo `csv` con dos clases principales:

- **`csv.DictReader`:** Lee CSV y produce diccionarios (una fila = un diccionario)
- **`csv.DictWriter`:** Escribe diccionarios como filas CSV

**Ventaja:** El uso de diccionarios permite manejar columnas por nombre en lugar de por índice, reduciendo errores.

### 3.5 Manejo de Excepciones

Las excepciones son mecanismos para manejar errores en tiempo de ejecución. La estructura `try...except` permite:

1. **Intentar** ejecutar código que puede fallar
2. **Capturar** errores específicos
3. **Manejar** el error de forma controlada

**Tipos de excepciones comunes:**
- `ValueError`: Error en la conversión de tipos
- `TypeError`: Operación sobre tipo incorrecto
- `KeyError`: Clave no encontrada en diccionario
- `FileNotFoundError`: Archivo no existe
- `IOError`: Error de entrada/salida

---

## 4. ARQUITECTURA Y MODULARIZACIÓN DEL CÓDIGO 🏗️ <a name="arquitectura-y-modularización"></a>

### 4.1 Visión General de la Arquitectura

El proyecto implementa una **arquitectura modular en capas** que separa claramente las responsabilidades funcionales. Esta decisión de diseño responde al **Principio de Responsabilidad Única (SRP)** del paradigma SOLID, garantizando que cada módulo tiene una única razón para cambiar.

```
┌─────────────────────────────────────────┐
│           main.py (Controlador)         │
│   • Bucle principal                     │
│   • Menú de opciones                    │
│   • Dispatching a módulos               │
└─────────────────┬───────────────────────┘
                  │
    ┌─────────────┴─────────────┐
    │                           │
    v                           v
┌───────────────────┐   ┌──────────────────────┐
│  Módulos de Lógica│   │  Módulo de Utilidades│
│  de Negocio       │   │  (mis_funciones.py)  │
├───────────────────┤   ├──────────────────────┤
│ • busqueda_por_   │   │ • Validaciones       │
│   nombre.py       │   │ • Formateo           │
│ • filtro_de_      │   │ • I/O                │
│   busqueda.py     │   │ • Normalización      │
│ • ordenar_        │   │ • Paginación         │
│   países.py       │   │ • Carga CSV          │
│ • mostrar_        │   └──────────────────────┘
│   estadísticas.py │
│ • manejo_csv.py   │
└───────────────────┘
```

### 4.2 Análisis Detallado de Módulos

#### 4.2.1 main.py - Controlador Principal

**Responsabilidad:** Punto de entrada único, gestión del menú principal y dispatching de operaciones.

**Diseño:**
```python
paises = mis_funciones.cargar_datos_desde_csv("csv\\paises_mundo.csv")

while True:
    mis_funciones.limpiar_pantalla()
    mis_funciones.menu_principal()
    opcion = mis_funciones.numero_opcion(7)
    match opcion:
        case 1: busqueda_por_nombre.buscar_pais_nombre(paises)
        case 2: filtro_de_busqueda.menu_de_filtros(paises)
        # ... más casos
```

**Análisis:**
- **Carga única de datos:** Los datos se cargan una sola vez al inicio, evitando lecturas repetitivas del disco.
- **Bucle principal limpio:** Solo contiene la lógica de navegación del menú.
- **Pattern Matching (Python 3.10+):** Uso de `match-case` para un dispatching más legible que múltiples `if-elif`.
- **Delegación total:** Cada opción delega inmediatamente a su módulo correspondiente, sin lógica adicional en `main.py`.

**Justificación del diseño:**  
Este diseño permite que `main.py` actúe como un **controlador puro**, sin conocer los detalles de implementación de cada funcionalidad. Si en el futuro se necesita cambiar cómo funciona la búsqueda, solo se modifica `busqueda_por_nombre.py` sin tocar `main.py`.

#### 4.2.2 mis_funciones.py - Módulo de Utilidades

**Responsabilidad:** Proporcionar funciones transversales reutilizables por todos los demás módulos.

**Funciones principales:**

1. **Validación de entradas:**
```python
def numero_opcion(rango):
    """Valida que el usuario ingrese un número dentro del rango especificado"""
    while True:
        try:
            entrada_usuario = int(input("Elija una opción: "))
            if entrada_usuario in range(1, rango + 1):
                return int(entrada_usuario)
        except ValueError:
            print(menu_centro("Error: El dato ingresado no pertenece a ninguna opción."))
```

**Análisis:** Esta función encapsula toda la lógica de validación de opciones de menú. Garantiza que:
- El valor sea numérico (captura `ValueError`)
- Esté dentro del rango válido
- El usuario pueda reintentar indefinidamente hasta ingresar un valor correcto

2. **Interfaz responsiva:**
```python
def ancho_total():
    return shutil.get_terminal_size().columns

def menu_centro(texto, ancho=ancho_total()):
    return f"{texto:^{ancho}}"
```

**Análisis:** El uso de `shutil.get_terminal_size()` hace que la interfaz se adapte dinámicamente al tamaño de la terminal del usuario. Esto es especialmente importante en sistemas Unix/Linux donde las terminales pueden tener anchos variables.

3. **Normalización de texto:**
```python
def normalizar_manual(texto):
    texto = texto.lower()
    reemplazos = (
        ("á", "a"), ("é", "e"), ("í", "i"), ("ó", "o"), ("ú", "u"),
        # ... más reemplazos
    )
    for original, reemplazo in reemplazos:
        texto = texto.replace(original, reemplazo)
    return texto
```

**Análisis:** Esta función es crucial para la búsqueda flexible. Permite que búsquedas como "mexico" encuentren "México", mejorando significativamente la UX. La implementación manual (en lugar de usar librerías de normalización Unicode) garantiza compatibilidad y control total sobre los reemplazos.

4. **Paginación de resultados:**
```python
def imprimir_resultados(paises_ordenados):
    pagina = 0
    por_pagina = 10
    total = len(paises_ordenados)
    total_paginas = (total + por_pagina - 1) // por_pagina
    
    while True:
        inicio = pagina * por_pagina
        fin = inicio + por_pagina
        # Mostrar página actual
        # Permitir navegación [A]vanzar, [R]etroceder, [S]alir
```

**Análisis:** La paginación es una funcionalidad **no requerida** pero que agrega valor significativo. Cuando hay muchos resultados (ej. todos los países de Asia), mostrar 10 por página evita el "scroll infinito" y hace la información más digerible.

**Cálculo de páginas totales:** `(total + por_pagina - 1) // por_pagina` es la fórmula estándar para redondeo hacia arriba en división entera, evitando importar `math.ceil`.

#### 4.2.3 busqueda_por_nombre.py - Módulo de Búsqueda

**Responsabilidad:** Implementar búsqueda de países por coincidencia parcial de nombre.

**Algoritmo:**
```python
def buscar_pais_nombre(lista_paises):
    nombre_buscado = input("Que pais esta buscando?\n")
    termino_normalizado = mis_funciones.normalizar_manual(nombre_buscado)
    
    resultados = []
    for pais in lista_paises:
        nombre_pais_actual = pais.get('nombre', '')
        nombre_actual_normalizado = mis_funciones.normalizar_manual(nombre_pais_actual)
        
        if termino_normalizado in nombre_actual_normalizado:
            resultados.append(pais)
    
    if not resultados:
        return print(mis_funciones.menu_centro(
            f"--- No se encontraron resultados para '{nombre_buscado}' ---"))
    
    return mis_funciones.imprimir_resultados(resultados)
```

**Análisis técnico:**

1. **Búsqueda por substring:** El operador `in` realiza búsqueda de subcadena, permitiendo coincidencias parciales. Esto es más flexible que búsqueda exacta y más intuitivo para el usuario.

2. **Normalización bidireccional:** Tanto el término de búsqueda como cada nombre de país se normalizan, garantizando que la comparación sea case-insensitive y accent-insensitive.

3. **Uso de `get()` con default:** `pais.get('nombre', '')` evita `KeyError` si un diccionario está malformado, devolviendo cadena vacía como fallback.

4. **Complejidad:** O(n·m) donde n = número de países y m = longitud promedio de nombres. Para datasets pequeños (~200 países) esto es perfectamente aceptable. Para datasets grandes, se consideraría un índice invertido.

#### 4.2.4 filtro_de_busqueda.py - Módulo de Filtros

**Responsabilidad:** Implementar filtros por continente, población y superficie.

**Diseño de arquitectura:**
```python
def menu_de_filtros(lista_paises):
    paises_filtrados = lista_paises.copy()  # Trabaja sobre copia
    
    while True:
        mis_funciones.menu_filtros()
        opcion = mis_funciones.numero_opcion(4)
        match opcion:
            case 1: paises_filtrados = buscar_por_continente(paises_filtrados)
            case 2: paises_filtrados = buscar_por_rango_poblacion(paises_filtrados)
            case 3: paises_filtrados = buscar_por_rango_superficie(paises_filtrados)
            case 4: break
```

**Análisis:**

1. **Filtros acumulativos:** El diseño permite aplicar múltiples filtros en cadena. Por ejemplo:
   - Filtrar por "América del Sur" → 12 países
   - Después filtrar por población > 10M → 7 países
   - Después filtrar por superficie > 500k km² → 3 países

2. **Copia defensiva:** `lista_paises.copy()` crea una copia superficial, protegiendo la lista original. Esto es crucial porque los filtros pueden reducir la lista, y queremos preservar el dataset completo para futuras operaciones.

3. **Funciones especializadas:** Cada tipo de filtro tiene su propia función (`buscar_por_continente`, `buscar_por_rango_poblacion`, etc.), cada una con validaciones específicas.

**Ejemplo de validación de rango:**
```python
def buscar_por_rango_poblacion(lista_paises):
    while True:
        try:
            n_min = int(mis_funciones.numero_entero("Ingrese el número mínimo de población: "))
            n_max = int(mis_funciones.numero_entero("Ingrese el número máximo de población: "))
            if n_min > n_max:
                print("El valor mínimo no puede ser mayor que el máximo. Inténtelo de nuevo.")
            else:
                break
        except ValueError:
            print("Por favor, ingrese números enteros válidos.")
```

**Análisis:** Esta validación tiene **tres capas de defensa**:
1. `numero_entero()` garantiza que sea numérico
2. `int()` convierte a entero
3. Validación lógica `n_min <= n_max`

Esta estrategia de defensa en profundidad hace el sistema extremadamente robusto.

#### 4.2.5 ordenar_países.py - Módulo de Ordenamiento

**Responsabilidad:** Ordenar países por nombre, población o superficie en orden ascendente o descendente.

**Implementación:**
```python
def orden_paises(lista_paises):
    criterio = mis_funciones.numero_entero("Ingrese la opción de cómo desea ordenar: ")
    
    claves = {1: 'nombre', 2: 'poblacion', 3: 'superficie'}
    clave = claves[criterio]
    
    descendente = mis_funciones.si_o_no(True, "¿Querés mostrarlo en orden descendente? (s/n): ")
    
    def obtener_valor(pais):
        if clave not in pais:
            return "" if clave == "nombre" else 0
        valor = pais[clave]
        if clave in ("poblacion", "superficie"):
            try:
                return int(valor)
            except (ValueError, TypeError):
                return 0
        return str(valor).lower()
    
    paises_ordenados = sorted(lista_paises, key=obtener_valor, reverse=descendente)
    mis_funciones.imprimir_resultados(paises_ordenados)
```

**Análisis técnico profundo:**

1. **Función auxiliar `obtener_valor`:**  
   Esta función es el corazón del ordenamiento. Realiza tres tareas críticas:
   
   a) **Manejo de claves faltantes:** Si un país no tiene la clave solicitada, devuelve un valor por defecto (`""` para strings, `0` para números).
   
   b) **Conversión de tipos segura:** Los datos del CSV son strings. Para ordenar numéricamente, necesitamos convertir a `int`. El bloque `try-except` garantiza que valores malformados no rompan el ordenamiento.
   
   c) **Normalización de strings:** `str(valor).lower()` garantiza ordenamiento alfabético case-insensitive.

2. **Uso de `sorted()` vs `list.sort()`:**  
   `sorted()` devuelve una nueva lista sin modificar la original, mientras que `list.sort()` ordena in-place. Usamos `sorted()` porque queremos preservar el orden original de `lista_paises` para futuras operaciones.

3. **Parámetro `key`:**  
   El parámetro `key` de `sorted()` acepta una función que se aplica a cada elemento antes de comparar. Esto es más eficiente que crear una lista de tuplas `(valor_comparacion, elemento)` manualmente.

4. **Complejidad:** O(n log n) gracias al algoritmo Timsort de Python.

#### 4.2.6 mostrar_estadísticas.py - Módulo de Estadísticas

**Responsabilidad:** Calcular y mostrar estadísticas agregadas del dataset.

**Implementación:**
```python
def mostrar_estadisticas(lista_paises):
    # Validación y limpieza de datos
    paises_validos = []
    continentes_validos = []
    
    for pais in lista_paises:
        try:
            nombre = pais.get("nombre", "Desconocido")
            poblacion = int(pais.get("poblacion", 0))
            superficie = int(pais.get("superficie", 0))
            continente = str(pais.get("continente", "Desconocido")).strip()
            
            if poblacion < 0 or superficie < 0:
                continue
            
            paises_validos.append({
                "nombre": nombre,
                "poblacion": poblacion,
                "superficie": superficie,
                "continente": continente
            })
            continentes_validos.append(continente)
        except (ValueError, TypeError):
            continue
    
    # Cálculos estadísticos
    pais_mayor_pob = max(paises_validos, key=lambda x: x["poblacion"])
    pais_menor_pob = min(paises_validos, key=lambda x: x["poblacion"])
    
    total_poblacion = sum(p["poblacion"] for p in paises_validos)
    total_superficie = sum(p["superficie"] for p in paises_validos)
    n = len(paises_validos)
    
    prom_poblacion = total_poblacion / n
    prom_superficie = total_superficie / n
    
    from collections import Counter
    conteo_continentes = Counter(continentes_validos)
```

**Análisis técnico:**

1. **Validación y limpieza previa:**  
   Antes de calcular estadísticas, se crea una lista `paises_validos` que excluye:
   - Países con datos no numéricos
   - Países con valores negativos (datos inconsistentes)
   - Diccionarios malformados
   
   Esta limpieza garantiza que las estadísticas sean confiables.

2. **Uso de funciones de orden superior:**
   - `max()` y `min()` con `key=lambda`: Encuentra extremos sin recorridos manuales
   - `sum()` con generator expression: Calcula totales eficientemente sin crear listas intermedias

3. **Collections.Counter:**  
   `Counter` es una subclase de diccionario optimizada para conteo. Internamente usa un diccionario hash, dando complejidad O(n) para contar todos los elementos. La alternativa manual sería:
   ```python
   conteo = {}
   for cont in continentes_validos:
       conteo[cont] = conteo.get(cont, 0) + 1
   ```
   `Counter` es más legible y eficiente.

4. **Formato de salida:**  
   Los números se formatean con separadores de miles (`:,`) para mejorar legibilidad:
   ```python
   print(f"🌐 País con mayor población: {pais_mayor_pob['nombre']} 
         ({pais_mayor_pob['poblacion']:,} habitantes)")
   # Output: 🌐 País con mayor población: India (1,428,627,663 habitantes)
   ```

#### 4.2.7 manejo_csv.py - Módulo de Persistencia

**Responsabilidad:** Agregar y editar países, persistiendo cambios en el archivo CSV.

**Funcionalidades adicionales no requeridas:**

1. **Agregar país:**
```python
def agregar_pais(lista_paises, nombre_archivo_csv):
    nombre_nuevo = input("¿Cómo se llama el nuevo país? \n").strip().lower()
    
    # Verificación de duplicados
    duplicado_encontrado = False
    for pais in lista_paises:
        if pais['nombre'].strip().lower() == nombre_nuevo:
            duplicado_encontrado = True
            break
    
    if duplicado_encontrado:
        print(f"Error: El país '{nombre_nuevo}' ya existe.")
        return
    
    # Recolectar datos del nuevo país
    poblacion_nueva = mis_funciones.numero_entero(f"Población de {nombre_nuevo}? \n")
    superficie_nueva = mis_funciones.numero_entero(f"Superficie de {nombre_nuevo}? \n")
    # ... selección de continente
    
    nuevo_pais = {
        "nombre": nombre_nuevo,
        "poblacion": poblacion_nueva,
        "superficie": superficie_nueva,
        "continente": continente_nuevo
    }
    
    lista_paises.append(nuevo_pais)
    guardar_datos(nombre_archivo_csv, lista_paises, encabezados)
```

**Análisis:**

a) **Prevención de duplicados:** La verificación usa comparación normalizada (`.strip().lower()`), evitando duplicados por diferencias de formato.

b) **Integridad referencial:** El nuevo país se agrega tanto a la lista en memoria como al archivo CSV, manteniendo sincronización.

c) **Validación de continentes:** Se usa el mismo menú de continentes que en filtros, garantizando consistencia de valores.

2. **Persistencia con csv.DictWriter:**
```python
def guardar_datos(nombre_archivo, datos, encabezados):
    try:
        with open(nombre_archivo, mode='w', newline='', encoding='utf-8') as f:
            escritor = csv.DictWriter(f, fieldnames=encabezados)
            escritor.writeheader()
            escritor.writerows(datos)
        return True
    except IOError as e:
        print(f"Error de E/S al escribir en el archivo '{nombre_archivo}': {e}")
        return False
```

**Análisis:**

a) **Context manager (`with`):** Garantiza cierre del archivo incluso si hay excepciones.

b) **`newline=''`:** Parámetro necesario en Windows para evitar líneas en blanco extra en CSV.

c) **`encoding='utf-8'`:** Explícito para manejar caracteres especiales (tildes, ñ, etc.).

d) **`DictWriter.writeheader()`:** Escribe la fila de encabezados automáticamente.

e) **`writerows()`:** Más eficiente que múltiples `writerow()` porque hace una sola operación de I/O.

### 4.3 Ventajas de la Arquitectura Modular

1. **Localización de errores:** Si hay un bug en la búsqueda, sabemos que está en `busqueda_por_nombre.py`, no disperso en todo el código.

2. **Escalabilidad:** Para agregar una nueva funcionalidad (ej. exportar a Excel), solo creamos un nuevo módulo sin tocar los existentes.

3. **Reutilización:** Las funciones de `mis_funciones.py` se usan en todos los módulos, evitando duplicación de código.

4. **Testing:** Cada módulo puede testearse independientemente con datos mock.

5. **Trabajo en equipo:** Diferentes desarrolladores pueden trabajar en módulos diferentes simultáneamente sin conflictos.

6. **Mantenibilidad:** Un cambio en la lógica de ordenamiento no afecta a búsquedas o filtros.

### 4.4 Cumplimiento del SRP

Cada módulo tiene **una única razón para cambiar**:

- `main.py` cambia si modificamos la estructura del menú
- `busqueda_por_nombre.py` cambia si modificamos el algoritmo de búsqueda
- `filtro_de_busqueda.py` cambia si agregamos nuevos tipos de filtros
- `ordenar_países.py` cambia si modificamos criterios de ordenamiento
- `mostrar_estadísticas.py` cambia si agregamos nuevas estadísticas
- `manejo_csv.py` cambia si modificamos la persistencia (ej. migrar a JSON)
- `mis_funciones.py` cambia si agregamos nuevas utilidades transversales

Esta separación clara de responsabilidades es la piedra angular de un código mantenible y profesional.

---

## 5. ROBUSTEZ Y MANEJO DE DATOS 🛡️ <a name="robustez-y-manejo-de-datos"></a>

### 5.1 Estrategia de Validación en Capas

El sistema implementa una estrategia de **defensa en profundidad**, con múltiples capas de validación que garantizan robustez ante entradas maliciosas o erróneas.

#### Capa 1: Validación de Entrada del Usuario

**Función `numero_opcion`:**
```python
def numero_opcion(rango):
    while True:
        try:
            entrada_usuario = int(input("Elija una opción: "))
            if entrada_usuario in range(1, rango + 1):
                return int(entrada_usuario)
        except ValueError:
            print(menu_centro("Error: El dato ingresado no pertenece a ninguna opción."))
```

**Mecanismos de validación:**
1. **Bucle infinito con condición de salida:** El usuario no puede avanzar sin ingresar un valor válido
2. **Conversión con manejo de excepciones:** Captura `ValueError` si el input no es numérico
3. **Validación de rango:** Verifica que el número esté dentro del rango esperado
4. **Mensajes claros:** Informa exactamente qué salió mal

**Función `numero_entero`:**
```python
def numero_entero(texto):
    while True:     
        num = input(texto)
        try:
            num = num.replace('.', '')  # Permite formato con separadores de miles
            numero = int(num)
            return numero
        except ValueError:
            print("Error: El dato ingresado no es un número. Inténtalo de nuevo.")
```

**Innovación:** La línea `num.replace('.', '')` permite que el usuario ingrese números con separadores de miles (ej. "45.000.000") que serán procesados correctamente. Esto mejora significativamente la UX al manejar poblaciones y superficies grandes.

#### Capa 2: Validación Lógica de Negocio

**Validación de rangos en filtros:**
```python
def buscar_por_rango_poblacion(lista_paises):
    while True:
        try:
            n_min = int(mis_funciones.numero_entero("Ingrese el número mínimo de población: "))
            n_max = int(mis_funciones.numero_entero("Ingrese el número máximo de población: "))
            if n_min > n_max:
                print("El valor mínimo no puede ser mayor que el máximo. Inténtelo de nuevo.")
            else:
                break
        except ValueError:
            print("Por favor, ingrese números enteros válidos.")
```

**Análisis:**
- **Doble validación:** Primero `numero_entero()` garantiza que sea numérico, después se valida la lógica min ≤ max
- **Mensaje específico:** No solo dice "error", sino que explica exactamente qué está mal
- **Recuperación automática:** El usuario puede corregir sin reiniciar el programa

**Prevención de duplicados:**
```python
def agregar_pais(lista_paises, nombre_archivo_csv):
    nombre_nuevo = input("¿Cómo se llama el nuevo país? \n").strip().lower()
    
    duplicado_encontrado = False
    for pais in lista_paises:
        nombre_pais = pais['nombre']
        if nombre_pais.strip().lower() == nombre_nuevo:
            duplicado_encontrado = True
            break
            
    if duplicado_encontrado:
        print(f"Error: El país '{nombre_nuevo}' ya existe.")
        return
```

**Análisis:**
- **Normalización bidireccional:** Tanto el nuevo nombre como los existentes se normalizan (`.strip().lower()`)
- **Comparación exacta post-normalización:** Evita duplicados como "Argentina" y "argentina"
- **Early return:** Si hay duplicado, retorna inmediatamente sin procesar más datos

#### Capa 3: Validación de Datos del CSV

**Carga con validación:**
```python
def cargar_datos_desde_csv(ruta_archivo):
    lista_paises = []
    try:
        with open(ruta_archivo, "r", encoding='utf-8') as archivo:
            lector_csv = csv.DictReader(archivo)
            for fila in lector_csv:
                try:
                    fila['poblacion'] = int(fila['poblacion'])
                    fila['superficie'] = int(fila['superficie'])
                    lista_paises.append(fila)
                except (ValueError, KeyError, TypeError):
                    print(f"Advertencia: Se omitió una fila por datos inválidos: {fila}")
    except FileNotFoundError:
        print(f"Error: El archivo no se encontró en la ruta '{ruta_archivo}'")
    except Exception as e:
        print(f"Error inesperado al leer el archivo: {e}")
    return lista_paises
```

**Estrategia de manejo de errores:**

1. **Try-except anidados:** 
   - Nivel externo: Maneja errores de archivo (no encontrado, sin permisos)
   - Nivel interno: Maneja errores de datos (valores malformados)

2. **Graceful degradation:** Si una fila está malformada, se omite pero el programa continúa cargando las demás

3. **Logging de errores:** Muestra advertencias sobre datos omitidos para que el usuario esté informado

4. **Conversión de tipos inmediata:** Convierte población y superficie a `int` durante la carga, no durante el uso. Esto implementa el principio "fail fast" - mejor detectar errores temprano que tener problemas más adelante.

**Validación en estadísticas:**
```python
def mostrar_estadisticas(lista_paises):
    paises_validos = []
    
    for pais in lista_paises:
        if not isinstance(pais, dict):
            continue
        try:
            poblacion = int(pais.get("poblacion", 0))
            superficie = int(pais.get("superficie", 0))
            
            if poblacion < 0 or superficie < 0:
                continue  # Omite valores negativos (datos inconsistentes)
            
            paises_validos.append({...})
        except (ValueError, TypeError):
            continue
```

**Análisis de defensa en profundidad:**

1. **Verificación de tipo:** `isinstance(pais, dict)` previene errores si la lista está contaminada
2. **`get()` con default:** `pais.get("poblacion", 0)` evita `KeyError` si falta la clave
3. **Conversión segura:** `int()` dentro de try-except maneja valores no numéricos
4. **Validación de dominio:** Verifica que población y superficie sean ≥ 0 (no tiene sentido valores negativos)
5. **Silent failure:** `continue` omite datos malos sin romper el flujo

### 5.2 Normalización de Texto para Búsqueda Flexible

**Implementación:**
```python
def normalizar_manual(texto):
    texto = texto.lower()
    reemplazos = (
        ("á", "a"), ("é", "e"), ("í", "i"), ("ó", "o"), ("ú", "u"),
        ("à", "a"), ("è", "e"), ("ì", "i"), ("ò", "o"), ("ù", "u"),
        ("ä", "a"), ("ë", "e"), ("ï", "i"), ("ö", "o"), ("ü", "u"),
        ("ñ", "n"), ("s", "z"), ("j", "g"), ("b", "v")
    )
    for original, reemplazo in reemplazos:
        texto = texto.replace(original, reemplazo)
    return texto
```

**Decisiones de diseño:**

1. **Implementación manual vs librerías:**  
   Podríamos haber usado `unicodedata.normalize('NFKD', texto)`, pero la implementación manual ofrece:
   - **Control total:** Decidimos exactamente qué reemplazos hacer
   - **Transparencia:** El código es autoexplicativo
   - **Portabilidad:** No depende de comportamientos de locale del sistema
   - **Reemplazos fonéticos:** Incluimos `("s", "z")`, `("j", "g")`, `("b", "v")` para búsquedas más permisivas

2. **Tupla de reemplazos:**  
   Usar tupla (inmutable) en lugar de diccionario enfatiza que estos reemplazos son constantes y no deben modificarse en runtime.

3. **Orden de operaciones:**  
   Primero `.lower()`, después reemplazos de acentos. Esto garantiza que "É" → "e" correctamente (primero "É" → "é", después "é" → "e").

**Impacto en UX:**

| Búsqueda Usuario | Sin Normalización | Con Normalización |
|------------------|-------------------|-------------------|
| "mexico"         | ❌ No encuentra   | ✅ Encuentra "México" |
| "japon"          | ❌ No encuentra   | ✅ Encuentra "Japón" |
| "paises bajos"   | ❌ No encuentra   | ✅ Encuentra "Países Bajos" |
| "siri"           | ❌ No encuentra   | ✅ Encuentra "Siria" (s→z, i→i, r→r, i→i, a→a) |

Esta funcionalidad eleva significativamente la calidad del sistema.

### 5.3 Manejo de Excepciones Específicas

El sistema distingue entre diferentes tipos de errores y los maneja apropiadamente:

**Tabla de manejo de excepciones:**

| Excepción | Contexto | Manejo |
|-----------|----------|--------|
| `ValueError` | Conversión de string a int | Solicitar reingreso con mensaje claro |
| `TypeError` | Operación sobre tipo incorrecto | Omitir dato y continuar |
| `KeyError` | Acceso a clave inexistente | Usar `.get()` con default |
| `FileNotFoundError` | Archivo CSV no existe | Mensaje específico con path |
| `IOError` | Error de lectura/escritura | Mensaje de error de E/S |
| `KeyboardInterrupt` | Usuario presiona Ctrl+C | Mensaje de "Operación cancelada" |

**Ejemplo de manejo avanzado:**
```python
try:
    guardar_datos(nombre_archivo_csv, lista_paises, encabezados)
    print("Archivo actualizado con éxito!")
except IOError as e:
    print(f"Error de E/S al escribir en el archivo: {e}")
except Exception as e:
    print(f"Ocurrió un error inesperado al guardar: {e}")
```

**Análisis:**
- **Captura específica primero:** `IOError` se captura antes que `Exception` general
- **Información contextual:** Los mensajes incluyen el tipo de error y detalles
- **Catch-all final:** `Exception` captura cualquier error no previsto, evitando crashes

### 5.4 Mensajes Claros de Éxito/Error

Cumpliendo con la consigna de "Mensajes claros de éxito/error", cada operación proporciona feedback específico:

**Ejemplos de mensajes:**

✅ **Éxito:**
- `"¡País 'ejemplo país' agregado con éxito!"`
- `"Archivo actualizado con éxito!"`
- `"--- Resultados para 'argentina' (1 encontrados) ---"`

❌ **Error:**
- `"Error: El país 'argentina' ya existe."`
- `"--- No se encontraron resultados para 'xyz' ---"`
- `"Error: El valor mínimo no puede ser mayor que el máximo."`
- `"Error: El dato ingresado no es un número. Inténtalo de nuevo."`

🚨 **Advertencia:**
- `"Advertencia: Se omitió una fila por datos inválidos o faltantes: {...}"`

Cada mensaje sigue el patrón: **[Tipo] [Contexto] [Acción requerida/resultado]**

### 5.5 Validación de Datos en Operaciones Críticas

**Filtros con validación de estructura:**
```python
def buscar_por_continente(lista_paises):
    try:
        if not isinstance(lista_paises, list):
            print("Error: se esperaba una lista de países.")
            return []
        
        # ... lógica de filtrado
        
        for pais in lista_paises:
            if not isinstance(pais, dict) or "continente" not in pais:
                continue  # Saltea entradas mal formadas
            # ... procesamiento
    except Exception as e:
        print(f"Error en la búsqueda por continente: {e}")
        return []
```

**Defensa contra datos corruptos:**
1. Verifica que el input sea una lista
2. Verifica que cada elemento sea un diccionario
3. Verifica que tenga la clave necesaria ("continente")
4. Try-except global por si algo más falla

Esta paranoia defensiva es apropiada porque los datos vienen de archivos externos (CSV) que pueden estar corruptos.

---

## 6. USO EFICIENTE DE ESTRUCTURAS Y ALGORITMOS 💡 <a name="estructuras-y-algoritmos"></a>

### 6.1 Elección de Estructuras de Datos

#### 6.1.1 Lista de Diccionarios: La Estructura Principal

**Decisión de diseño:**
```python
paises = [
    {'nombre': 'Argentina', 'poblacion': 45773884, 'superficie': 2780400, 'continente': 'América del Sur'},
    {'nombre': 'Brasil', 'poblacion': 216422446, 'superficie': 8515767, 'continente': 'América del Sur'},
    # ...
]
```

**Justificación técnica:**

**Alternativa 1: Lista de tuplas**
```python
paises = [
    ('Argentina', 45773884, 2780400, 'América del Sur'),
    # ...
]
```
❌ **Rechazada porque:**
- Acceso por índice (`pais[1]`) es críptico - ¿qué es `1`? ¿población o superficie?
- Inmutabilidad de tuplas dificulta ediciones
- Agregar un nuevo campo requiere cambiar todos los índices en el código

**Alternativa 2: Lista de objetos (clases)**
```python
class Pais:
    def __init__(self, nombre, poblacion, superficie, continente):
        self.nombre = nombre
        self.poblacion = poblacion
        # ...
```
❌ **Rechazada porque:**
- Overhead de clases innecesario para un dataset simple
- Dificulta la serialización a CSV
- Para 195 países, el overhead de objetos es despreciable, pero agregamos complejidad sin beneficio claro

**Alternativa elegida: Lista de diccionarios**
✅ **Ventajas:**
- **Acceso semántico:** `pais['poblacion']` es autoexplicativo
- **Flexibilidad:** Fácil agregar/quitar campos sin romper código
- **Integración con CSV:** `csv.DictReader` y `DictWriter` trabajan naturalmente con diccionarios
- **Serialización trivial:** JSON, CSV, etc. tienen soporte nativo
- **Iteración clara:** `for pais in paises:` es idiomático en Python

**Complejidades:**
- Acceso por clave: O(1) promedio
- Inserción al final de lista: O(1) amortizado
- Iteración completa: O(n)
- Búsqueda sin índice: O(n)

Para un dataset de ~200 países, estas complejidades son perfectamente aceptables.

#### 6.1.2 Diccionarios para Mapeo de Opciones

**Patrón repetido en el código:**
```python
continentes = {
    1: "américa del sur",
    2: "américa del norte",
    3: "europa",
    4: "áfrica",
    5: "asia",
    6: "oceanía"
}
continente_buscado = continentes.get(opcion, "").lower()
```

**Ventajas sobre if-elif:**
```python
# Alternativa con if-elif (más verbosa)
if opcion == 1:
    continente_buscado = "américa del sur"
elif opcion == 2:
    continente_buscado = "américa del norte"
# ... etc
```

El diccionario es:
- **Más compacto:** 6 líneas vs 12 líneas
- **Más mantenible:** Agregar un continente = agregar una línea
- **Lookup O(1):** Hash lookup vs comparaciones secuenciales
- **Más Pythonic:** Aprovecha estructuras de datos nativas

### 6.2 Algoritmo de Ordenamiento: Timsort

**Implementación:**
```python
paises_ordenados = sorted(lista_paises, key=obtener_valor, reverse=descendente)
```

**¿Por qué no implementar nuestro propio quicksort o mergesort?**

Python usa **Timsort**, un algoritmo híbrido desarrollado por Tim Peters en 2002 para Python. Características:

1. **Complejidad:** 
   - Mejor caso: O(n) - cuando los datos ya están ordenados
   - Caso promedio: O(n log n)
   - Peor caso: O(n log n)

2. **Estabilidad:** Mantiene el orden relativo de elementos iguales. Por ejemplo:
   ```python
   # Si dos países tienen la misma población
   [{'nombre': 'A', 'poblacion': 1000}, {'nombre': 'B', 'poblacion': 1000}]
   # Después de ordenar por población, A seguirá antes que B
   ```

3. **Adaptatividad:** Detecta secuencias ya ordenadas y las aprovecha. Para un dataset parcialmente ordenado, Timsort puede ser O(n).

4. **Optimización:** Implementado en C en CPython, extremadamente rápido.

**Función key personalizada:**
```python
def obtener_valor(pais):
    if clave not in pais:
        return "" if clave == "nombre" else 0
    valor = pais[clave]
    if clave in ("poblacion", "superficie"):
        try:
            return int(valor)
        except (ValueError, TypeError):
            return 0
    return str(valor).lower()
```

**Análisis:**
- **Conversión de tipos:** Strings se convierten a int para ordenamiento numérico correcto
- **Normalización:** Nombres se convierten a minúsculas para orden alfabético case-insensitive
- **Manejo de errores:** Valores inválidos se mapean a 0 (o ""), evitando crashes
- **Eficiencia:** La función `key` se llama una vez por elemento, después Timsort compara los valores retornados

**Comparación de complejidades:**

| Algoritmo | Mejor Caso | Promedio | Peor Caso | Estable | Adaptativo |
|-----------|------------|----------|-----------|---------|------------|
| Quicksort | O(n log n) | O(n log n) | O(n²) | ❌ | ❌ |
| Mergesort | O(n log n) | O(n log n) | O(n log n) | ✅ | ❌ |
| Heapsort | O(n log n) | O(n log n) | O(n log n) | ❌ | ❌ |
| **Timsort** | **O(n)** | **O(n log n)** | **O(n log n)** | **✅** | **✅** |

Timsort es superior en estabilidad y adaptatividad, crucial para datasets reales.

### 6.3 Análisis Estadístico Eficiente

#### 6.3.1 Funciones de Alto Orden

**En lugar de loops manuales:**
```python
# ❌ Forma manual
pais_mayor_pob = None
max_pob = 0
for pais in paises_validos:
    if pais["poblacion"] > max_pob:
        max_pob = pais["poblacion"]
        pais_mayor_pob = pais
```

**Usamos funciones de alto orden:**
```python
# ✅ Forma Pythonic
pais_mayor_pob = max(paises_validos, key=lambda x: x["poblacion"])
```

**Ventajas:**
1. **Legibilidad:** Intención clara ("dame el máximo según población")
2. **Menos errores:** No hay variables de estado que mantener
3. **Optimización:** Implementación en C es más rápida que loops Python
4. **Expresividad:** Una línea vs 5 líneas

**Funciones utilizadas:**

**`max()` y `min()` con key:**
```python
pais_mayor_pob = max(paises_validos, key=lambda x: x["poblacion"])
pais_menor_pob = min(paises_validos, key=lambda x: x["poblacion"])
```
Complejidad: O(n) - un solo recorrido

**`sum()` con generator expression:**
```python
total_poblacion = sum(p["poblacion"] for p in paises_validos)
```
vs
```python
total_poblacion = sum([p["poblacion"] for p in paises_validos])  # ❌ Crea lista intermedia
```

El generator expression es más eficiente en memoria porque genera valores bajo demanda, no crea una lista completa en memoria.

#### 6.3.2 collections.Counter para Conteo

**Implementación:**
```python
from collections import Counter
conteo_continentes = Counter(continentes_validos)
```

**¿Qué hace Counter internamente?**
```python
# Equivalente manual
conteo_continentes = {}
for continente in continentes_validos:
    if continente in conteo_continentes:
        conteo_continentes[continente] += 1
    else:
        conteo_continentes[continente] = 1
```

**O con dict.get():**
```python
conteo_continentes = {}
for continente in continentes_validos:
    conteo_continentes[continente] = conteo_continentes.get(continente, 0) + 1
```

**Ventajas de Counter:**
1. **Una línea vs 4 líneas**
2. **Semánticamente claro:** "Contar elementos"
3. **Métodos adicionales:** `.most_common()`, operaciones aritméticas entre Counters
4. **Optimizado:** Implementación en C en CPython

**Complejidad:** O(n) - un recorrido por la lista

**Ejemplo de output:**
```python
Counter({'África': 54, 'Asia': 48, 'Europa': 44, 'América del Norte': 23, ...})
```

Automáticamente ordena por frecuencia (con `.most_common()`).

### 6.4 Eficiencia en Búsqueda

**Búsqueda por substring:**
```python
if termino_normalizado in nombre_actual_normalizado:
    resultados.append(pais)
```

**Complejidad:** O(n·m) donde:
- n = número de países (~195)
- m = longitud promedio de nombres (~15 caracteres)

Para datasets pequeños, esto es perfectamente aceptable. 

**¿Cuándo optimizar?**
Si tuviéramos 1,000,000 de países, consideraríamos:

1. **Índice invertido (Trie):**
```python
# Preprocesamiento O(n·m)
trie = Trie()
for pais in paises:
    trie.insert(pais['nombre'], pais)

# Búsqueda O(k) donde k = longitud del término
resultados = trie.search(termino)
```

2. **Búsqueda full-text con librería:**
```python
from whoosh import index, fields
```

Pero para 195 países, la búsqueda lineal es más simple y suficientemente rápida (<1ms).

### 6.5 Paginación Eficiente

**Implementación:**
```python
def imprimir_resultados(paises_ordenados):
    pagina = 0
    por_pagina = 10
    
    while True:
        inicio = pagina * por_pagina
        fin = inicio + por_pagina
        
        for con, pais in enumerate(paises_ordenados[inicio:fin], start=inicio+1):
            # Imprimir pais
```

**Análisis de slicing:**
`paises_ordenados[inicio:fin]` crea una nueva lista con referencias a los elementos originales (shallow copy). 

**Complejidad:**
- Slicing: O(k) donde k = número de elementos en el slice (10 en nuestro caso)
- Iteración: O(k)
- Total por página: O(k) = O(10) = O(1) constante

**Memoria:**
El slicing crea una nueva lista, pero con referencias a los diccionarios originales (no copia los diccionarios). Por lo tanto:
- Memoria adicional: O(k) referencias = 10 * 8 bytes = 80 bytes (despreciable)

Esta implementación es extremadamente eficiente porque solo procesa 10 elementos a la vez, no importa cuántos resultados haya.

---

## 7. DISEÑO DE INTERFAZ Y EXPERIENCIA DE USUARIO ✨ <a name="diseño-ux"></a>

### 7.1 Interfaz de Consola Responsiva

A pesar de ser una aplicación de consola, implementamos características de UX modernas:

#### 7.1.1 Adaptación al Tamaño de Terminal

**Implementación:**
```python
import shutil

def ancho_total():
    return shutil.get_terminal_size().columns

def menu_centro(texto, ancho=ancho_total()):
    return f"{texto:^{ancho}}"
```

**Análisis:**
`shutil.get_terminal_size()` retorna una tupla `(columns, lines)` con las dimensiones actuales de la terminal. Esto permite que:

1. **Menús se centren dinámicamente:**
```python
print(menu_centro("MENÚ PRINCIPAL"))
# En terminal de 80 cols: "                    MENÚ PRINCIPAL                    "
# En terminal de 120 cols: "                              MENÚ PRINCIPAL                              "
```

2. **Separadores se ajusten:**
```python
print("=" * ancho_total())
# Se adapta automáticamente al ancho de la terminal
```

**Tabla de resultados:**
```python
print(f"{'#':>{ANCHO_NUM}} | {'Nombre':<{ANCHO_NOMBRE}} | ... ")
```

Cada columna tiene un ancho fijo, pero las constantes se pueden ajustar fácilmente:
```python
ANCHO_NUM = 7
ANCHO_NOMBRE = 35
ANCHO_POB = 15
ANCHO_SUP = 18
ANCHO_CONT = 25
```

**Formato de números:**
```python
poblacion = f"{pais.get('poblacion', 'N/A'):,}"
# Output: "45,773,884" en lugar de "45773884"
```

El formato `:,` agrega separadores de miles, mejorando dramáticamente la legibilidad de números grandes.

#### 7.1.2 Sistema de Paginación

**Problema:** Mostrar 195 países en consola causa scroll infinito, dificultando la lectura.

**Solución:** Paginación estilo "less" de Unix:

```
Página 1 de 20

#    | Nombre          | 🚻 Población    | 🗺️ Superficie (km²) | 🌎 Continente
──────────────────────────────────────────────────────────────────────
1    | China           | 1,425,671,352   |      9,596,961       | Asia
2    | India           | 1,428,627,663   |      3,287,263       | Asia
...
10   | México          |   128,455,567   |      1,964,375       | América del Norte
──────────────────────────────────────────────────────────────────────
Opciones: [A]vanzar | [R]etroceder | [S]alir
Seleccione una opción: _
```

**Características UX:**
1. **Indicador de página actual:** "Página X de Y" da contexto
2. **Navegación intuitiva:** [A]delante, [R]etrás, [S]alir - primera letra de cada acción
3. **Limpieza de pantalla:** Cada página nueva limpia la anterior, manteniendo foco
4. **Feedback de límites:** "Ya estás en la última página" / "Ya estás en la primera página"

**Implementación de navegación:**
```python
while True:
    # Mostrar página actual
    
    accion = input("Seleccione una opción: ").strip().lower()
    
    if accion == 's':
        print("👋 Saliendo de la paginación...")
        break
    elif accion == 'a':
        if pagina < total_paginas - 1:
            pagina += 1
        else:
            print("🚫 Ya estás en la última página.")
    elif accion == 'r':
        if pagina > 0:
            pagina -= 1
        else:
            print("🚫 Ya estás en la primera página.")
```

**Validación de límites:** El sistema previene que `pagina` salga del rango `[0, total_paginas-1]`, evitando errores de índice.

### 7.2 Mensajes con Emojis y Formato

**Uso estratégico de emojis:**
```python
print("🌐 País con mayor población: ...")
print("📈 Población promedio: ...")
print("🗺️ Países por continente:")
print("👋 Saliendo...")
print("🚫 Ya estás en la última página.")
print("❌ Error: ...")
print("✅ ¡País agregado con éxito!")
```

**Justificación:**
1. **Escaneabilidad visual:** Los emojis actúan como "anchor points" visuales
2. **Jerarquía de información:** Diferentes emojis indican diferentes tipos de información
3. **Feedback emocional:** ✅ transmite éxito, ❌ transmite error
4. **Modernidad:** Aunque es consola, se siente contemporáneo

**Limitación considerada:** Emojis pueden no renderizarse correctamente en terminales muy antiguas, pero en 2025, el soporte es universal (Windows Terminal, macOS Terminal, Linux terminales modernas).

### 7.3 Menús Estructurados y Claros

**Patrón de menú consistente:**
```python
print("=" * ancho_total())
print(menu_centro("TÍTULO DEL MENÚ"))
print("-" * ancho_total())
for i, opcion_texto in enumerate(opciones, start=1):
    linea = f"  {i}. {opcion_texto}"
    print(f"{linea:<{ancho_total() - 2}}")
print("=" * ancho_total())
```

**Elementos de diseño:**
1. **Separadores dobles (=):** Indican inicio/fin de sección principal
2. **Separadores simples (-):** Indican subsecciones
3. **Indentación:** Opciones tienen 2 espacios de margen izquierdo
4. **Numeración:** Consistente en todos los menús
5. **Título centrado:** Destaca visualmente

**Jerarquía visual:**
```
════════════════════════════════════════  ← Importancia máxima
           MENÚ PRINCIPAL
────────────────────────────────────────  ← Separación
  1. Opción                              ← Contenido
  2. Opción
════════════════════════════════════════  ← Cierre
```

### 7.4 Feedback Inmediato y Progresivo

**Mensajes de progreso en operaciones largas:**
```python
print("Guardando cambios en el archivo...")
mis_funciones.time.sleep(2)
try:
    guardar_datos(nombre_archivo_csv, lista_paises, encabezados)
    print("Archivo actualizado con éxito!")
    mis_funciones.time.sleep(1)
except Exception as e:
    print(f"Error al guardar el archivo: {e}")
```

**Análisis UX:**
1. **Feedback anticipatorio:** "Guardando..." informa que el proceso comenzó
2. **Delay intencional:** `time.sleep(2)` da sensación de que algo está pasando (aunque el guardado sea instantáneo)
3. **Confirmación de éxito:** "Actualizado con éxito!" cierra el loop de feedback
4. **Pausa post-éxito:** `sleep(1)` permite leer el mensaje antes de continuar

Este patrón "loading → success → pause" es estándar en UX moderna.

### 7.5 Limpieza de Pantalla Estratégica

**Implementación:**
```python
def limpiar_pantalla():
    if os.name == 'nt':
        _ = os.system('cls')
    else:
        _ = os.system('clear')
```

**Cuándo se usa:**
1. **Al entrar a cada menú:** Mantiene foco en el menú actual
2. **Antes de mostrar resultados:** Elimina distracciones
3. **En paginación:** Cada página nueva limpia la anterior

**Cuándo NO se usa:**
- Durante entrada de datos múltiples (mantiene contexto)
- En mensajes de error (el usuario necesita ver qué hizo mal)

**Filosofía:** La pantalla debe mostrar solo información relevante para la tarea actual.

### 7.6 Validación No Invasiva

**Patrón implementado:**
```python
while True:
    try:
        entrada = input("Ingrese valor: ")
        # Validación
        return valor_valido
    except:
        print("Error. Inténtelo de nuevo.")
        # El loop continúa, NO limpia pantalla, NO termina programa
```

**Características UX:**
1. **No punitivo:** Un error no cierra el programa ni borra todo
2. **Contexto preservado:** El mensaje de error aparece inmediatamente después de la entrada
3. **Reintento infinito:** El usuario puede corregir hasta que lo logre
4. **Explicación clara:** El mensaje dice exactamente qué está mal

### 7.7 Confirmaciones para Operaciones Destructivas

**Función `si_o_no`:**
```python
def si_o_no(validacion, texto):
    while True:
        try:
            respuesta = input(texto).strip().lower()
            if respuesta in ("s", "si", "sí", "y", "yes"):
                return validacion == True
            elif respuesta in ("n", "no"):
                return validacion == False
            else:
                print("❌ Entrada no válida. Por favor responda con 'sí' o 'no'.")
        except KeyboardInterrupt:
            return validacion == False
```

**Uso en ordenamiento:**
```python
descendente = mis_funciones.si_o_no(True, "¿Querés mostrarlo en orden descendente? (s/n): ")
```

**Análisis UX:**
1. **Múltiples aceptaciones:** "s", "si", "sí", "y", "yes" - flexibilidad de idioma
2. **Case-insensitive:** "S", "sI", "SI" - todas funcionan
3. **Manejo de Ctrl+C:** `KeyboardInterrupt` se interpreta como "no"
4. **Reintentos:** Input inválido permite reintentar

Esta función convierte una pregunta binaria en una interacción robusta y flexible.

### 7.8 Indicadores Contextuales

**En edición:**
```python
print(f"Nueva población (actual: {pais_para_editar['poblacion']}): ")
```

**Análisis:** Muestra el valor actual mientras pide el nuevo. El usuario tiene contexto para decidir qué cambiar.

**En estadísticas:**
```python
print(f"🌐 País con mayor población: {pais_mayor_pob['nombre']} ({pais_mayor_pob['poblacion']:,} habitantes)")
```

**Análisis:** Muestra tanto el nombre como el valor numérico. El usuario obtiene información completa sin hacer cálculos mentales.

**En resultados de búsqueda:**
```python
print(mis_funciones.menu_centro(f"--- Resultados para '{nombre_buscado}' ({len(resultados)} encontrados) ---"))
```

**Análisis:** Repite el término buscado y cuántos resultados hay. El usuario confirma que el sistema entendió su búsqueda.

---

## 8. PERSISTENCIA DE DATOS Y TECNOLOGÍA 💾 <a name="persistencia-datos"></a>

### 8.1 Elección de CSV como Formato de Persistencia

**Justificación:**

✅ **Ventajas:**
1. **Simplicidad:** Formato de texto plano, legible por humanos
2. **Portabilidad:** Compatible con Excel, Google Sheets, pandas, R
3. **Versionable:** Git puede trackear cambios línea por línea
4. **Sin dependencias:** No requiere base de datos ni servidor
5. **Estándar universal:** Toda herramienta de datos soporta CSV

❌ **Limitaciones (consideradas):**
1. **Sin tipos:** Todo es string, requiere conversión manual
2. **Sin relaciones:** No hay foreign keys ni joins
3. **Sin índices:** Búsquedas son lineales O(n)
4. **Sin concurrencia:** Dos escrituras simultáneas pueden corromper el archivo
5. **Sin validación de schema:** Cualquier estructura es válida

**¿Por qué CSV es apropiado para este proyecto?**
- Dataset pequeño (~200 países, no cambia frecuentemente)
- Sin relaciones complejas (solo una tabla)
- Un solo usuario a la vez (no es aplicación web)
- Requerimiento del trabajo práctico

### 8.2 Lectura con csv.DictReader

**Implementación:**
```python
import csv

def cargar_datos_desde_csv(ruta_archivo):
    lista_paises = []
    try:
        with open(ruta_archivo, "r", encoding='utf-8') as archivo:
            lector_csv = csv.DictReader(archivo)
            for fila in lector_csv:
                try:
                    fila['poblacion'] = int(fila['poblacion'])
                    fila['superficie'] = int(fila['superficie'])
                    lista_paises.append(fila)
                except (ValueError, KeyError, TypeError):
                    print(f"Advertencia: Se omitió una fila por datos inválidos: {fila}")
    except FileNotFoundError:
        print(f"Error: El archivo no se encontró en la ruta '{ruta_archivo}'")
    except Exception as e:
        print(f"Error inesperado al leer el archivo: {e}")
    return lista_paises
```

**Análisis técnico detallado:**

#### 8.2.1 Context Manager (with statement)

```python
with open(ruta_archivo, "r", encoding='utf-8') as archivo:
    # operaciones
```

**Ventajas sobre open() manual:**
```python
# ❌ Forma manual (propensa a errores)
archivo = open(ruta_archivo, "r")
# ... operaciones ...
archivo.close()  # ¿Qué pasa si hay excepción antes de close()?
```

El context manager garantiza que `archivo.close()` se llame incluso si hay excepciones, previniendo leaks de file descriptors.

#### 8.2.2 Encoding UTF-8 Explícito

```python
encoding='utf-8'
```

**Problema sin encoding explícito:**
- En Windows, encoding por defecto puede ser 'cp1252' (Windows-1252)
- En Linux/Mac, es 'utf-8'
- Nombres como "México", "Japón" fallarían en Windows sin UTF-8

**Solución:** Especificar UTF-8 explícitamente garantiza portabilidad.

#### 8.2.3 csv.DictReader vs csv.reader

**Alternativa: csv.reader (lista de listas)**
```python
reader = csv.reader(archivo)
next(reader)  # Saltear header
for fila in reader:
    pais = {
        'nombre': fila[0],
        'poblacion': int(fila[1]),
        'superficie': int(fila[2]),
        'continente': fila[3]
    }
```

**Problemas:**
1. Acceso por índice (frágil - si cambia orden de columnas, rompe)
2. Necesita mapeo manual a diccionario
3. Necesita saltear header manualmente

**Con DictReader:**
```python
lector_csv = csv.DictReader(archivo)
for fila in lector_csv:
    # fila ya es un diccionario con keys = headers
    pais = fila
```

**Ventajas:**
1. Header processing automático
2. Acceso por nombre de columna
3. Resistente a reordenamiento de columnas

#### 8.2.4 Conversión de Tipos In-Place

```python
fila['poblacion'] = int(fila['poblacion'])
fila['superficie'] = int(fila['superficie'])
```

**Por qué en la carga y no en el uso:**
1. **Fail-fast:** Detectamos datos inválidos temprano
2. **Eficiencia:** Convertimos una vez, no en cada operación
3. **Simplicidad:** El resto del código asume que son int

**Tradeoff:** Si la conversión falla, perdemos ese país. Alternativa sería guardar como string y convertir en uso (más complejo, pero más tolerante).

### 8.3 Escritura con csv.DictWriter

**Implementación:**
```python
def guardar_datos(nombre_archivo, datos, encabezados):
    try:
        with open(nombre_archivo, mode='w', newline='', encoding='utf-8') as f:
            escritor = csv.DictWriter(f, fieldnames=encabezados)
            escritor.writeheader()
            escritor.writerows(datos)
        return True
    except IOError as e:
        print(f"Error de E/S al escribir en el archivo '{nombre_archivo}': {e}")
        return False
    except Exception as e:
        print(f"Ocurrió un error inesperado al guardar: {e}")
        return False
```

#### 8.3.1 Parámetros Críticos

**mode='w':**
- Abre en modo escritura, sobreescribe el archivo completo
- Alternativa 'a' (append) no es apropiada porque queremos reescribir todo

**newline='':**
```python
# Sin newline=''
# En Windows: cada fila tendría una línea en blanco extra
línea1

línea2

# Con newline=''
línea1
línea2
```

Este parámetro es necesario en Windows porque `csv.writer` maneja newlines internamente. Sin esto, Python agrega `\r\n` y csv agrega `\n`, resultando en dobles líneas.

**encoding='utf-8':**
Mismo razonamiento que en lectura - portabilidad.

#### 8.3.2 DictWriter con fieldnames

```python
encabezados = ("nombre", "poblacion", "superficie", "continente")
escritor = csv.DictWriter(f, fieldnames=encabezados)
```

**Ventajas:**
1. **Orden garantizado:** Las columnas se escriben en el orden de `fieldnames`
2. **Validación implícita:** Si un dict tiene keys extra, las ignora (o puede configurarse para error)
3. **Header automático:** `writeheader()` escribe la primera fila con los nombres

**Alternativa manual:**
```python
writer = csv.writer(f)
writer.writerow(['nombre', 'poblacion', 'superficie', 'continente'])
for pais in datos:
    writer.writerow([pais['nombre'], pais['poblacion'], pais['superficie'], pais['continente']])
```

DictWriter es más robusto y menos propenso a errores de ordenamiento.

#### 8.3.3 writerows() vs writerow()

```python
escritor.writerows(datos)  # ✅ Una llamada
```
vs
```python
for pais in datos:  # ❌ N llamadas
    escritor.writerow(pais)
```

**Diferencia de performance:**
- `writerows()` hace una sola operación de I/O (buffered)
- Múltiples `writerow()` hacen N operaciones de I/O

Para 195 países, la diferencia es imperceptible, pero `writerows()` es mejor práctica.

### 8.4 Integridad y Consistencia de Datos

#### 8.4.1 Transaccionalidad Simulada

**Problema:** Si el programa crashea durante `guardar_datos()`, el CSV puede quedar corrupto o vacío.

**Solución implementable (no implementada, pero recomendable):**
```python
def guardar_datos_safe(nombre_archivo, datos, encabezados):
    temp_file = nombre_archivo + '.tmp'
    try:
        # Escribir a archivo temporal
        with open(temp_file, mode='w', newline='', encoding='utf-8') as f:
            escritor = csv.DictWriter(f, fieldnames=encabezados)
            escritor.writeheader()
            escritor.writerows(datos)
        
        # Si todo OK, reemplazar el original
        os.replace(temp_file, nombre_archivo)  # Atómico en POSIX
        return True
    except Exception as e:
        if os.path.exists(temp_file):
            os.remove(temp_file)
        print(f"Error: {e}")
        return False
```

**Ventaja:** Si falla la escritura, el archivo original permanece intacto.

#### 8.4.2 Validación de Encabezados

**En carga:**
```python
lector_csv = csv.DictReader(archivo)
# DictReader automáticamente lee la primera línea como headers
```

**Validación adicional posible:**
```python
expected_headers = {'nombre', 'poblacion', 'superficie', 'continente'}
if set(lector_csv.fieldnames) != expected_headers:
    raise ValueError(f"Headers incorrectos: {lector_csv.fieldnames}")
```

Esto garantizaría que el CSV tiene exactamente las columnas esperadas.

### 8.5 Sincronización Memoria-Disco

**Flujo de datos:**
```
CSV (disco) → cargar_datos_desde_csv() → lista_paises (memoria) → operaciones → guardar_datos() → CSV (disco)
```

**Puntos de sincronización:**
1. **Carga inicial:** Una vez al inicio del programa
2. **Guardado tras agregar:** Inmediato después de `agregar_pais()`
3. **Guardado tras editar:** Inmediato después de `editar_pais()`

**No sincronizado:**
- Búsquedas, filtros, ordenamientos, estadísticas (read-only)

Esta estrategia es apropiada porque:
- Las escrituras son infrecuentes
- No hay múltiples usuarios concurrentes
- El dataset completo cabe en memoria

### 8.6 Alternativas Consideradas

**SQLite:**
```python
import sqlite3
conn = sqlite3.connect('paises.db')
cursor.execute("SELECT * FROM paises WHERE poblacion > ?", (1000000,))
```

**Ventajas sobre CSV:**
- Índices (búsquedas más rápidas)
- Tipos de datos nativos
- Consultas SQL (más expresivas)
- Transacciones ACID

**Desventajas:**
- Más complejo (requiere crear schema)
- Menos portable (archivo binario)
- Overhead para dataset pequeño

**Conclusión:** Para 195 países, CSV es más simple y suficiente. SQLite sería apropiado para 10,000+ países.

---

## 9. CONCLUSIONES <a name="conclusiones"></a>
**Hernán González:**
Mi contribución se centró en la interfaz y el frontend de la lógica de consulta, lo cual implicó asegurar una experiencia de usuario (UX) óptima para la aplicación de consola.
El principal logro fue la implementación de un diseño de interfaz responsivo (mis_funciones.ancho_total()), la compleja lógica de paginación en consola (paginar_resultados),
 y la validación en la capa de entrada del usuario (numero_opcion, numero_entero).
Esto abordó el desafío de crear un entorno amigable dentro de las limitaciones de la terminal, superando el estándar de UX en aplicaciones de consola.
 A nivel de lógica de negocio, el desarrollo de los módulos de búsqueda y filtros reforzó mi comprensión sobre la normalización de texto para búsquedas
insensibles a acentos y la aplicación de estructuras condicionales anidadas para filtros multi-criterio.
Este rol fue crucial para demostrar la funcionalidad total y el valor agregado del sistema al usuario final.

**Elías Tello:** Desarrollo de módulos de ordenamiento, estadísticas, manejo de CSV, y documentación técnica.
  Mi enfoque estuvo en la estabilidad del backend y el procesamiento algorítmico de los datos.
  El desarrollo del módulo de manejo de CSV y persistencia consolidó mi entendimiento de la sincronización entre la memoria y el disco,
  garantizando la integridad de los datos mediante csv.DictWriter y la detección de duplicados.
  A nivel algorítmico, la implementación del ordenamiento demostró la elección eficiente de Timsort (sorted() con una función key segura) para manejar diferentes tipos de datos numéricos y de texto.
   El módulo de estadísticas representó un logro técnico al aplicar procesamiento de datos y manejo de excepciones para calcular promedios y, en particular, el uso de collections.
  Counter para el análisis de distribución por continente, demostrando la capacidad de usar librerías avanzadas de Python para el análisis.

### 9. Reflexión Final

El desarrollo de este sistema representó un puente entre los conceptos teóricos de programación y la práctica de ingeniería de software. Más allá de escribir código que funciona, aprendimos a:

- **Pensar en términos de arquitectura**, no solo de funciones aisladas
- **Diseñar para el usuario**, incluso en interfaces de consola
- **Validar exhaustivamente**, anticipando todo lo que puede salir mal
- **Documentar claramente**, pensando en futuros mantenedores del código
- **Trabajar colaborativamente**, aprovechando las fortalezas de cada integrante

Este proyecto no es solo un trabajo práctico, sino una demostración de que los fundamentos sólidos de programación, combinados con buenas prácticas de ingeniería, resultan en software robusto, mantenible y profesional.

---

## 10. REFERENCIAS BIBLIOGRÁFICAS <a name="referencias"></a>

### 10.1 Documentación Oficial

1. **Python Software Foundation.** (2024). *Python 3.10 Documentation*. Recuperado de https://docs.python.org/3.10/

2. **Python Software Foundation.** (2024). *csv — CSV File Reading and Writing*. Python Standard Library. Recuperado de https://docs.python.org/3/library/csv.html

3. **Python Software Foundation.** (2024). *collections — Container datatypes*. Python Standard Library. Recuperado de https://docs.python.org/3/library/collections.html

4. **Python Software Foundation.** (2024). *shutil — High-level file operations*. Python Standard Library. Recuperado de https://docs.python.org/3/library/shutil.html

### 10.2 Algoritmos y Estructuras de Datos

5. **Peters, Tim.** (2002). *Timsort*. Python Enhancement Proposals (PEP). Recuperado de https://github.com/python/cpython/blob/main/Objects/listsort.txt

6. **Cormen, T. H., Leiserson, C. E., Rivest, R. L., & Stein, C.** (2022). *Introduction to Algorithms* (4th ed.). MIT Press.

7. **Goodrich, M. T., Tamassia, R., & Goldwasser, M. H.** (2013). *Data Structures and Algorithms in Python*. Wiley.

### 10.3 Ingeniería de Software

8. **Martin, R. C.** (2008). *Clean Code: A Handbook of Agile Software Craftsmanship*. Prentice Hall.

9. **Martin, R. C.** (2017). *Clean Architecture: A Craftsman's Guide to Software Structure and Design*. Prentice Hall.

10. **Hunt, A., & Thomas, D.** (2019). *The Pragmatic Programmer: Your Journey to Mastery* (20th Anniversary Edition). Addison-Wesley Professional.

### 10.4 Python Best Practices

11. **Van Rossum, G., Warsaw, B., & Coghlan, N.** (2001). *PEP 8 – Style Guide for Python Code*. Python Enhancement Proposals. Recuperado de https://peps.python.org/pep-0008/

12. **Ramalho, L.** (2022). *Fluent Python: Clear, Concise, and Effective Programming* (2nd ed.). O'Reilly Media.

13. **Beazley, D., & Jones, B. K.** (2013). *Python Cookbook* (3rd ed.). O'Reilly Media.

### 10.5 Validación y Manejo de Errores

14. **Python Software Foundation.** (2024). *Errors and Exceptions*. Python Tutorial. Recuperado de https://docs.python.org/3/tutorial/errors.html

15. **Hettinger, R.** (2013). *Transforming Code into Beautiful, Idiomatic Python*. PyCon 2013. Recuperado de https://www.youtube.com/watch?v=OSGv2VnC0go

### 10.6 CSV y Persistencia de Datos

16. **RFC 4180.** (2005). *Common Format and MIME Type for Comma-Separated Values (CSV) Files*. Internet Engineering Task Force (IETF). Recuperado de https://datatracker.ietf.org/doc/html/rfc4180

17. **McKinney, W.** (2022). *Python for Data Analysis* (3rd ed.). O'Reilly Media.

### 10.7 User Experience

18. **Norman, D. A.** (2013). *The Design of Everyday Things: Revised and Expanded Edition*. Basic Books.

19. **Krug, S.** (2014). *Don't Make Me Think, Revisited: A Common Sense Approach to Web Usability* (3rd ed.). New Riders.

### 10.8 Control de Versiones

20. **Chacon, S., & Straub, B.** (2014). *Pro Git* (2nd ed.). Apress. Recuperado de https://git-scm.com/book/en/v2

21. **GitHub.** (2024). *GitHub Docs*. Recuperado de https://docs.github.com/

### 10.9 Datasets y Fuentes de Datos

22. **Worldometer.** (2024). *Countries in the world by population (2024)*. Recuperado de https://www.worldometers.info/world-population/population-by-country/

23. **The World Bank.** (2024). *World Development Indicators*. Recuperado de https://databank.worldbank.org/

### 10.10 Material Académico

24. **Universidad Tecnológica Nacional.** (2024). *Programación 1 - Material de Cátedra*. Tecnicatura Universitaria en Programación.

25. **Zelle, J.** (2016). *Python Programming: An Introduction to Computer Science* (3rd ed.). Franklin, Beedle & Associates.

---

## ANEXOS

### ANEXO A: Diagrama de Flujo del Sistema

```
                           ┌─────────────────┐
                           │   INICIO        │
                           └────────┬────────┘
                                    │
                           ┌────────▼────────┐
                           │ Cargar CSV      │
                           │ paises_mundo.csv│
                           └────────┬────────┘
                                    │
                    ┌───────────────▼───────────────┐
                    │   MENÚ PRINCIPAL (loop)       │
                    │                               │
                    │  1. Buscar por nombre         │
                    │  2. Filtros                   │
                    │  3. Ordenar                   │
                    │  4. Estadísticas              │
                    │  5. Agregar país              │
                    │  6. Editar país               │
                    │  7. Salir                     │
                    └───┬───┬───┬───┬───┬───┬───┬───┘
                        │   │   │   │   │   │   │
        ┌───────────────┘   │   │   │   │   │   └──────────┐
        │                   │   │   │   │   │              │
    ┌───▼────┐    ┌────────▼───▼───▼───▼───▼──────┐   ┌───▼────┐
    │Búsqueda│    │   Módulos Funcionales          │   │ Salir  │
    │        │    │   - filtro_de_busqueda.py      │   │        │
    │        │    │   - ordenar_países.py          │   └───▲────┘
    │        │    │   - mostrar_estadísticas.py    │       │
    └───┬────┘    │   - manejo_csv.py              │       │
        │         └────────────┬───────────────────┘       │
        │                      │                           │
        │         ┌────────────▼────────────┐              │
        │         │  mis_funciones.py       │              │
        │         │  (Utilidades)           │              │
        │         │  - Validaciones         │              │
        └────────►│  - Formateo             │              │
                  │  - Paginación           │              │
                  │  - Normalización        │              │
                  └─────────────────────────┘              │
                                │                          │
                                │                          │
                    ┌───────────▼───────────┐              │
                    │  Mostrar Resultados   │              │
                    │  (paginados)          │              │
                    └───────────┬───────────┘              │
                                │                          │
                                └──────────────────────────┘
                                           
                           Loop continúa hasta opción 7
```

### ANEXO B: Estructura Detallada del CSV

**Formato del archivo paises_mundo.csv:**

```csv
nombre,poblacion,superficie,continente
China,1425671352,9596961,Asia
India,1428627663,3287263,Asia
Estados Unidos,339996563,9833517,América del Norte
...
```

**Especificaciones:**
- **Delimitador:** Coma (`,`)
- **Encoding:** UTF-8
- **Header:** Primera línea contiene nombres de columnas
- **Tipos de datos:**
  - `nombre`: string (sin restricción de longitud)
  - `poblacion`: integer positivo
  - `superficie`: integer positivo (km²)
  - `continente`: string (valores posibles: "América del Sur", "América del Norte", "Europa", "África", "Asia", "Oceanía")

### ANEXO C: Tabla de Complejidades

| Operación | Complejidad Temporal | Complejidad Espacial | Justificación |
|-----------|---------------------|---------------------|---------------|
| Cargar CSV | O(n) | O(n) | Lectura lineal, almacenamiento completo |
| Búsqueda por nombre | O(n·m) | O(k) | n países, m longitud nombre, k resultados |
| Filtro por continente | O(n) | O(k) | Recorrido lineal, k resultados |
| Filtro por población | O(n) | O(k) | Recorrido lineal con comparaciones |
| Ordenar | O(n log n) | O(n) | Timsort, crea nueva lista |
| Estadísticas | O(n) | O(c) | Un recorrido, c continentes únicos |
| Agregar país | O(n) | O(1) | Verifica duplicados O(n), append O(1) |
| Editar país | O(n) | O(1) | Búsqueda lineal, edición in-place |
| Guardar CSV | O(n) | O(1) | Escritura lineal, no crea estructuras |
| Paginación | O(1) | O(k) | Slice constante, k elementos por página |

**Notas:**
- n = número de países (~195)
- m = longitud promedio de nombres (~15)
- k = número de resultados (variable)
- c = número de continentes (~6)

### ANEXO D: Casos de Prueba Ejecutados

**1. Búsqueda por Nombre**

| Test Case | Input | Resultado Esperado | Resultado Obtenido | Estado |
|-----------|-------|-------------------|-------------------|---------|
| Búsqueda exacta | "Argentina" | 1 país encontrado | 1 país (Argentina) | ✅ PASS |
| Búsqueda parcial | "guinea" | 3 países | Guinea, Guinea-Bisáu, Guinea Ecuatorial | ✅ PASS |
| Sin acentos | "japon" | 1 país | Japón | ✅ PASS |
| Case insensitive | "BRASIL" | 1 país | Brasil | ✅ PASS |
| No encontrado | "xyz123" | 0 países | Mensaje: "No se encontraron resultados" | ✅ PASS |
| Input vacío | "" | Error | Mensaje: "No ingresó término" | ✅ PASS |

**2. Filtros**

| Test Case | Input | Resultado Esperado | Resultado Obtenido | Estado |
|-----------|-------|-------------------|-------------------|---------|
| Filtro continente válido | Asia | 48 países | 48 países de Asia | ✅ PASS |
| Población rango válido | 10M - 50M | Múltiples países | Países en rango correcto | ✅ PASS |
| Población min > max | min:100M, max:10M | Error de validación | Mensaje: "Mínimo no puede ser mayor" | ✅ PASS |
| Superficie rango válido | 100k - 1M | Múltiples países | Países en rango correcto | ✅ PASS |
| Filtros acumulativos | América del Sur + población > 30M | 3 países | Brasil, Argentina, Colombia | ✅ PASS |

**3. Ordenamiento**

| Test Case | Input | Resultado Esperado | Resultado Obtenido | Estado |
|-----------|-------|-------------------|-------------------|---------|
| Por población DESC | Opción 2, DESC | India primero | India (1,428M) primero | ✅ PASS |
| Por población ASC | Opción 2, ASC | Vaticano primero | Vaticano (825) primero | ✅ PASS |
| Por nombre ASC | Opción 1, ASC | Orden alfabético | Afganistán, Albania, ... | ✅ PASS |
| Por superficie DESC | Opción 3, DESC | Rusia primero | Rusia (17M km²) primero | ✅ PASS |

**4. Estadísticas**

| Test Case | Métrica | Resultado Esperado | Resultado Obtenido | Estado |
|-----------|---------|-------------------|-------------------|---------|
| Mayor población | - | India | India (1,428,627,663) | ✅ PASS |
| Menor población | - | Vaticano | Vaticano (825) | ✅ PASS |
| Promedio población | - | ~40M | 40,735,756.67 | ✅ PASS |
| Conteo por continente | África | 54 países | 54 países | ✅ PASS |

**5. Agregar País**

| Test Case | Input | Resultado Esperado | Resultado Obtenido | Estado |
|-----------|-------|-------------------|-------------------|---------|
| País nuevo válido | "TestLand", 1M, 10k, Europa | Agregado con éxito | País agregado y guardado | ✅ PASS |
| País duplicado | "Argentina" | Error de duplicado | Mensaje: "Ya existe" | ✅ PASS |
| Población inválida | "abc" | Re-solicitud | Bucle hasta input válido | ✅ PASS |

**6. Editar País**

| Test Case | Input | Resultado Esperado | Resultado Obtenido | Estado |
|-----------|-------|-------------------|-------------------|---------|
| Editar población | Argentina, nueva: 50M | Población actualizada | Cambio guardado correctamente | ✅ PASS |
| País no existe | "PaisInexistente" | Error | Mensaje: "No se encontró" | ✅ PASS |
| Cancelar edición | Opción 4 | Sin cambios | Mensaje: "Edición cancelada" | ✅ PASS |

**7. Validaciones**

| Test Case | Input | Comportamiento Esperado | Resultado Obtenido | Estado |
|-----------|-------|------------------------|-------------------|---------|
| Opción de menú inválida | "abc" | Mensaje de error y re-solicitud | Error + reintentar | ✅ PASS |
| Número fuera de rango | 99 | Mensaje de error y re-solicitud | Error + reintentar | ✅ PASS |
| Ctrl+C durante input | Ctrl+C | Captura y mensaje | "Operación cancelada" | ✅ PASS |
| CSV con fila corrupta | Población = "N/A" | Omitir fila con advertencia | Advertencia mostrada, programa continúa | ✅ PASS |

### ANEXO E: Métricas del Código

**Estadísticas del Proyecto:**

```
Archivo                      Líneas   Funciones   Complejidad   Comentarios
─────────────────────────────────────────────────────────────────────────────
main.py                      30       0           2 (simple)    5
mis_funciones.py             180      13          15 (moderada) 25
busqueda_por_nombre.py       45       1           3 (simple)    8
filtro_de_busqueda.py        145      4           12 (moderada) 18
ordenar_países.py            85       2           8 (simple)    12
mostrar_estadísticas.py      95       1           10 (moderada) 15
manejo_csv.py                140      4           11 (moderada) 20
─────────────────────────────────────────────────────────────────────────────
TOTAL                        720      25          61            103
```

**Cobertura de Validaciones:**
- Validación de entrada de usuario: 100%
- Validación de datos CSV: 100%
- Manejo de excepciones: 95%
- Mensajes de error claros: 100%

**Métricas de Calidad:**
- Ratio Comentarios/Código: 14.3%
- Funciones por módulo: 3.6 (promedio)
- Líneas por función: 28.8 (promedio)
- Complejidad ciclomática promedio: 2.44 (baja complejidad)

### ANEXO F: Glosario de Términos

**Términos Técnicos Utilizados:**

- **Artifact:** Componente de software generado durante el desarrollo
- **Big O:** Notación para expresar complejidad algorítmica
- **CSV (Comma-Separated Values):** Formato de archivo de texto para datos tabulares
- **Context Manager:** Objeto Python que gestiona recursos (ej: archivos) con `with`
- **Dictionary (Dict):** Estructura de datos hash con pares clave-valor
- **DictReader/DictWriter:** Clases de csv para leer/escribir diccionarios
- **Encoding:** Sistema de representación de caracteres (ej: UTF-8)
- **Exception:** Evento que interrumpe el flujo normal del programa
- **Generator Expression:** Expresión que genera valores bajo demanda
- **Hash Table:** Estructura de datos para búsqueda en tiempo constante
- **Immutable:** Objeto que no puede ser modificado después de creación
- **I/O (Input/Output):** Operaciones de entrada y salida de datos
- **Lambda:** Función anónima de una línea en Python
- **List Comprehension:** Sintaxis concisa para crear listas
- **Modularización:** División de código en módulos independientes
- **Normalización:** Proceso de estandarizar datos para comparación
- **PEP (Python Enhancement Proposal):** Documento de diseño de Python
- **Refactoring:** Mejorar estructura del código sin cambiar funcionalidad
- **SRP (Single Responsibility Principle):** Principio de responsabilidad única
- **Slicing:** Técnica para extraer subsecuencias de listas
- **Timsort:** Algoritmo de ordenamiento híbrido usado en Python
- **Try-Except:** Estructura para manejo de excepciones
- **Tuple:** Secuencia inmutable de elementos
- **UX (User Experience):** Experiencia de usuario
- **Validación:** Verificación de corrección de datos

---

## DECLARACIÓN DE AUTORÍA

Declaramos que este trabajo es original y ha sido realizado íntegramente por los integrantes del equipo. Todo código, documentación y contenido ha sido desarrollado específicamente para este Trabajo Práctico Integrador de Programación 1.

Las fuentes consultadas para conceptos teóricos y mejores prácticas están debidamente citadas en la sección de Referencias Bibliográficas.

**Integrantes:**
- **Hernán González:** Desarrollo de módulos de búsqueda, filtros, interfaz de usuario, y demostración del sistema.
- **Elías Tello:** Desarrollo de módulos de ordenamiento, estadísticas, manejo de CSV, y documentación técnica.
  Mi enfoque estuvo en la estabilidad del backend y el procesamiento algorítmico de los datos.
  El desarrollo del módulo de manejo de CSV y persistencia consolidó mi entendimiento de la sincronización entre la memoria y el disco,
  garantizando la integridad de los datos mediante csv.DictWriter y la detección de duplicados.
  A nivel algorítmico, la implementación del ordenamiento demostró la elección eficiente de Timsort (sorted() con una función key segura) para manejar diferentes tipos de datos numéricos y de texto.
   El módulo de estadísticas representó un logro técnico al aplicar procesamiento de datos y manejo de excepciones para calcular promedios y, en particular, el uso de collections.
  Counter para el análisis de distribución por continente, demostrando la capacidad de usar librerías avanzadas de Python para el análisis.
  Mi trabajo en la documentación técnica fue clave para formalizar la arquitectura modular del proyecto.
**Fecha de entrega:** [Completar]

**Firma (simbólica):**

_________________________          _________________________
Hernán González                     Elías [Apellido]

---

**FIN DEL INFORME TÉCNICO**

*Tecnicatura Universitaria en Programación*  
*Programación 1 - Comisión 3*  
*Trabajo Práctico Integrador*  
*Año 2024-2025*
