import csv
<<<<<<< HEAD
import os
ANCHO_TOTAL = 102

def inicializar_archivo():
    if not os.path.exists('csv\\paises_mundo.csv'):
        with open('csv\\paises_mundo.csv', 'w', newline='', encoding='utf-8') as archivo:
            escritor = csv.DictWriter(archivo, fieldnames=["nombre","poblacion","superficie","continente"])
            escritor.writeheader()

def menu_centro(texto, ancho=ANCHO_TOTAL):
=======
import shutil
import time
import os

def limpiar_pantalla():
    if os.name == 'nt':
        _ = os.system('cls')

def ancho_total():
    ancho = shutil.get_terminal_size().columns
    return ancho

def menu_centro(texto, ancho=ancho_total()):
>>>>>>> b7d4a458f98df2513eb614722256533bb3f5955d
    return f"{texto:^{ancho}}"

def menu_principal():
    opciones = [
        "Buscar país por nombre",
        "Filtro de países",
        "Ordenar lista de países",
        "Mostrar estadísticas",
        "Agregar un nuevo pais",
        "Editar un pais de la lista",
        "Salir"
    ]
    # Imprime el menú línea por línea con formato
    print("=" * ancho_total())
    print(menu_centro("MENÚ PRINCIPAL"))
    print("-" * ancho_total())
    
    # Itera sobre la lista e imprime cada opción con formato
    for i, opcion_texto in enumerate(opciones, start=1):
        linea = f"  {i}. {opcion_texto}"
        print(f"{linea:<{ancho_total() - 2}}")
    print("=" * ancho_total())

def menu_filtros():
    
    limpiar_pantalla()
    
    
    opciones = [
        "Buscar por continente",
        "Buscar por rango de población",
        "Buscar por rango de superficie",
        "Volver atrás"
    ]
    
    # Imprime el menú línea por línea con formato
    print("=" * ancho_total())
    print(menu_centro("¿Qué tipo de filtros deseas usar?"))
    print("-" * ancho_total())
    
    # Itera sobre la lista e imprime cada opción con formato
    for i, opcion_texto in enumerate(opciones, start=1):
        linea = f"  {i}. {opcion_texto}"
        print(f"{linea:<{ancho_total() - 6}}  ") 
    print("=" * ancho_total())

def menu_continentes():
    
    limpiar_pantalla()
    
    
    opciones = [
        "América del Sur",
        "América del Norte",
        "Europa",
        "África",
        "Asia",
        "Oceanía",
    ]
    
    # Imprime el menú línea por línea con formato
    print("=" * ancho_total())
    print(menu_centro("Elige algún continente:"))
    print("-" * ancho_total())
    
    # Itera sobre la lista e imprime cada opción con formato
    for i, opcion_texto in enumerate(opciones, start=1):
        linea = f"  {i}. {opcion_texto}"
        print(f"{linea:<{ancho_total() - 6}}  ") 
    print("=" * ancho_total())

def numero_opcion(rango):
    while True:
        try:
            entrada_usuario = int(input("Elija una opción: "))
            if entrada_usuario in range(1, rango +1):
                numero = int(entrada_usuario)
                return numero
        except ValueError:
                print("-" * ancho_total())
                print(menu_centro("Error: El dato ingresado no pertenece a ninguna opción. Inténtalo de nuevo."))
                print("-" * ancho_total())

def numero_entero(texto):
    while True:     
        num = input(texto)
        try:
            num = num.replace('.', '')
            numero = int(num)
            return numero
        except ValueError:
            print("Error: El dato ingresado no es un número. Inténtalo de nuevo.")

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
                    print(f"Advertencia: Se omitió una fila por datos inválidos o faltantes: {fila}")
    except FileNotFoundError:
        print(f"Error: El archivo no se encontró en la ruta '{ruta_archivo}'")
    except Exception as e:
        print(f"Error inesperado al leer el archivo: {e}")
    return lista_paises

def verificar_num(num):
    if num.isdigit():
        numero = int(num)
        return numero

def si_o_no(validacion, texto):
    while True:
        try:
            respuesta = input(texto).strip().lower()
            
            # Respuestas afirmativas comunes
            if respuesta in ("s", "si", "sí", "y", "yes"):
                return validacion == True
            # Respuestas negativas comunes
            elif respuesta in ("n", "no"):
                return validacion == False
            else:
                print("❌ Entrada no válida. Por favor responda con 'sí' o 'no' (o 's'/'n').")
                print("-" * ancho_total())
        except KeyboardInterrupt:
            print("\n\nOperación cancelada por el usuario.")
            return validacion == False  
            # o podrías lanzar una excepción si lo prefieres
        except Exception as e:
            print(f"Error inesperado al leer la respuesta: {e}")
            print("Por favor, inténtelo de nuevo.")

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

def imprimir_resultados(paises_ordenados):
    
    # 1. Definición de constantes (fuera del while)
    ANCHO_NUM = 7
    ANCHO_NOMBRE = 35
    ANCHO_POB = 15
    ANCHO_SUP = 18
    ANCHO_CONT = 25
    #ANCHO_TOTAL = ANCHO_NUM + ANCHO_NOMBRE + ANCHO_POB + ANCHO_SUP + ANCHO_CONT + (4 * 3)

    # 2. Inicialización de variables de paginación (fuera del while)
    pagina = 0
    por_pagina = 10
    total = len(paises_ordenados)
    total_paginas = (total + por_pagina - 1) // por_pagina

    # 3. Bucle de navegación (dentro del while)
    while True:
        # Cálculo de índices de página actual
        inicio = pagina * por_pagina
        fin = inicio + por_pagina

        # Encabezado
        limpiar_pantalla()
        
        print(f"\nPágina {pagina+1} de {total_paginas}")
        print(f"\n{'#':>{ANCHO_NUM}} | {'Nombre':<{ANCHO_NOMBRE}} | 🚻 {'Población':>{ANCHO_POB}} | 🗺️ {'Superficie (km²)':>{ANCHO_SUP}} | 🌎 {'Continente':<{ANCHO_CONT}}")
        print("-" * ancho_total())

        # Filas de países
        for con, pais in enumerate(paises_ordenados[inicio:fin], start=inicio+1):
            nombre = pais.get('nombre', 'Desconocido')
            poblacion = f"{pais.get('poblacion', 'N/A'):,}"
            superficie = f"{pais.get('superficie', 'N/A'):,}"
            continente = pais.get('continente', 'N/A')
            print(f"{con:>{ANCHO_NUM}} | {nombre:<{ANCHO_NOMBRE}} |    {poblacion:>{ANCHO_POB}} |   {superficie:>{ANCHO_SUP}} |    {continente:<{ANCHO_CONT}}")

        print("-" * ancho_total())

        # Opciones de navegación
        print("Opciones: [A]vanzar | [R]etroceder | [S]alir")
        accion = input("Seleccione una opción: ").strip().lower()

        # Lógica de navegación
        if accion == 's':
            print("👋 Saliendo de la paginación...")
            time.sleep(1)
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
        else:
            print("❌ Opción inválida. Intente nuevamente.")