import csv

def numero_opcion(rango):
    while True:
        entrada_usuario = input("Elija una opción: ")        
        try:
            if int(entrada_usuario) in range(1, rango +1):
                numero = int(entrada_usuario)
            return numero
        except ValueError:
            print("Error: El dato ingresado no pertenece a ninguna opción. Inténtalo de nuevo.")

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
    """
    Solicita al usuario una respuesta de sí o no y devuelve un valor booleano.
    
    Parámetros:
        texto (str): Mensaje a mostrar al usuario (debe incluir la pregunta).
    
    Retorna:
        bool: True si la respuesta es afirmativa ('s', 'si', etc.), False si es negativa.
    
    Comportamiento:
        - Acepta: 's', 'si', 'y', 'yes' (y variantes en mayúsculas)
        - Acepta: 'n', 'no' (y variantes)
        - Si la entrada es inválida, repite la pregunta hasta obtener una respuesta válida.
    """
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