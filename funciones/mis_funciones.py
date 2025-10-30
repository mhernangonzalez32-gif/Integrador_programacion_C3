import csv

ANCHO_TOTAL = 102

def menu_centro(texto, ancho=ANCHO_TOTAL):
    return f"{texto:^{ancho}}"

def menu_principal():
    opciones = [
        "Buscar país por nombre",
        "Filtro de países",
        "Ordenar lista de países",
        "Mostrar estadísticas",
        "Salir"
    ]
    # Imprime el menú línea por línea con formato
    print("=" * ANCHO_TOTAL)
    print(menu_centro("MENÚ PRINCIPAL"))
    print("-" * ANCHO_TOTAL)
    
    # Itera sobre la lista e imprime cada opción con formato
    for i, opcion_texto in enumerate(opciones, start=1):
        linea = f"  {i}. {opcion_texto}"
        print(f"{linea:<{ANCHO_TOTAL - 2}}")
    print("=" * ANCHO_TOTAL)

def menu_filtros():
    opciones = [
        "Buscar por continente",
        "Buscar por rango de población",
        "Buscar por rango de superficie",
        "Volver atras"
    ]
    
    # Imprime el menú línea por línea con formato
    print("=" * ANCHO_TOTAL)
    print(menu_centro("¿Qué tipo de filtros deseas usar?"))
    print("-" * ANCHO_TOTAL)
    
    # Itera sobre la lista e imprime cada opción con formato
    for i, opcion_texto in enumerate(opciones, start=1):
        linea = f"  {i}. {opcion_texto}"
        print(f"{linea:<{ANCHO_TOTAL - 6}}  ") 
    print("=" * ANCHO_TOTAL)

def menu_con():
    opciones = [
        "América del Sur",
        "América del Norte",
        "Europa",
        "África",
        "Asia",
        "Oceanía",
    ]
    
    # Imprime el menú línea por línea con formato
    print("=" * ANCHO_TOTAL)
    print(menu_centro("Elige algún continente:"))
    print("-" * ANCHO_TOTAL)
    
    # Itera sobre la lista e imprime cada opción con formato
    for i, opcion_texto in enumerate(opciones, start=1):
        linea = f"  {i}. {opcion_texto}"
        print(f"{linea:<{ANCHO_TOTAL - 6}}  ") 
    print("=" * ANCHO_TOTAL)

def numero_opcion(rango):
    while True:
        try:
            entrada_usuario = int(input("Elija una opción: "))
            if entrada_usuario in range(1, rango +1):
                numero = int(entrada_usuario)
                return numero
        except ValueError:
                print("-" * ANCHO_TOTAL)
                print(menu_centro("Error: El dato ingresado no pertenece a ninguna opción. Inténtalo de nuevo."))
                print("-" * ANCHO_TOTAL)

def numero_entero(texto):
    while True:     
        num = input(texto)
        try:
            numero = int(num)
            return numero
        except ValueError:
            print("Error: El dato ingresado no es un numero. Inténtalo de nuevo.")

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
                except ValueError:
                    print(f"Advertencia: Se omitió una fila por datos inválidos: {fila}")
    except FileNotFoundError:
        print(f"Error: El archivo no se encontró en la ruta '{ruta_archivo}'")
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
        except KeyboardInterrupt:
            print("\n\nOperación cancelada por el usuario.")
            return validacion == False  
            # o podrías lanzar una excepción si lo prefieres
        except Exception as e:
            print(f"Error inesperado al leer la respuesta: {e}")
            print("Por favor, inténtelo de nuevo.")

def normalizar_manual(texto):
    """
    Reemplaza caracteres acentuados por su versión sin tilde
    y convierte a minúsculas.
    """
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

def imprimir_resutados(lista):
    ANCHO_NUM = 7
    ANCHO_NOMBRE = 30
    ANCHO_POB = 15
    ANCHO_SUP = 18
    ANCHO_CONT = 20
    print(f"\n{'#':>{ANCHO_NUM}} | {'Nombre':<{ANCHO_NOMBRE}} | {'Población':>{ANCHO_POB}} | {'Superficie (km²)':>{ANCHO_SUP}} | {'Continente':<{ANCHO_CONT}}")
    ANCHO_TOTAL = ANCHO_NUM + ANCHO_NOMBRE + ANCHO_POB + ANCHO_SUP + ANCHO_CONT + (4 * 3)
    print("-" * ANCHO_TOTAL)
    for con, pais in enumerate(lista, start=1):
        nombre = pais.get('nombre', 'Desconocido')
        poblacion = pais.get('poblacion', 'N/A')
        superficie = pais.get('superficie', 'N/A')
        continente = pais.get('continente', 'N/A')
        print(f"{con:>{ANCHO_NUM}} | {nombre:<{ANCHO_NOMBRE}} | {poblacion:>{ANCHO_POB}} | {superficie:>{ANCHO_SUP}} | {continente:<{ANCHO_CONT}}")
