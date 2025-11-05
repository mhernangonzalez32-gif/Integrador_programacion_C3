# 🌍 Gestión de Datos de Países en Python

Sistema de gestión y análisis de información sobre países del mundo, desarrollado en Python. Permite realizar búsquedas, filtrados, ordenamientos y estadísticas sobre un dataset de países con información demográfica y geográfica.

## 📋 Descripción del Proyecto

Este proyecto es un Trabajo Práctico Integrador de Programación 1 que implementa una aplicación de consola para gestionar información de países. El sistema permite cargar datos desde un archivo CSV y realizar diversas operaciones como búsquedas, filtros personalizados, ordenamientos y cálculos estadísticos.

### Características principales:
- ✅ Búsqueda de países por nombre (coincidencia parcial)
- ✅ Filtros por continente, población y superficie
- ✅ Ordenamiento ascendente/descendente por múltiples criterios
- ✅ Estadísticas: promedios, máximos, mínimos y distribución por continente
- ✅ Agregar y editar países en el dataset
- ✅ Paginación de resultados
- ✅ Interfaz de consola intuitiva y responsiva

## 🛠️ Tecnologías Utilizadas

- **Lenguaje:** Python 3.x
- **Librerías estándar:**
  - `csv` - Lectura y escritura de archivos CSV
  - `shutil` - Gestión del tamaño de terminal
  - `os` - Operaciones del sistema operativo
  - `time` - Pausas y temporizadores
  - `difflib` - Comparación de cadenas (búsqueda)
  - `collections.Counter` - Conteo de elementos

## 📁 Estructura del Proyecto

```
proyecto-paises/
│
├── main.py                          # Archivo principal con menú
├── csv/
│   └── paises_mundo.csv            # Dataset con 195 países
│
├── funciones/
│   ├── mis_funciones.py            # Funciones auxiliares y utilidades
│   ├── busqueda_por_nombre.py      # Búsqueda de países
│   ├── filtro_de_busqueda.py       # Filtros por continente, población, superficie
│   ├── ordenar_países.py           # Ordenamiento de países
│   ├── mostrar_estadísticas.py     # Cálculos estadísticos
│   └── manejo_csv.py               # Agregar y editar países
│
└── README.md                        # Este archivo
```

## 🚀 Instalación y Uso

### Requisitos previos
- Python 3.x instalado en el sistema
- Terminal o consola de comandos

### Instrucciones de instalación

1. **Clonar el repositorio:**
```bash
git clone https://github.com/tu-usuario/gestion-paises-python.git
cd gestion-paises-python
```

2. **Verificar que existe el archivo CSV:**
Asegúrate de que el archivo `csv/paises_mundo.csv` esté en la carpeta correcta.

3. **Ejecutar el programa:**
```bash
python main.py
```

## 📖 Guía de Uso

### Menú Principal
Al ejecutar el programa, verás 7 opciones:

```
═══════════════════════════════════════════
              MENÚ PRINCIPAL
───────────────────────────────────────────
  1. Buscar país por nombre
  2. Filtro de países
  3. Ordenar lista de países
  4. Mostrar estadísticas
  5. Agregar un nuevo pais
  6. Editar un pais de la lista
  7. Salir
═══════════════════════════════════════════
```

### Ejemplos de Uso

#### 1️⃣ Buscar País por Nombre
**Entrada:**
```
Que pais esta buscando?
argentina
```

**Salida:**
```
--- Resultados para 'argentina' (1 encontrados) ---

#    | Nombre          | 🚻 Población    | 🗺️ Superficie (km²) | 🌎 Continente
──────────────────────────────────────────────────────────────────────
1    | Argentina       |   45,773,884    |      2,780,400       | América del Sur
```

#### 2️⃣ Filtrar por Continente
**Entrada:**
```
Elige algún continente:
1. América del Sur
```

**Salida:**
Muestra todos los países de América del Sur con paginación (10 países por página).

#### 3️⃣ Ordenar Países
**Entrada:**
```
Ordenar países por:
2. Población

¿Querés mostrarlo en orden descendente? (s/n): s
```

**Salida:**
Lista de países ordenados de mayor a menor población.

#### 4️⃣ Estadísticas
**Salida automática:**
```
═════════════════ ESTADÍSTICAS GENERALES ═════════════════

🌐 País con mayor población: India (1,428,627,663 habitantes)
🌐 País con menor población: Ciudad del Vaticano (825 habitantes)

📈 Población promedio: 40,735,756.67 habitantes
📏 Superficie promedio: 695,959.82 km²

🗺️ Países por continente:
   • África: 54 país(es)
   • América del Norte: 23 país(es)
   • América del Sur: 12 país(es)
   • Asia: 48 país(es)
   • Europa: 44 país(es)
   • Oceanía: 14 país(es)
```

#### 5️⃣ Agregar Nuevo País
**Entrada:**
```
¿Cómo se llama el nuevo país?
ejemplo país

Población de ejemplo país?
1000000

Superficie de ejemplo país?
50000

Elige algún continente:
1. América del Sur
```

