<<<<<<< HEAD
import csv

def numero_opcion(rango):
    while True:
        entrada_usuario = input("Elija una opción:")        
        try:
            if int(entrada_usuario) in range(rango):
                numero = int(entrada_usuario)
            return numero
        except ValueError:
            print("Error: El dato ingresado no pertenece a ninguna opción. Inténtalo de nuevo.")



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
=======
def verificar_num(num):
    if num.isdigit():
        numero = int(num)
        return numero
>>>>>>> 4035f803ac34cfe54ca27a213ba370a5989e116e
