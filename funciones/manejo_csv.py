import funciones.mis_funciones as mis_funciones
import csv

encabezados = (
    "nombre",
    "poblacion",
    "superficie",
    "continente"
)

def agregar_pais(lista_paises):
    
    nombre_nuevo = input("¿Cómo se llama el nuevo país? \n")
    
    # 1. Verificamos si ya existe
    duplicado_encontrado = False
    for pais in lista_paises:
        nombre_pais = pais['nombre']
        if nombre_pais.lower() == nombre_nuevo:
            duplicado_encontrado = True
            break # Rompemos el bucle
            
    if duplicado_encontrado:
        print(f"Error: El país '{nombre_nuevo}' ya existe.")
        return

    # 2. Pedimos los OTROS datos
    try:
        poblacion_nueva = int(input(f"Población de {nombre_nuevo}? \n"))
        superficie_nueva = int(input(f"Superficie de {nombre_nuevo}? \n"))
        mis_funciones.menu_con()
        opcion = mis_funciones.numero_opcion(6)
        continentes = {
            1: "américa del sur",
            2: "américa del norte",
            3: "europa",
            4: "áfrica",
            5: "asia",
            6: "oceanía"
        }
        continente_nuevo = continentes.get(opcion, "").lower()
    except ValueError:
        poblacion_nueva = 0
        superficie_nueva = 0

    # 3. Creamos el nuevo "país" (el diccionario)
    nuevo_pais = {
        "nombre": nombre_nuevo,
        "poblacion": poblacion_nueva,
        "superficie": superficie_nueva,
        "continente": continente_nuevo
    }
    
    # 4. Lo añadimos a la lista
    lista_paises.append(nuevo_pais)
    print(f"¡País '{nombre_nuevo}' agregado con éxito!")


def editar_pais(lista_paises, encabezados, nombre_archivo_csv):

    buscar_pais = input("Qué país buscas editar? ").strip().lower()

    pais_para_editar = None

    for pais in lista_paises:
        # Compara ambos nombres en minúsculas y sin espacios
        nombre_pais_en_lista = pais["nombre"].strip().lower() 
        
        if nombre_pais_en_lista == buscar_pais:
            pais_para_editar = pais 
            break

    # Si "pais_para_editar" sigue siendo None, es que no se encontró.
    if pais_para_editar is None:
        print(f"Error: No se encontró el país '{buscar_pais}'.")
        return

    print(
        f"=" * mis_funciones.ANCHO_TOTAL,
        f"¿Qué necesitas editar de {pais_para_editar['nombre']}?",
        f"=" * mis_funciones.ANCHO_TOTAL,
        "1. Población",
        "2. Superficie",
        "3. Continente",
        "4. Cancelar",
        f"=" * mis_funciones.ANCHO_TOTAL,
        sep = "\n" # 'sep="\n"' imprime cada elemento en una nueva línea
    )
    opcion = mis_funciones.numero_opcion(4)
    
    hubo_cambios = False

    match opcion:
        case 1:
            nuevo_valor = input(f"Nueva población (actual: {pais_para_editar['poblacion']}): ")
            pais_para_editar['poblacion'] = nuevo_valor
            hubo_cambios = True

        case 2:
            nuevo_valor = input(f"Nueva superficie (actual: {pais_para_editar['superficie']}): ")
            pais_para_editar['superficie'] = nuevo_valor
            hubo_cambios = True

        case 3:
            nuevo_valor = input(f"Nuevo continente (actual: {pais_para_editar['continente']}): ")
            pais_para_editar['continente'] = nuevo_valor
            hubo_cambios = True
        
        case 4:
            print("Edición cancelada.")
        
        case _:
            print("Opción no válida.")

    if hubo_cambios:
        print("Guardando cambios en el archivo...")
        try:
            guardar_datos(nombre_archivo_csv, lista_paises, encabezados)
            print("✅ ¡Archivo actualizado con éxito!")
        except Exception as e:
            print(f"❌ Error al guardar el archivo: {e}")

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