**Salida:**
```
¡País 'ejemplo país' agregado con éxito!
Archivo actualizado con éxito!
```

## 🔍 Estructura de Datos

### Dataset CSV
Cada país contiene la siguiente información:

| Campo        | Tipo    | Descripción                    |
|--------------|---------|--------------------------------|
| `nombre`     | string  | Nombre del país                |
| `poblacion`  | int     | Población total                |
| `superficie` | int     | Superficie en km²              |
| `continente` | string  | Continente al que pertenece    |

**Ejemplo de registro:**
```csv
nombre,poblacion,superficie,continente
Argentina,45773884,2780400,América del Sur
```

## 🧩 Funcionalidades Técnicas

### Conceptos de Programación Aplicados

#### 📝 Listas
Almacenamiento dinámico de países como lista de diccionarios:
```python
paises = [
    {'nombre': 'Argentina', 'poblacion': 45773884, ...},
    {'nombre': 'Brasil', 'poblacion': 216422446, ...}
]
```

#### 📚 Diccionarios
Cada país es representado como un diccionario con claves estandarizadas.

#### ⚙️ Funciones
Modularización total del código con funciones específicas:
- `cargar_datos_desde_csv()` - Carga de datos
- `buscar_pais_nombre()` - Búsqueda
- `imprimir_resultados()` - Visualización con paginación

#### 🔀 Condicionales
Control de flujo con `if/elif/else` y `match/case` (Python 3.10+).

#### 🔄 Estructuras Repetitivas
- `while` para menús y validaciones
- `for` para iteración sobre países

#### 📊 Ordenamientos
Uso de `sorted()` con funciones `lambda` y parámetro `reverse`:
```python
sorted(lista_paises, key=lambda x: x['poblacion'], reverse=True)
```

#### 📈 Estadísticas
Funciones `max()`, `min()`, `sum()` y `Counter()` para análisis de datos.

#### 📁 Manejo de Archivos CSV
Lectura con `csv.DictReader()` y escritura con `csv.DictWriter()`.

### Validaciones Implementadas

✅ Control de errores en formato CSV  
✅ Validación de entradas numéricas  
✅ Mensajes claros de éxito/error  
✅ Manejo de búsquedas sin resultados  
✅ Prevención de duplicados al agregar países  
✅ Normalización de texto para búsquedas (eliminación de tildes)

## 👥 Participación de Integrantes

### [Integrante 1 - Elias Tello]
- Desarrollo del módulo de búsqueda y filtros
- Implementación de funciones auxiliares
- Diseño de la interfaz de consola

### [Integrante 2 - Hernan Gonzalez]
- Desarrollo del módulo de ordenamiento y estadísticas
- Manejo de archivos CSV (agregar/editar)
- Documentación y testing

## 📚 Conceptos Teóricos Aplicados

### Listas en Python
Estructura de datos secuencial y mutable que permite almacenar colecciones ordenadas. En este proyecto, se utiliza para mantener el conjunto completo de países.

### Diccionarios
Estructura de datos tipo hash que almacena pares clave-valor. Cada país es un diccionario con claves `nombre`, `poblacion`, `superficie` y `continente`.

### Funciones
Bloques de código reutilizable que realizan tareas específicas. El proyecto está completamente modularizado siguiendo el principio de "una función = una responsabilidad".

### Ordenamiento
Algoritmo de ordenación de Python (`Timsort`) implementado en la función `sorted()`. Permite ordenar por cualquier criterio usando funciones `key`.

### Archivos CSV
Formato de archivo de texto plano para datos tabulares. Se utiliza `csv.DictReader` para lectura y `csv.DictWriter` para escritura, facilitando el manejo de datos estructurados.

## 🎯 Criterios de Evaluación Cumplidos

- ✅ **Funcionalidad correcta:** Todas las búsquedas, filtros, ordenamientos y estadísticas funcionan correctamente
- ✅ **Estructuras de datos:** Uso apropiado de listas y diccionarios
- ✅ **Calidad de código:** Modularización, legibilidad y comentarios
- ✅ **Documentación:** README completo con ejemplos e instrucciones
- ✅ **Validaciones:** Manejo robusto de errores y entradas inválidas

## 🔮 Posibles Mejoras Futuras

- [ ] Interfaz gráfica con Tkinter o PyQt
- [ ] Exportar resultados a Excel o PDF
- [ ] Gráficos estadísticos con matplotlib
- [ ] Base de datos SQL en lugar de CSV
- [ ] API REST para consultas remotas
- [ ] Tests unitarios automatizados

## 📞 Contacto

**Desarrolladores:** [Hernan https://github.com/mhernangonzalez32-gif]  
                     [Elias https://github.com/eEmanuel07] 
**Materia:** Programación 1  
**Institución:** Tecnicatura Universitaria en Programación

---

⭐ Si este proyecto te resultó útil, no olvides darle una estrella en GitHub!

## 📄 Licencia

Este proyecto es de uso académico para la Tecnicatura Universitaria en Programación.
